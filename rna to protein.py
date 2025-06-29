from Bio.Seq import Seq

with open("rosalind_prot (2).txt","r") as f:
    data=f.read()
    
print(len(data))

if len(data)%3 ==1:
    data=data[:-1]
elif len(data)%3==2:
    data=data[:-2]
else:
    data=data
    
rna=Seq(data)
protein=rna.translate(to_stop=True)
print(protein)
