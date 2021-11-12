# module dna
#


# sequence, description = load(filename)
# Take the filename of a .fna file and return the DNA sequence and description line.
# The filename is str and is the path to the .fna file.
def load(filename):  # T1
    description = ''
    sequence = list()
    if filename[-4:] != '.fna':  # File format error
        description = 'file was not loaded'
    else:
        try:
            with open(filename, 'r') as fna:
                description = fna.readline().replace('>', '').replace('\n', '')  # Data format editing
                sequence = list(fna.read().upper().replace('\n', ''))  # Data format editing
        except IOError:  # file is unreachable
            print('file was not loaded')
    return sequence, description


# table = stats(sequence)
# Take a sequence and return a table that includes the number of times a nucleic acid code occurs.
def stats(sequence):  # T2
    codes = ['A', 'C', 'G', 'T', 'N', 'U', 'K', 'S', 'Y', 'M', 'W', 'R', 'B', 'D', 'H', 'V', '-']
    sequence = list(sequence)
    table = dict()
    count = list()
    for code in codes:
        count.append(sequence.count(code))

    table = dict(zip(codes, count))  # pack them like {codes[0]: count[0], codes[1]: count[1], ...}
    table.update(other=len(sequence) - sum(count))  # other = total chars - categorized

    return table


# formatted_sequences = format_sequence(sequence, first_index, last_index)
# Take a sequence along with two indices and return the subsequence with a particular format.
def format_sequence(sequence, first_index, last_index):  # T3
    formatted_sequences = list()
    for index in range(first_index, last_index, 80):
        if last_index - index > 80:
            formatted_sequences.append(''.join(sequence[index:index + 80]))
        else:  # it is the last line of seq which could be fewer than 80
            formatted_sequences.append(''.join(sequence[index:last_index + 1]))
    return formatted_sequences


# write(filename, description, sequence, first_index, last_index)
# Take a description, sequence, and sequence range, and write to a .fna file.
def write(filename, description, sequence, first_index, last_index):  # T4
    with open(filename, 'w') as fna:
        fna.write('>' + description + '\n')
        fna.write(''.join(sequence[first_index:last_index + 1]) + '\n')


# matches = find(sequence, sequence_to_find)
# Find a sequence within another sequence and record the indices where they occurred.
def find(sequence, sequence_to_find):  # T5
    matches = []
    sequence = ''.join(sequence)  # cast to str
    sequence_to_find = ''.join(sequence_to_find)

    count = sequence.count(sequence_to_find)
    # find the first appearance then set start param
    matches.append(sequence.find(sequence_to_find))
    for i in range(count - 1):
        matches.append(sequence.find(sequence_to_find, matches[-1] + 1))

    return matches


# new_sequence = add(sequence, sequence_to_add, index)
# Add a sequence into an existing sequence at a specified index.
def add(sequence, sequence_to_add, index):  # T6
    new_sequence = list(sequence)
    sequence_to_add = list(sequence_to_add)

    for i in range(len(sequence_to_add)):
        new_sequence.insert(index + i, sequence_to_add[i]) #Add at the specified position

    return new_sequence


# new_sequence = delete(sequence, index, number_of_codes)
# Delete a subsequence from a sequence as specified by a starting index and the number of codes to delete.
def delete(sequence, index, number_of_codes):  # T7
    new_sequence = list(sequence)
    for i in range(number_of_codes):
        try:
            new_sequence.pop(index)  #delete it
        except IndexError:
            break
    return new_sequence


# new_sequence = replace(sequence, sequence_to_add, index, number_of_codes)
# Replace a section of a sequence with a new subsequence.
def replace(sequence, sequence_to_add, index, number_of_codes):  # T8
    new_sequence = list(sequence)
    #  replace == delete and add
    new_sequence = add(delete(new_sequence, index, number_of_codes), sequence_to_add, index)
    return new_sequence


# protein_sequence, table = dna2protein(dna_sequence)
# Convert the DNA sequence to its corresponding protein sequence.
def dna2protein(dna_sequence):  # T9
    code = list()
    pro = list()
    table = dict()
    protein_sequence = list()
    try:
        with open('.\\dna2protein.csv', 'r') as database:
            for line in database:
                code.append(''.join(line.split(',')[0:3]))
                pro.append(line.split(',')[4])
    except IOError:
        print('file not found')
    code.append('???')
    pro.append('?')
    table = dict(zip(code, pro))
    for i in range(0, len(dna_sequence) - 2, 3):
        try:
            protein_sequence.append(table[''.join(dna_sequence[i:i + 3])])
        except KeyError:
            protein_sequence.append(table[''.join('???')])
    return protein_sequence, table
# 77777777777777后撤步
