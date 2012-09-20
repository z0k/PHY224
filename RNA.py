DNA = 'ACGT'
RNA = 'UGCA'

dna = raw_input('Enter a DNA sequence: ')
rna = []

for i in dna:
    pair = DNA.index(i)
    new = RNA[pair]
    rna.append(new)

print ''.join(rna)
