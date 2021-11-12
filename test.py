import dna
#there is the test file


if __name__ == '__main__':
    seq, info = dna.load('.\\BRCA1.fna')
    print(info)
    print(seq[0:80])

    table = dna.stats(seq)
    print(table)

    data = dna.format_sequence(seq, 100, 300)
    print(data)

    dna.write('BRCA1_subseq.fna', 'fragment sequence of BRCA1.fna', seq, 100, 300)

    seq = list('AAAGTTAAATAATAAATAGGTGAA')
    seq_to_find = list('AAA')
    matches = dna.find(seq, seq_to_find)
    print(matches)

    line = ''
    seq = list('AAAGTTAAATAATAAATAGGTGAA')
    print(line.join(seq))
    seq = dna.add(seq, list('NNNNN'), 5)
    print(line.join(seq))

    seq = dna.delete(seq, 6, 4)
    print(line.join(seq))

    seq = dna.replace(seq, list('HHH'), 5, 1)
    print(line.join(seq))

    dna_seq = list('AAAGTTAAATAATAAATAGGTGAA') #666这个字典输出是啥顺序。。哈希 要不给加点注释吧okk
    pro_seq, table = dna.dna2protein(dna_seq)
    print(pro_seq)
    print(table)
