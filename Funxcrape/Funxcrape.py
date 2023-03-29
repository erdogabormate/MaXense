#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 2  13:47:09 2022
@author: Gabor Mate Erdo, 2022

FUNXcrape 1.1 - Protein Function Webscraper - Get all functionalities for your list of Uniprot links - Gabor Mate Erdo, 2022

"""
from selenium import webdriver
from bs4 import BeautifulSoup
from itertools import repeat
import chromedriver_binary
import requests
import re
import time
import Keyword_getter as kg

print("\n---------------------------------------\nStarting FUNXcrape 1.0 - make sure you have a stable connection.") 

Keywords, Categorynames = kg.Get_lists()
Categories=len(Categorynames)
 
start=time.time()

link_list=[]
with open ("uniprot_link_list.txt") as f: #filename for protein entry weblinks
    for line in f: 
        link_list.append(line.strip('\n'))

if len(link_list)<3: print("\nREALLY?!? You made a list of ",len(link_list)," entries, instead of just opening that in the browser?\nWOW!")

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

def get_function_entry(address):
    entry=""
    r = requests.get(address)
    soup = BeautifulSoup(r.text,features="lxml") #under features the parsing method is defined
    uniprot_website_function = soup.find_all("ul", {"class": "noNumbering biological_process"})
    entry=""
    for line in uniprot_website_function:
        entry+=str(line)
    return(entry) 

def get_protein_name_entry(address):
    entry=""
    r = requests.get(address)
    soup = BeautifulSoup(r.text,features="lxml") #under features the parsing method is defined
    uniprot_website_function = soup.find_all("div", {"id": "content-protein"},{"class": "entry-overview-content"})
    entry=""
    for line in uniprot_website_function:
        entry+=str(line)
    return(entry) 

def function_finder(uniprotentry):
    function_list=[]
    start_matches=re.finditer("GO-Term",uniprotentry) 
    function_start_positions=[12 + match.start() for match in start_matches]
    end_matches=re.finditer("</a><span class", uniprotentry)
    function_end_positions=[match.start() for match in end_matches]
    for i in range (len(function_start_positions)):
        function_list.append(uniprotentry[function_start_positions[i]:function_end_positions[i]])
    return function_list

def protein_name_finder(uniprotentry):
    protein_name_list=[]
    start_matches=re.finditer("h1 property=",uniprotentry) 
    protein_name_start_positions=[19 + match.start() for match in start_matches]
    end_matches=re.finditer("</h1>", uniprotentry)
    protein_name_end_positions=[match.start() for match in end_matches]
    for i in range (len(protein_name_end_positions)):
        protein_name_list.append(uniprotentry[protein_name_start_positions[i]:protein_name_end_positions[i]])
    return protein_name_list

data=[]  #protein functions
data2=[] #protein names
print ("\nCollecting all protein names and functions.\n")
total=len(link_list)
progress=0
for current_line in link_list:
    progress+=1
    entries=current_line.split(", ")
    functions=[]
    for word in entries:
        functions.append(function_finder(get_function_entry(word)))
    data.append(functions)
    
    proteinname=current_line.split(",")
    name_to_add=protein_name_finder(get_protein_name_entry(proteinname[0]))
    if name_to_add==[] and len(proteinname) > 1:
        name_to_add=protein_name_finder(get_protein_name_entry(proteinname[1]))
    data2.append(name_to_add)
    if int(progress/total*100)%5==0 and int(progress/total*100) > 0 and int((progress-1)/total*100)%5>0: print(int(progress/total*100),"% completed.")
         
print("\nData collection successful. Generating statistics.\n")

count = [0] * Categories
traits = 0		#shows the total number of functions identified with all entries
entry_count = 0 	#shows the number entries
relevant_proteins = [[] for i in repeat(None, Categories)]
empty=0

f = open("functionslist.txt", 'w')

for entry in data:
    traits+=len(entry)
    entry_count+=1
    if entry==[]:
         empty+=1
         continue
    f.write((str(entry)[1:-1]+ "\n").replace("'","").replace("[","").replace("]","").replace(", , ",""))
 
    for i in range (0,Categories):
        Category_count=0 
        for word in Keywords[i]:
            if "#" in word: continue
            if word.lower().strip("\n") in str(entry).lower(): 
                print("------\nProtein #",entry_count," - Hit found:",word,"- related to:",Categorynames[i],"------\n")
                Category_count+=1
                relevant_proteins[i].append(entry_count)
        count[i]+=Category_count
f.close()


f = open("protein_name_list.txt", 'w')
pncount=[0] * Categories
p_empty=0
p_count=0

for p_name in data2:
    p_count+=1
    f.write((str(p_name)[1:-1]+ "\n").replace("'",""))
    if p_name==[]:
        p_empty+=1
    '''
    for i in range (0,Categories):
        PN_Category_count=0 
        for word in Keywords[i]:
            if "#" in word: continue
            if word.lower().strip("\n") in str(p_name).lower(): 
                print("------\nProtein #",p_count," - Hit found:",word,"- related to:",Categorynames[i],"------\n")
                PN_Category_count+=1
                relevant_proteins[i].append(p_count)
        pncount[i]+=Category_count
    '''
f.close()

end=time.time()
runtime=str(end-start)[:5]


print("\nPROTEIN FUNCTION ANNOTATION SUMMARY:\nOut of ",entry_count,"different proteins, (with",empty,"empty entries) a total of ",traits," functions were identified. \nThe total number of hits for each functional category, and the corresponding proteins: \n")

for i in range (Categories):
    print(Categorynames[i], "(",count[i],")", relevant_proteins[i]) 

f = open("hits_by_category.txt", 'w')
for i in range (Categories):
    f.write(str(Categorynames[i][:-1]) + " ("+str(count[i])+")\n" + str(relevant_proteins[i]) + "\n")
f.close()

f = open("score_list.txt", 'w')
protein_score=[0]*(len(data)+1)
for i in range (1,len(data)+1):
    for j in relevant_proteins:
        protein_score[i]+=j.count(i)
    f.write((str(protein_score[i])+"\n").replace("'",""))
f.close()


if (end-start)<1200:
    print("\n---------------------------------------\nData scraping terminated in ",runtime,"seconds.\n---------------------------------------")
else:
    print("\n---------------------------------------\nData scraping terminated in ",int(int(runtime)/60),"minutes.\n---------------------------------------")