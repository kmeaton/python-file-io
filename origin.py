#! /usr/bin/env python3

"A module for searching a plain-text version of Charles Darwin's Origin of Species for the words inheritance, heritability, inherit, etc."

import sys
import re

pattern = r'[a-zA-Z]*herit[A-Za-z]*'

regex_pattern = re.compile(pattern, re.I)

with open('origin.txt', 'r') as in_stream:
    with open('heritability.txt', 'w') as out_stream:
        line_number = 0    
        for line in in_stream:
            line = line.strip()
            line_number += 1
            match = regex_pattern.search(line)
            if match:
                out_stream.write(str(line_number)+"\t"+match.group(0)+"\n")


