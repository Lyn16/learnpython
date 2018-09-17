#!/usr/bin/env python
import json
import re
import fileinput

for line in fileinput.input(['/home/jiawen/data/Homo_sapiens.GRCh37.75.gtf']):
    gene_name_matches = re.findall('gene_name \"(.*?)\";',line)
    chromosome_matches  = re.findall('^\d',line)
    startPos_matches = re.findall('gene.(\d*)\W\S',line)	
    endPos_matches = re.findall('\sgene.\d*\s(\d*).',line)
    if gene_name_matches:
       if chromosome_matches:
          if startPos_matches:
	     if endPos_matches:
	       print(json.dumps({'geneNames':gene_name_matches[0], 'chr':chromosome_matches[0], 'startPos':startPos_matches[0],'endPos':endPos_matches[0]}, sort_keys=False, indent=4))             
