#!/usr/bin/python   

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
    
for line in reader:
    if len(line) == 19:
        nid, user_id, ntype, abspid = [line[0], line[3], line[5], line[7]]
        if ntype == 'node_type': 
            continue

        if abspid == '\N':
            print "{0}\t{1}".format(nid, user_id)
        else:
            print "{0}\t{1}".format(abspid, user_id)
            
