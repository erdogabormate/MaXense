l1_list=[]
l2_list=[]
l1_in_l2=[]
l2_in_l1=[]


with open ("List1.txt") as l1: 
    for line in l1: 
        l1_list.append(line.strip('\n'))

with open ("List2.txt") as l2: 
    for line in l2: 
        l2_list.append(line.strip('\n'))

for gene in l1_list:
    if gene in l2_list: l1_in_l2.append(gene)

for gene in l2_list:
    if gene in l1_list: l2_in_l1.append(gene)

f = open("l1_in_l2.txt", 'w')
for gene in l1_in_l2:
    f.write(gene+"\n")

f = open("l2_in_l1.txt", 'w')
for gene in l2_in_l1:
    f.write(gene+"\n")
print(len(lung_in_bmdm))