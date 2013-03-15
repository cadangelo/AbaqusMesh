#!/usr/bin/python

#import numpy

# print to screen
print 'hello python'

import os
import sys
import math
import numpy as np

def changeLine(line,firstnum):
  splitLine=line.split(',')
  origElNum=int(splitLine[0])
  newElNum=origElNum - firstnum + 1
#  editedLine=splitLine
#  return editedLine
  return newElNum

#def getfirstvalue(splitLine):
#  firstvalue=splitLine
  

# open a mesh file
f = open('sr_mesh220.inp','r')
# open edited file
g = open('fixed.inp', 'w')

flag=0
val=0

for line in f:
     if '*ELEMENT' in line:  #If *ELEMENT is in the line, flag=1 signaling you are 
         flag=1              # in element data section now
     if '**\n':              #When the end of the element data is reached (**\n)
         val=0               # val=0 which signals print lines as they are, do not edit
         
     if  flag==1:
         flag=0              #Reset flag to 0
         val=1               #Will go to changeLine function
	
     if (flag == 0 & val == 0):
         firstnum=int(line.split(',')[0])       #Gets first element number in part

     if  val==0:
         finishedLine=line
     else:
         print line
         finishedLine=changeLine(line, firstnum)
     
     g.write(str(finishedLine))


f.close()
g.close()


 
