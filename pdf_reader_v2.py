# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 22:15:54 2018

@author: Ferhat
"""

import PyPDF2
import re

pdf_file = open('annual_report_and_accounts.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
#read_pdf.getPage(18)
pdf_text = ""
for x in range(0, read_pdf.getNumPages()):
    #pdf_text = ""
    pdf_text = pdf_text + read_pdf.getPage(x).extractText()
    #print (pdf_text)

red = len(re.findall("challenging", pdf_text)) + len(re.findall("difficult", pdf_text)) + len(re.findall("down by", pdf_text)) +\
    len(re.findall("unpredictable", pdf_text)) + len(re.findall("lower", pdf_text)) + len(re.findall("poor", pdf_text)) +\
    len(re.findall("difficult trading", pdf_text)) + len(re.findall("tough", pdf_text)) + len(re.findall("below expectations", pdf_text)) +\
    len(re.findall("deficit", pdf_text))

yellow = len(re.findall("in line with expectations", pdf_text)) + len(re.findall("cash", pdf_text))

green = len(re.findall("exceeding expectations", pdf_text)) + len(re.findall("positive", pdf_text)) + len(re.findall("favourable", pdf_text)) +\
        len(re.findall("profit up", pdf_text)) + len(re.findall("excellent", pdf_text)) + len(re.findall("transformational", pdf_text))

blue = len(re.findall("debt", pdf_text)) + len(re.findall("covenents", pdf_text)) + len(re.findall("borrowings", pdf_text))

print ("Red =", red)
print ("Yellow =", yellow)
print ("Green =", green)
print ("Blue =", blue)