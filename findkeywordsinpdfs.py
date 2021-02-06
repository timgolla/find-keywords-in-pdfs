#!/usr/bin/env python
# @author Tim Golla <tim.golla.official@gmail.com>

import glob
import os
import re
from PyPDF4 import PdfFileReader
import argparse

parser = argparse.ArgumentParser(description="Find keywords in pdfs version\nAuthor: Tim Golla <tim.golla.official@gmail.com>\nNo warranty whatsoever.")
parser.add_argument("keywordfile",help="File that contains the keywords to search for, one word per line.")
parser.add_argument("pdffolder",help="Folder that contains the pdfs.")
parser.add_argument("-i","--ignorecase",  action="store_true",help="Ignore case of keywords.")
args = parser.parse_args()
keywordfilename = args.keywordfile
inputfolder = args.pdffolder
infiles = glob.glob(os.path.join(inputfolder, "*.pdf"))
outstring = ""
kwfile = open(keywordfilename,"r")
keywordtext = kwfile.read()
keywords = keywordtext.split("\n")
keywords.remove("")
for fn in infiles:
    keywordsfound = []
    f = open(fn,'rb')
    bn = os.path.basename(fn)
    pdf = PdfFileReader(f)
    npages = pdf.getNumPages()
    pagetexts = []
    for pnr in range(npages):
        page = pdf.getPage(pnr)
        textcurrent = page.extractText()
        pagetexts.append(textcurrent)
    text = "\n".join(pagetexts)
    for kw in keywords:
        searchstring = r'\b'+ kw.strip() +r'\b'
        if args.ignorecase:
            matchobject = re.search(searchstring,text, re.IGNORECASE)
        else:
            matchobject = re.search(searchstring,text)
        if matchobject:
            if kw not in keywordsfound:
                keywordsfound.append(kw)
    outstring += bn + "," + ",".join(keywordsfound) +"\n"
outfilename = os.path.join(inputfolder, "keywordsinpdfs.csv")
f = open(outfilename,"w")
f.write(outstring)
f.close()
print("Output written to: " + outfilename)