import os.path
from itertools import repeat

path = 'Patho_lists'
num_files = len([f for f in os.listdir(path) if "List" in f and os.path.isfile(os.path.join(path, f))])

def Get_lists():
    Listnames=[]
    for i in range (1, num_files+1):
        filename="List"+str(i)+".txt"
        Listnames.append(filename)
    listindex=0
    Category = [[] for i in repeat(None, num_files)]
    for List in Listnames:
        with open(path+"/"+List) as Categories:
            for line in Categories:
                Category[listindex].append(line)
        listindex+=1
    Categoryname=[] * num_files
    for i in range (num_files):
        Categoryname.append(Category[i].pop(0))
    return Category, Categoryname
