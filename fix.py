#!/usr/bin/python

import os
import sys
import math
import numpy as np
import linecache 

print 'hello python'
  
def splitbycomma(line):
      nodes=[]
      firstline=line.split(',',1)
      el_num = firstline[0]
      remainder=firstline[1]
      for i in range(1,4):
	    node = str(remainder).split(',',1)
            remainder=node[1]
            nodes.append(node[0])
            if i==3:
                  nodes.append(node[1])     
      return el_num,nodes


# open a mesh file
f = open('sr_mesh220.inp','r')
# open edited file
g = open('fixed.inp', 'w')

flag=0
val=0 
i=0

list_element=[]
list_node=[]
list_firstEl=[]

for line in f:
#     i=i+1
     if '*ELEMENT' in line:  #If *ELEMENT is in the line, 
          flag=1
     if '**\n' in line:
          val=0

     if ( flag == 1):
	if '*ELEMENT' not in line: 
	  splitLine=line.split(',',1)
          firstElNum=int(splitLine[0])
	  list_firstEl.append(firstElNum)
	  firstEl=list_firstEl[-1]
	  flag=0
	  val=1

     if  ( val == 1 and flag == 0 ):
	(el_num,nodes)=splitbycomma(line)
	list_element.append(el_num)
	list_node.append(nodes)
#	print list_element[-1]
#	print list_firstEl[0]

#	print newEl
#	list_newEl.append(newEl, geldof)
#	firstElNum=getFirstEl(line)
#	list_firstEl.append(firstElNum)
#	StartEl=list_firstEl[-1]

# j is elset counter
j=0

list_firstEl.append(len(list_firstEl)+1)

new_element=[]

print list_firstEl

for l in range(0,len(list_element)):
#      print list_element[l],int(list_element[l])-int(list_firstEl[j])+1
      if int(list_element[l]) == int(list_firstEl[j+1]):
         j=j+1
      print list_element[l],int(list_element[l])-int(list_firstEl[j])+1


""""
      print j,list_element[l],int(list_element[l])-int(list_firstEl[j])+1
      if int(list_element[l]) == int(list_firstEl[j+1]):
#	   print list_element[l],list_firstEl[j]
#           print j
           if (j < len(list_firstEl)-1 ):
	        j=j+1

"""
exit()

# loop over the members of list_element
for l in range(0,len(list_element)):
# if the current element is equal to where a new element begins
     if int(list_element[l]) == int(list_firstEl[j]):
	# if we are not on the final elset increment j
	if j <= (len(list_firstEl)-1):
	    j=j+1
	# otherwise do nothing
        else:
            j=j
     # new value is the original value - start value + 1
     newEl=(int(list_element[l])-int(list_firstEl[j-1]) + 1)
#     print int(list_firstEl[j])
     new_element.append(newEl)
     print list_element[l], new_element[l], list_firstEl[j-1], j #,list_node[l]
#g.write(str(new_element[l]))	    


# loop over the members of list_element
for l in range(0,len(list_element)):
# if the current element is equal to where a new element begins
     if int(list_element[l]) == int(list_firstEl[j]):
	# if we are not on the final elset increment j
	if j < (len(list_firstEl)-1):
	    j=j+1
	    print "*ELSET=EB1"
	# otherwise do nothing
        else:
            j=j
	    print "*ELSET=EB4"
     # new value is the original value - start value + 1
     print list_element[l], new_element[l], list_firstEl[j] #,list_node[l]
     g.write(str(new_element))	

#print list_element[-1] #,list_node
#print list_element[-1],list_node[-1]


f.close()
g.close()


 
