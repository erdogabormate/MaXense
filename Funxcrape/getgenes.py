#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 9  14:57:11 2022
@author: Gabor Mate Erdo, 2022

GENEScrape 1.0 - GENEScrape Webscraper - Get all genes and their interrelationship for your list of Uniprot links - Gabor Mate Erdo, 2022

"""
from selenium import webdriver
from bs4 import BeautifulSoup
from itertools import repeat

from selenium.webdriver.chrome.service import Service
ser = Service(r"C:/Users/MErdoe/.wdm/drivers/chromedriver/win32/chromedriver.exe")
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)


#import chromedriver_binary
import requests
import re
import time
import Keyword_getter as kg

print("\n---------------------------------------\nGetting genes - make sure you have a stable connection.") 

'''
from selenium.webdriver.chrome.service import Service
s=Service('C:/Users/MErdoe/.wdm/drivers/chromedriver/win32/chromedriver.exe')
browser = webdriver.Chrome(service=s)
url='https://www.google.com'
browser.get(url)
'''

from selenium.webdriver.chrome.service import Service
ser = Service(r"C:/Users/MErdoe/.wdm/drivers/chromedriver/win32/chromedriver.exe")
op = webdriver.ChromeOptions()
s = webdriver.Chrome(service=ser, options=op)



Keywords, Categorynames = kg.Get_lists()
Categories=len(Categorynames)
 
start=time.time()

link_list=[]
with open ("uniprot_link_list.txt") as f: #filename for protein entry weblinks
    for line in f: 
        link_list.append(line.strip('\n'))

if len(link_list)<3: print("\nREALLY?!? You made a list of ",len(link_list)," entries, instead of just opening that in the browser?\nWOW!")

#driver = webdriver.Chrome("/usr/local/bin/chromedriver")
#driver = webdriver.Chrome("/Users/MErdoe/.wdm/drivers/chromedriver/win32/chromedriver")

def get_gene_name_entry(address):
    entry=""
    r = requests.get(address)
    soup = BeautifulSoup(r.text,features="lxml") 
    #under features the parsing method is defined - use (r.text,features="lxml") or (s,  "html.parser") or (html, "html5lib")
    uniprot_website_function = soup.find_all("div", {"id": "content-gene"},{"class": "entry-overview-content"})
    entry=""
    for line in uniprot_website_function:
        entry+=str(line)
    return(entry)

def gene_name_finder(uniprotentry): 
    gene_name_list=[]
    start_matches=re.finditer("<h2>",uniprotentry) 
    gene_name_start_positions=[match.end() for match in start_matches]
    end_matches=re.finditer("</h2>", uniprotentry)
    gene_name_end_positions=[match.start() for match in end_matches]
    for i in range (len(gene_name_end_positions)):
        gene_name_list.append(uniprotentry[gene_name_start_positions[i]:gene_name_end_positions[i]])
    return gene_name_list

data3=[] #gene names
print("\nCollecting genes.")
total=len(link_list)
progress=0

for current_line in link_list:
    progress+=1
    entries=current_line.split(", ")
    genename=current_line.split(",")
    name_to_add=gene_name_finder(get_gene_name_entry(genename[0]))
    if name_to_add==[] and len(genename) > 1:
        name_to_add=gene_name_finder(get_gene_name_entry(genename[1]))
    data3.append(name_to_add)
    if int(progress/total*100)%5==0 and int(progress/total*100) > 0 and int((progress-1)/total*100)%5>0: print(int(progress/total*100),"% completed.")

f = open("genelist.txt", 'w')  #Saves output data under genelist.txt - based on this analysis can already be started while the parser collects functions
for p_name in data3:
    f.write((str(p_name)[1:-1]+ "\n").replace("'",""))
f.close()
print("\nGene names collected and saved under genelist.txt.")
exit()
 
end=time.time()
runtime=str(end-start)[:5]
print("\n---------------------------------------\nData scraping terminated in ",runtime,"seconds.\n---------------------------------------")






