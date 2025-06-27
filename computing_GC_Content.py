#Given multiple DNA sequences in FASTA format, calculate the GC-content of each and identify the one with the highest GC-content.
#GC-content - What percentage of the DNA string is made up of just the letters G and C

f= open("rosalind_gc.txt","r")
data=f.read()

lines = data.strip().splitlines()
sequences = {}
label = ""

# Read sequences
for line in lines:
    if line.startswith(">"):
        label = line[1:]
        sequences[label] = ""
    else:
        sequences[label] += line.strip()

# Calculate GC content and find the highest
max_id = ""
max_gc = 0

for id, seq in sequences.items():
    gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
    if gc > max_gc:
        max_gc = gc
        max_id = id

print(max_id)
print(round(max_gc, 6))
    
