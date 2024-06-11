
#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Parse the arguments
args = parser.parse_args()
args.seq = args.seq.upper()     

def calculate_nucleotide_percentage_DNA(sequence):
    
    # total length of the sequence
    total_length = len(sequence)
    
    # Count number of nucleotide on sequence 
    count_a = sequence.count('A')
    count_t = sequence.count('T')
    count_c = sequence.count('C')
    count_g = sequence.count('G')
    
    percentage_a = (count_a / total_length) * 100
    percentage_t = (count_t / total_length) * 100
    percentage_c = (count_c / total_length) * 100
    percentage_g = (count_g / total_length) * 100
    
    return percentage_a, percentage_t, percentage_c, percentage_g


def calculate_nucleotide_percentage_RNA (sequence):

    # total length of the sequence
    total_length = len(sequence)

    # Count number of nucleotide on sequence
    count_a = sequence.count('A')
    count_u = sequence.count('U')
    count_c = sequence.count('C')
    count_g = sequence.count('G')

    # Calculate the %  of each nucleotide
    percentage_a = (count_a / total_length) * 100
    percentage_u = (count_u / total_length) * 100
    percentage_c = (count_c / total_length) * 100
    percentage_g = (count_g / total_length) * 100

    return percentage_a, percentage_u, percentage_c, percentage_g


if re.search('^[ACGT]+$', args.seq):    # selecting the right function for DNA
    percentage_a, percentage_t, percentage_c, percentage_g = calculate_nucleotide_percentage_DNA(args.seq)
    print(f"Percentage of A:", percentage_a)
    print(f"Percentage of T:", percentage_t)
    print(f"Percentage of C:", percentage_c)
    print(f"Percentage of G:",  percentage_g)
elif re.search('^[ACGU]+$', args.seq):    # selecting the right function for RNA
    percentage_a, percentage_u, percentage_c, percentage_g = calculate_nucleotide_percentage_RNA(args.seq)
    print(f"Percentage of A:", percentage_a)
    print(f"Percentage of U:", percentage_u)
    print(f"Percentage of C:", percentage_c)
    print(f"Percentage of G:",  percentage_g)
else:
    print("The sequence is wrong")


