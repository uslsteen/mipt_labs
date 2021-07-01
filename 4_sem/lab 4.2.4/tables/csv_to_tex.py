#!/usr/bin/env python3

import argparse
import csv


def csv_to_lst(filename, delim):

    txt_lst = list()

    with open(filename, 'r', encoding='utf-8', newline='') as fin:
        
        txt_it = csv.reader(fin, delimiter=delim)
        for string in txt_it:
            txt_lst.append(string)

    return txt_lst


def lst_to_tex(lst):

    col_n = 0
    body = ''

    for line in lst:

        line_len = len(line)
        col_n = line_len if line_len > col_n else col_n

    for line in lst:

        for idx, word in enumerate(line, 1):
            body += '$' + str(word) + '$' + (' & ' if idx != col_n else '')

        body += '&' * (col_n - len(line) - 1) + '\\\\\n\\hline\n'

    columns = ' '.join('| c' for i in range(col_n)) + ' |'

    header = f'\\begin{{tabular}}{{{columns}}}\n' \
             f'\\hline\n'
    footer = '\\end{tabular}\n'

    return header + body + footer


def main():
    parser = argparse.ArgumentParser(description='Hi! This is csv_to_tex v 1.0. Transforms csv table to LaTeX code.\
                                                  (c) Tako-San && derzhavin3016')
    parser.add_argument('in_f', metavar='INPUT', type=str, help='input file in csv format')
    parser.add_argument('out_f', metavar='OUTPUT', type=str, help='output file in tex format')

    parser.add_argument('-d', '--delim', type=str, default=',', help='parsing delimeter')

    args = parser.parse_args()
 
    lst = csv_to_lst(args.in_f, args.delim)
    tex = lst_to_tex(lst)

    with open(args.out_f, 'w', encoding='utf-8') as fout:
        fout.write(tex)


if __name__ == '__main__':
    main()
