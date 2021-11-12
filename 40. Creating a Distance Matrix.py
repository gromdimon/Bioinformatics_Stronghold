def hamming_dist(string1, string2):
    # Calculating distance (number of mismatches) of two strings
    return sum([x != y for x, y in zip(string1, string2)])

def distance_matrix(strings):
    str_len = len(strings[0])
    dist_mat = []  # List of lists
    for str1 in strings:  # The first string
        current_row = []  # list
        for str2 in strings:  # The second string
            current_row.append(hamming_dist(str1, str2) / str_len)
        dist_mat.append(current_row)
    return dist_mat

def extract_sequence_from_input(file):
    sequences = []
    result = ""
    for line in file:
        if ">" in line:
            sequences.append(result)  # Appending sequence list with final seq
            result = ""  # Initiation of a new seq
        else:
            if "\n" in line:
                result += line[:len(line) - 1]  # Lengthening of sequence
            else:
                result += line
    sequences.append(result)  # Appending list with last seq
    sequences.remove('')
    return sequences

f = open('test.txt')
s = extract_sequence_from_input(f)
distance_mat = distance_matrix(s)

for row in distance_mat:
    print(' '.join(["%.3f" % x for x in row]))
