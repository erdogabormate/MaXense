#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 3  14:57:11 2022
@author: Gabor Mate Erdo, 2022

MetaX 1.0 - Creates an interaction Matrix of based on Metabolite name, function, precursors and derivatives - Gabor Mate Erdo, 2022

"""

Metabolite_list=[]
with open ("Metabolite_function_list.csv") as f: #filename for 3 column .csv export of metabolites, functions and reaction products/precursors
    for line in f: 
        Metabolite_list.append(line.strip('\n').lower())

if len(Metabolite_list)<5: print("\nREALLY?!? You made a list of ",len(Metabolite_list)," entries, instead of just making the Matrix yourself?\nWOW!")

total=len(Metabolite_list)
progress=0

m_names=[]
keywords=[]

for current_line in Metabolite_list:
    progress+=1
    entries=current_line.split(";")
    m_names.append(entries[0])
    keywords.append((entries[1])+" "+entries[2])

matrix = [ [ 0 for i in range(total) ] for j in range(total) ]

interaction_count=0
interaction_list=[]

for a in range(0,total):
    for b in range(0, total):
        if m_names[a] in keywords[b]: 
            matrix[a][b]+=1
            print(m_names[a]," has a match.")
            interaction_count+=1
            interaction_list.append(str(a)+"->"+str(b))
print(interaction_count,"interactions in total: \n",interaction_list)
print(matrix)

f = open("Matrix.txt", 'w')
for a in matrix:
    f.write((str(a)[1:-1]+ "\n").replace("'",""))
f.close()
print("\nMatrix has been saved as Matrix.txt")
exit()
 



