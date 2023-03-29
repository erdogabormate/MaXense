
MaXense Bundle for functional proteomics analysis and scoring - 2nd Release mid 2022 (developed by Gabor Mate Erdo) free for public use, providing following reference:
MaXense Bundle v1.1 - Gabor Máté Erdö 

-------------
MaXense 1.1 
-------------

1. PURPOSE

MaXense is a toolset for the support of genomic, transcriptomic and proteomic analysis by scraping relevant data from uniprot and implementing functional scoring.
Data is generated in Microsoft Excel importable format - adequately to output for further Analysis. 
A variety of tools to support this, their required input formats and outputs are described in detail in the following section.


2. USAGE

Use the utility tools provided with Funxcrape to get your data in the right format. 
All tools function without arguments, but data must be provided in the relevant formats. 
Length of input is arbitrary yet any modification of output data can lead to glitches while compiling. 
It is strongly advised to do such corrections and editing at the very first step, or in the final imported results table.

The first step is to generate the uniprot links based on the proteome discoverer output or UniProt IDs. 
An example of the required data format is provided under proteinlist.txt. 
Multiple entries per line are possible and will all be parsed under the same index for functional annotation.
This helps to get a full overview of functions as some entries are poorly annotated.


-------------------
2.1. Linkparser 1.1 
-------------------

Run linkparser.py to generate a list of UniProt links, these will be required for webscraping gene names and functional annotation.

	INPUT Data: 

		proteinlist.txt - a list of accession numbers or proteome discoverer output.
	
	OUTPUT Data: 
		
		uniprot_link_list.txt - a list of links (can be multiple links per line) as an input for the webscraper.


-------------------
2.2. GENEScrape 1.1
-------------------

Once uniprot_link_list.txt is generated you can procede with GENEScrape - executed via getgenes.py.

Before getgenes.py or FunXcrape starts working you might need to install some libraries listed below:

pip install selenium
pip install bs4
pip install chromedriver_binary  #needs to be compatible with version of Google Chrome
pip install requests 
pip install lxml

These are essential for the webscraping funtionalities - see also Section 3.

Launch getgenes.py to webscrape the genes names coding for the proteins. 
With this you can already start exploring Proteome networks in String, Cytoscape or other well known tools.

	INPUT Data: 

		uniprot_link_list.txt - a list of links (can be multiple links per line) as an input for the webscraper.

	OUTPUT Data: 

		genelist.txt - a list of genes in sequential order.

The genelist takes the primary accession number and if no matching gene is found continues to the next one. 
A gene is often referred in multiple different ways. CD markers typically have a common name and name starting with CD. 
Currently the package does not contain any tools to account for this but will in the future be extended to allow for a more wholesome analysis.
		

-----------------
2.3 FunXcrape 1.1 
-----------------

The next step is to check for functional annotation and score them against keywords related to certain topics of interest.
Funxcrape is searching for biological functions - but the code can be modified to find cellular location, etc.

Prepare lists that contain a short description of the feature/topic they relate to in the header, and relevant keywords or or keyword chunks.
Place these in sequential order into the Keyword_lists subfolder, and Funxcrape will parse through them. One line should contain one entry.
In case you use chunks make sure they are long and specific enough not to generate hits irrelevant to your topic of interest. 

An example of bad and a good keyword chunk:
- "pH" for example would produce hits against "phosphorylation", "phagocyte" etc. 
- Whereas "acidi" would produce hits against "acidic", "acidity",but not against "placid" - fulfilling the criteria of specificity.

Preparing a list requires attention and in-depth knowledge of a topic. By reading 5-6 relevant articles a high level of saturation can be reached. 
Also some keywords will never be matched against functional GO Annotations - so being familiar with these might save time.

Having the same keyword in multiple lists will lead to biased scoring, so try to avoid this if you want to use the scoring function as is. 
The listcompare.py tool helps to spot this by comparing two lists (List1.txt and List2.txt) and can easily be generalized to compare all lists against each other.

	INPUT Data: 
		
		Keyword_lists/list1.txt - a list (or more lists with sequential numbering) of relevant functions. 
		In case you are not interested in particular functions create an empty list.
		
		uniprot_link_list.txt - contains the list of Uniprot links the webscraper will use to get the data. 

	OUTPUT Data:
		
		functionslist.txt - contains the functions of all proteins. For lines containing multiple entries all functional annotations are included in the list.
		
		score_list.txt - A cumulative score given based on the number of matches against a specific keyword. 2-2 keyword matches against 2 lists will result in a score of 4.
		
		hits_by_category.txt
		
		protein_name_list.txt


-------------------
2.4 Pathofinder 1.0
-------------------

Executed through Pathofinder.py. A tool written to highligh pathogenic associations based on lists - these are prepared based on medical assocociations, HGMD and a review of relevant gene panels.


	INPUT Data: 

		Patho_lists/List1.txt - A list (or more sequentially numbered lists) of comma separated genes with pathogenic association - header line indicates the associated disease.

	OUTPUT Data:

		patho_GENES.tsv: A list containing indeces, genes, scores - the number of pathogenic associations, and the associations themselves.


------------------
2.5 Funximport 1.0  
------------------

Executed through Funximport.py. Generates Excel-importable .tsv file compiling all data generated before enabling filtering on multiple features, and exploring and generating new datasets. 

	
	INPUT Data:
	
		genelist.txt - see above (output of getgenes.py)

		functionslist.txt - see above (output of Funxcrape.py)
		
		score_list.txt - A cumulative score given based on the number of matches against a specific keyword. 2-2 keyword matches against 2 lists will result in a score of 4.
		
		hits_by_category.txt - see above (output of Funxcrape.py)
		
		protein_name_list.txt - see above (output of Funxcrape.py)
	
		expression.txt - and export of positive and negative integers matching the sequence of proteins. 

	OUTPUT Data: 

		Results.tsv


3.)  DEVELOPER'S NOTES

Currently as of March 2023 the code is under revision as the website structure of Uniprot has susbstantially changed. 
This affects the functionality of all webscraping tools (Genescrape and Funxcrape) and also the linkparser - this latter has been updated based on the new website sturcture. 

The code is currently under review - an update should be available by the end of April. 
As of July 2022 the same code was working and results were fetched from the website and imported in excel for the Molecular and Systems Biology Group of the University of Vienna.


 

