#! /usr/bin/env python3

"A module for searching a plain-text version of Charles Darwin's Origin of Species for the words inheritance, heritability, inherit, etc."

import sys
import re

def search_heritability(infile, outfile):
    """
    Searches an input file for words containing the string "herit" (e.g., heritability, inheritance, inherited).
    Writes the line number on which a match was found, followed by a tab, followed by the word that was matched to a new output file.
    
    Parameters
    ----------
    infile : str
        The name of the file which will be searched, in quotes.
    
    outfile: str
        The name of the file to which output will be written, in quotes.

    Returns
    -------
    None
        Will write output to a file.

    """
    pattern = r'[a-zA-Z]*herit[A-Za-z]*'
    regex_pattern = re.compile(pattern, re.I)
    with open(infile, 'r') as in_stream:
        with open(outfile, 'w') as out_stream:
            line_number = 0    
            for line in in_stream:
                line = line.strip()
                line_number += 1
                match = regex_pattern.search(line)
                if match:
                    out_stream.write(str(line_number)+"\t"+match.group(0)+"\n")
    return None

if __name__ == '__main__':
    if len(sys.argv) != 3: 
        sys.exit("Error! Expecting two command line arguments -- an input file and an output file.")
    
    search_heritability(sys.argv[1], sys.argv[2])
