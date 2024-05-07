def DNA_strand(dna):
    switch = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    return ''.join([switch[letter] for letter in dna])
