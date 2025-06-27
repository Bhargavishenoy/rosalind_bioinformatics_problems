"""Hamming distance is a measure of the difference between two strings of equal length. It counts the number of positions at which the corresponding characters are different."""

def Hamming_distance(data):
    lines = data.strip().splitlines()
    
    seq1 = ""
    seq2 = ""

    for line in lines:
        if not seq1:
            seq1 += line.strip()
        else:
            seq2 += line.strip()

    # Now compare both sequences
    count = 0
    for a, b in zip(seq1, seq2):
        if a != b:
            count += 1

    return count

# Read file
f = open("rosalind_hamm.txt", "r")
data = f.read()
print(Hamming_distance(data))



