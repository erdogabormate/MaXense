#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 3  14:57:11 2021
@author: Gabor Mate Erdo, 2021

Phosphomotive 1.0 - Attributes of Phosphorylation motifs - Gabor Mate Erdo, 2021

"""
from collections import Counter
import re
import time

print("\n---------------------------------------\nPhosphomotive 1.0 - Statistical analysis of phosphorylation sites\n\n") 
 
start=time.time()

Peptide_list=[]
with open ("Peptide_sequences.txt") as f: #filename for peptide sequences
    for line in f: 
        Peptide_list.append(line.strip('\n'))

Motif_list=[]
with open ("Phosphosites.txt") as f: #filename for coordinates
    for line in f: 
        Motif_list.append(line.strip('\n'))

Code=[]
Acidity=[]
Class=[]
Charge=[]
Polarity=[]
Hydrophobicity=[]
with open ("AA_Conversion_Table.txt") as attributes:
    for a in attributes:
        b=re.sub(r"\W", "", a)
        Code.append(b[0].strip("\t"))
        Acidity.append(b[1].strip("\t"))
        Class.append(b[2].strip("\t"))
        Charge.append(b[3].strip("\t"))
        Polarity.append(b[4].strip("\t"))
        Hydrophobicity.append(b[5].strip("\t"))

# The Table contains the Code(1-letter aa code)	Acidity(Basic/Acidic/Neutral), Class(aLiphatic/aRomatic/Basic/Acidic/amiNe/Sulfur containing/Hydroxyl containting/Cyclic) and	Charge(Charged/Neutral), Polarity(Polar/Neutral) and Hydrophobicity(strongly Hydrophobic(H), hydrophobic(h), neutral(N), hydrophilic (W) in 6 tab-separated columns.

Motifs=[]
for line in Motif_list:
    newstring=''
    for letter in line:
        if letter=="X": 
            newstring+="X"
        if letter=="P":
            newstring+="P"
        if letter=="O":
            newstring+="O" 
    Motifs.append(newstring)


for a in range(0,len(Peptide_list)):
    for i in range (0,31):
        if Motifs[a][i]=="P": 
            Peptide_list[a]=Peptide_list[a][:i]+Peptide_list[a][i].lower()+Peptide_list[a][i+1:]
        if Motifs[a][i]=="O":
            Peptide_list[a]=Peptide_list[a][:i]+Peptide_list[a][i].lower()+Peptide_list[a][i+1:]

f = open("Sequences_marked.txt", 'w')
for a in Peptide_list:
    f.write((a+"\n").replace("'",""))
f.close()
print("\nA list of peptide sequences with case marked phosphorylation sites has been saved under Sequences_marked.txt\n\n")

Motif3_list=[]  
Motif5_list=[]
       
for a in range(0,len(Peptide_list)):
    for i in range (0,31):
        if i==0 and Peptide_list[a][i].islower(): Motif3_list.append(Peptide_list[a][i:i+2])
        if i==31 and Peptide_list[a][i].islower(): Motif3_list.append(Peptide_list[a][i-1:i+1])
        if i>0 and i<31 and Peptide_list[a][i].islower(): Motif3_list.append(Peptide_list[a][i-1:i+2])
        if i==0 and Peptide_list[a][i].islower(): Motif5_list.append(Peptide_list[a][i:i+3])
        if i==31 and Peptide_list[a][i].islower(): Motif5_list.append(Peptide_list[a][i-2:i+1])
        if i==1 and Peptide_list[a][i].islower(): Motif5_list.append(Peptide_list[a][i-1:i+3])
        if i==30 and Peptide_list[a][i].islower(): Motif5_list.append(Peptide_list[a][i-2:i+2])
        if (i>1 and i<30) and Peptide_list[a][i].islower(): Motif5_list.append(Peptide_list[a][i-2:i+3])

for i in range (0, len(Motif3_list)):
    if len(Motif3_list[i])==2 and Motif3_list[i][1].islower(): Motif3_list[i]=Motif3_list[i]+"#"
    if len(Motif3_list[i])==2 and Motif3_list[i][0].islower(): Motif3_list[i]="#"+Motif3_list[i]

for i in range (0, len(Motif5_list)):
    if len(Motif5_list[i])==4 and Motif5_list[i][3].islower(): Motif5_list[i]=Motif5_list[i]+"#"
    if len(Motif5_list[i])==4 and Motif5_list[i][0].islower(): Motif5_list[i]="#"+Motif5_list[i]
    if len(Motif5_list[i])==4 and Motif5_list[i][2].islower(): Motif5_list[i]=Motif5_list[i]+"#"
    if len(Motif5_list[i])==4 and Motif5_list[i][1].islower(): Motif5_list[i]="#"+Motif5_list[i]
    
    if len(Motif5_list[i])==3 and Motif5_list[i][2].islower(): Motif5_list[i]=Motif5_list[i]+"##"
    if len(Motif5_list[i])==3 and Motif5_list[i][0].islower(): Motif5_list[i]="##"+Motif5_list[i]

cnt = Counter()
for motif in Motif3_list:
          if len(motif)!=3: print(motif)
          cnt[motif]+=1

cnt = Counter()
for motif in Motif5_list:
          if len(motif)!=5: print(motif)
          cnt[motif]+=1

cnt = Counter()
for peptide in Peptide_list:
      for letter in peptide:
          cnt[letter]+=1

print("Amino acids by frequency in peptide chains:\n--------------------------\n", cnt.most_common(25))

Acidity3_list=[]
Class3_list=[]
Charge3_list=[]
Polarity3_list=[]
Hydrophobicity3_list=[]

#-------conversion of aminoacids to attributes in motifs of n=3

for motif in Motif3_list:
    new_aciditymotif=motif
    new_classmotif=motif
    new_chargemotif=motif
    new_polaritymotif=motif
    new_hydrophobicitymotif=motif
    for b in range (0,3):
        for a in range (0, 20):
            if Code[a]==motif[b]:  
                new_aciditymotif=new_aciditymotif[:b]+Acidity[a]+new_aciditymotif[b+1:]
                new_classmotif=new_classmotif[:b]+Class[a]+new_classmotif[b+1:]
                new_chargemotif=new_chargemotif[:b]+Charge[a]+new_chargemotif[b+1:]
                new_polaritymotif=new_polaritymotif[:b]+Polarity[a]+new_polaritymotif[b+1:] 
                new_hydrophobicitymotif=new_hydrophobicitymotif[:b]+Hydrophobicity[a]+new_hydrophobicitymotif[b+1:]
                break
    Acidity3_list.append(new_aciditymotif)
    Class3_list.append(new_classmotif)
    Charge3_list.append(new_chargemotif)
    Polarity3_list.append(new_polaritymotif)
    Hydrophobicity3_list.append(new_hydrophobicitymotif)

#-------conversion of aminoacids to attributes in motifs of n=5

Acidity5_list=[]
Class5_list=[]
Charge5_list=[]
Polarity5_list=[]
Hydrophobicity5_list=[]

for motif in Motif5_list:
    new_aciditymotif=motif
    new_classmotif=motif
    new_chargemotif=motif
    new_polaritymotif=motif
    new_hydrophobicitymotif=motif
    for b in range (0,5):
        for a in range (0, 20):
            if Code[a]==motif[b]: 
                new_aciditymotif=new_aciditymotif[:b]+Acidity[a]+new_aciditymotif[b+1:]
                new_classmotif=new_classmotif[:b]+Class[a]+new_classmotif[b+1:]
                new_chargemotif=new_chargemotif[:b]+Charge[a]+new_chargemotif[b+1:]
                new_polaritymotif=new_polaritymotif[:b]+Polarity[a]+new_polaritymotif[b+1:] 
                new_hydrophobicitymotif=new_hydrophobicitymotif[:b]+Hydrophobicity[a]+new_hydrophobicitymotif[b+1:]
                break
    Acidity5_list.append(new_aciditymotif)
    Class5_list.append(new_classmotif)
    Charge5_list.append(new_chargemotif)
    Polarity5_list.append(new_polaritymotif)
    Hydrophobicity5_list.append(new_hydrophobicitymotif)

cnt = Counter()
for motif in Motif3_list:
      cnt[motif[2]]+=1
print("Most common motifs of length 3:\n",cnt.most_common(27))


print("Amino acid motifs\n--------------------------\n")
cnt = Counter()
for motif in Motif3_list:
      cnt[motif]+=1
print("Most common motifs of length 3:\n",cnt.most_common(15))
print("Unique motifs of length 3:",len(cnt))
cnt = Counter()
for motif in Motif5_list:
      cnt[motif]+=1
print("\nMost common motifs of length 5:\n",cnt.most_common(10))
print("Unique motifs of length 5:",len(cnt))


print("Acidity (A: Acidic, N: Neutral, B: Basic)\n--------------------------\n")
cnt = Counter()
for motif in Acidity3_list:
      cnt[motif]+=1
print("Most common Acidity motifs of length 3:\n",cnt.most_common(15))
print("Unique motifs of length 3:",len(cnt))
cnt = Counter()
for motif in Acidity5_list:
      cnt[motif]+=1
print("\nMost common Acidity motifs of length 5:\n",cnt.most_common(10))
print("Unique motifs of length 5:",len(cnt),"\n\n")

print("Class (L: Aliphatic, R: Aromatic, B: Basic, A: Acidic, N: Amine, S: Sulfur Containing, H: Hydroxyl containing C: Circular)\n--------------------------\n")
cnt = Counter()
for motif in Class3_list:
      cnt[motif]+=1
print("Most common Class motifs of length 3:\n",cnt.most_common(15))
print("Unique motifs of length 3:",len(cnt))
cnt = Counter()
for motif in Class5_list:
      cnt[motif]+=1
print("\nMost common Class motifs of length 5:\n",cnt.most_common(10))
print("Unique motifs of length 5:",len(cnt),"\n\n")

print("Charge (C: Charged, N: Not charged)\n--------------------------\n")
cnt = Counter()
for motif in Charge3_list:
      cnt[motif]+=1
print("Most common Charge motifs of length 3:\n",cnt.most_common(15))
print("Unique motifs of length 3:",len(cnt))
cnt = Counter()
for motif in Charge5_list:
      cnt[motif]+=1
print("\nMost common Charge motifs of length 5:\n",cnt.most_common(10))
print("Unique motifs of length 5:",len(cnt),"\n\n")

print("Polarity (P: Polar, N: Not polar)\n--------------------------\n")
cnt = Counter()
for motif in Polarity3_list:
      cnt[motif]+=1
print("Most common Polarity motifs of length 3:\n",cnt.most_common(15))
print("Unique motifs of length 5:",len(cnt))
cnt = Counter()
for motif in Polarity5_list:
      cnt[motif]+=1
print("\nMost common Polarity motifs of length 5:\n",cnt.most_common(10))
print("Unique motifs of length 5:",len(cnt),"\n\n")

print("Hydrophobicity (H: Strongly hydrophobic, h: Hydrophobic, N: neutral, W: Hydrophilic)\n--------------------------\n")
cnt = Counter()
for motif in Hydrophobicity3_list:
      cnt[motif]+=1
print("Most common Hydrophobicity motifs of length 3:\n",cnt.most_common(15))
print("Unique motifs of length 3:",len(cnt))
cnt = Counter()
for motif in Hydrophobicity5_list:
      cnt[motif]+=1
print("\nMost common Hydrophobicity motifs of length 5:\n",cnt.most_common(10))
print("Unique motifs of length 5:",len(cnt),"\n\n")


end=time.time()
runtime=str(end-start)[:5]
print("\n---------------------------------------\nData compiling finished in ",runtime,"seconds.\n---------------------------------------")

exit()




