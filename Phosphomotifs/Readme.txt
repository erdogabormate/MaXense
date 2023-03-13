
-----------------------
Phosphomotifs 1.0
-----------------------

1. Purpose

Phosphomotifs is a tool for the support of phosphoproteomic analysis. 

1.a Phosphomotifs converts uppercase motifs of -15/+15 radius motifs to lowercase where phosphorylation of methionine sulphoxydation are annotated.
Motifs are 31-digit uppercase string sequences, see an example in Peptide_sequences.txt. 
Annotation is required in (X; Oxidation (M); Phospho (STY)) format, see example in Phosphosites.txt. 

1.b Phosphomotifs allows the assessment of motifs based on different attributes:

- Acidity of sidechain:   B: Basic, N: Neutral, A: Acidic)
- Side Chain Class:   L: aLiphatic; R: aRomatic; B:Basic; A:Acidic; N: amiNe containing; S: Sulfur containing; H:Hydroxyl containing; C: Cyclic
- Charge:   N: Not charged; C: Charged
- Polarity:   N: Non-polar; p: Polar; P: Highly polar
- Hydrophobicity   W: Hydrophilic, h: Hydrophobic (scores 0-70); H: Highly Hydrophobic (scores 70-100)

Motifs are converted accordingly, and frequencies of motifs of length 3 and 5 are displayed, with the phosphorylation site being represented as "s", "t" or "y", corresponding to aminoacid 1-Letter codes.
 Sulphoxidated metionine sites are displayes as "m". 

2. Usage

Simply launch Phosphomitfs.py with the following three input files in the same folder:
- AA_Conversion_Table.txt (contains one-letter codes and conversion based on 1.b) - should not be changed unless new functionality is added.

- Phosphosites.txt (contains an annotation in each line in the following format: "X;X;X;X;X;X;X;X;X;X;X;X;X;X;X;Phospho (STY);X;X;X;X;X;X;X;X;X;X;X;X;X;X;X", see 1.a.
- Peptide_sequences.txt (contains amino acid sequences in the following format: "GEATAERPGEAAVASSPSKANGQENGHVKVN"
These letter two should be represent the same dataset in the same order.

An output corresponding to 1.a is generated: "Sequences_marked.txt"
Statistics corresponding to 1.b are displayed as output.



 

