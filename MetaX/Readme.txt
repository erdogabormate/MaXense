
MaXense Bundle for functional proteomics analysis and scoring - 2nd Release mid 2022 (developed by Gabor Mate Erdo) free for public use, providing following reference:
MaXense Bundle v1.1 - Gabor Máté Erdö 

-------------
MetaX 1.0 
-------------

1. PURPOSE

MetaX 1.0 creates an interaction matrix using descriptons of metabolites and annotations of their reactions, precursors and derivatives by crosschecking metabolite occurence in these annotations.
Interactions, where found are indicated by '1', while the desired level of indicated interactions (direct / indirect / secondary derivative) can be adjusted via the annotations.
This interaction matrix can be used for Jacobi transformation of metabolites togethher with other tools developed at the department of Molecular and systems biology.


2. USAGE

	INPUT data:

		Metabolite_function_list.csv - a semicolon separated list, each line contains the following separated entries: 
			-metabolite name
			-metabolite involvment in pathways
			-upstream effectors
			-precursors and derivatives

	OUTPUT data: 

		Matrix.txt - a comma separated list of metabolite interactions in sequence of the original metabolites.




