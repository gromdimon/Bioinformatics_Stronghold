def probability_of_motif(string, gc, tries):
    # The function calculates probability of motif by multiplying probability of each nucleotide
    prob_list = {'G':(gc / 2), 'C':(gc / 2), 'A':((1 - gc) / 2), 'T':((1 - gc) / 2)}
    percent = 1
    for nucl in string:
        percent *= prob_list[nucl]
    return 1 - ((1 - percent) ** tries)

# Reading file
file = open('test.txt')
lines = file.readlines()
lines[0] = lines[0].rstrip()
tries, gc_content = lines[0].split(' ')
tries = int(tries)
gc_content = float(gc_content)
motif = lines[1].rstrip()
print(probability_of_motif(motif, gc_content, tries))
