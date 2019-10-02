def DNA_strand(dna):
    translated = ''
    nucleotide = {
        'C': 'G',
        'G': 'C',
        'A': 'T',
        'T': 'A'
    }
    
    for i in dna:
        translated += nucleotide[i]
    return translated
