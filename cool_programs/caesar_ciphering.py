# -*- coding: utf-8 -*-
import numpy as np
import sys

Sentence = sys.argv[1]

Big_numbers = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',\
              11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',\
              20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z'}
small_numnbers={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',\
               11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',\
               20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
Big_alphabet = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,\
                'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,\
                'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
small_alphabet ={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,\
                 'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,\
                 't':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}

example = 'hello world again'
listofwords = example.split()
print ','.join(listofwords[0])

for i in range(2):
    pass
