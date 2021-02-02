# algoritmo de tradução de RNA para proteína

# modules
import re  # for regular expressions

f = open('coddon_table.txt')


for line in f:
    line = line.strip()
    line = [(codon.split(' ')[0], codon.split(' ')[1])
            for codon in re.split(r'[ ]{2, 3}', line) if codon]

    for r in line:
        print(r[0])
        table[[r[0]]] = r[1]
