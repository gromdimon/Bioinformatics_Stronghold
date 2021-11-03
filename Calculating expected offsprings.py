# Reading file
file = open('test.txt')
lines = file.readlines()
individuals = [int(i) for i in lines[0].split(" ")]
# Counting dominant offsprings
# AA-AA (1) AA-Aa (1) AA-aa (1) Aa-Aa (0.75) Aa-aa (0.5) aa-aa (0)
print(2 * (individuals[0] + individuals[1] + individuals[2] + individuals[3] * 3 / 4 + individuals[4] / 2))