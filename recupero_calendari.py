#!/usr/bin/python
import fileinput
import urllib2
from lettoreFile import GestoreCollezioneFile

page1 = urllib2.urlopen('http://www.unive.it/data/46/1')
page2 = urllib2.urlopen('http://www.unive.it/data/46/2')
page3 = urllib2.urlopen('http://www.unive.it/data/46/3')
output1 = open('output1.txt', 'w')
output2 = open('output2.txt', 'w')
output3 = open('output3.txt', 'w')

for line in page1:
    output1.write(line)

for line in page2:
    output2.write(line)

for line in page3:
    output3.write(line)

output1.close()
output2.close()
output3.close()

lista=('output1.txt','output2.txt','output3.txt')

Variabile=GestoreCollezioneFile(lista)
Variabile.printer()