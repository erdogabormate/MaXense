'''
---------------
Link Parser 1.1 
---------------
Utility tool for generating all uniprot weblinks as from accession numbers or Proteome discoverer output.
'''

formated_list=[] 
with open ("proteinlist.txt") as f:
    counter=1
    linklist=[[]]
    for line in f:
        entry=[]
        linklist.append(line.replace("tr|","").replace("sp|","").replace(";tr","").replace(";sp","").replace(";","|").strip("\n").split("|"))
        for i  in range (len(linklist[counter])):
            if "MOrSE" not in linklist[counter][i]:
                entry.append("http://www.uniprot.org/uniprotkb/"+linklist[counter][i]+"/entry")
        counter+=1
        if entry !=[]:
            formated_list.append(entry)     

output = open("uniprot_link_list.txt", 'w')
for line in formated_list:
    output.write((str(line)[1:-1]+ "\n").replace("'",""))
f.close()

print("UniProt links have been parsed and saved under uniprot_link_list.txt. \n-Use getgenes.py to scrape coding genes. \n-Use Funxcrape.py to get scoring and functions.")