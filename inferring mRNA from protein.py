'''
Inferring mRNA from Protein meansGiven a protein string, how many possible mRNA sequences could have produced this protein
'''

# number of codons for each amino acid
codon_table = {
    'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2,
    'W': 1, 'P': 4, 'H': 2, 'Q': 2, 'R': 6,
    'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2,
    'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4
}

# 3 stop codons: UAA, UAG, UGA
stop_codons = 3

# Input: protein string
protein = open("rosalind_mrna.txt","r")
protein = protein.read().strip()

# Total possible mRNA sequences
result = stop_codons

for amino_acid in protein:
    result *= codon_table[amino_acid]
    result %= 1000000 

print(result)

