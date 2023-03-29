#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 3  14:57:11 2022
@author: Gabor Mate Erdo, 2022

ProteomiCSV 1.0 - Generates Excel-importable tsv - Gabor Mate Erdo, 2022

"""

import time

print("\n---------------------------------------\nCompiling offline data") 
 
start=time.time()

gene_list=[]
score_list=[]
prot_list=[]
hit_list=[]
category_list=[]
expression_list=[]
category_match=[]

with open ("genelist.txt") as genes: 
    for line in genes: 
        gene_list.append(line.strip('\n'))

with open ("protein_name_list.txt") as prots: 
    for line in prots: 
        prot_list.append(line.strip('\n'))

with open ("score_list.txt") as scores: 
    for line in scores: 
        score_list.append(line.strip('\n'))

with open ("hits_by_category.txt") as hits:
    for line in hits: 
        if line[-2:-1]==")":
            category_list.append(line.strip('\n'))
        else:
            hit_list.append(line.strip('\n'))
with open ("Expression.txt") as express: 
    for line in express: 
        expression_list.append(line.strip('\n'))

for index in range (0,len(gene_list)):
    category_match.append("")
    for entry in hit_list:
        entry=entry.replace(']',',').replace(" ",",").replace("[",",")
        search_string=(","+str(index)+",")
        if search_string in str(entry):
            category_match[index]+="\tX" 
        else: category_match[index]+="\t"

categories="\t".join(category_list)

f = open("Results.tsv", 'w')
f.write("index\tgene\tprotein_name\tkeyw_score\tdiff_exp\t"+categories+"\n")
for index in range(0, len(score_list)):
    f.write(str(index+1)+"\t"+str(gene_list[index])+"\t"+str(prot_list[index])+"\t"+str(score_list[index])+"\t"+str(expression_list[index])+category_match[index]+"\n")
f.close()
print("\nData compiled as tab separated values under Results.tsv.")
 
end=time.time()
runtime=str(end-start)[:5]
print("\n---------------------------------------\nData compiling finished in ",runtime,"seconds.\n---------------------------------------")

exit()
