#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19  21:57:11 2022
@author: Gabor Mate Erdo, 2022

Pathofinder 1.0 - Checks geneset for known pathogenic associations - Gabor Mate Erdo, 2022

"""
import time
import Patho_getter as pg

print("\n---------------------------------------\nChecking geneset for pathogenic associations") 
 
start=time.time()

gene_list=[]
Categorynames=[]
Keywords=[]
pathocount=0
pathogenecount=0

Keywords, Categorynames = pg.Get_lists()

with open ("genelist.txt") as genes:
    for line in genes: 
        gene_list.append(line.strip('\n'))

Category_scores=[""]*len(gene_list)

for index in range (0,len(gene_list)):
    Category_index=0
    for pathogeneset in Keywords:
        if gene_list[index]!="":
            searchstring=str(gene_list[index]).lower()
        else: searchstring="MISSING GENE"
        if searchstring in str(pathogeneset).lower():
            Category_scores[index]+=Categorynames[Category_index].strip()+"\t"
            pathocount+=1
        Category_index+=1

for i in range (0, len(gene_list)):
    if Category_scores[i]!="":
        print("Gene ", gene_list[i]," has the following pathogenic association(s):",Category_scores[i])
        pathogenecount+=1

f = open("PathoGENES.tsv", 'w')
f.write("index\tgene\tscore\tpathogenic_associations\n")
for index in range(0, len(gene_list)):
    f.write(str(index+1)+"\t"+str(gene_list[index])+"\t"+str(Category_scores[index].count(":"))+"\t"+str(Category_scores[index])+"\n")
f.close()

print("\nData compiled as tab separated values under PatoGENES.tsv. A Total of",pathocount," pathogenic associations have been found in",pathogenecount,"genes (",str(pathogenecount/len(gene_list)*100)[:4],"% ).")



end=time.time()
runtime=str(end-start)[:5]
print("\n---------------------------------------\nSearch finished in ",runtime,"seconds.\n---------------------------------------")

exit()