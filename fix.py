#!/usr/bin/python

import os
import sys
import math
import numpy as np
import linecache 

print 'hello python'
  
def splitbycomma(line):
      nodes=[]
      splitLine=line.split(',',1)
      el_num = splitLine[0]
      remainder=splitLine[1]
      for i in range(1,4):
	    node = str(remainder).split(',',1)
            remainder=node[1]
            nodes.append(node[0])
            if i==3:
		  test=node[1].split('\n', 1)   
		  string=test[0]

                  nodes.append(string)  

      return el_num,nodes

def dump_header ():
      f.seek(0)
      g.seek(0)

      for line in f:
            g.write(line)
            if '*ELEMENT, TYPE=C3D4, ELSET=EB1' in  line:
                break  

def dump_footer ():
      flag = 0
      for line in f:
            if '**' in  line:
                  flag = 1
            if flag == 1:
                  g.write(line)
 

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
     if '*ELEMENT' in line:  
          flag=1
     if '**\n' in line:
          val=0

     if ( flag == 1):
	if '*ELEMENT' not in line: 
          firstLine=line.split(',',1)
          firstElNum=int(firstLine[0])
          list_firstEl.append(firstElNum)
	  firstEl=list_firstEl[-1]
	  val=1
          flag=0
                  
     if  ( val == 1 and flag == 0 ):
	(el_num,nodes)=splitbycomma(line)
	list_element.append(el_num)
	list_node.append(nodes)
       	


     if (val == 0):
          writeLine=line    
 #         g.write(writeLine)
# j is elset counter
j=0
list_firstEl.append(len(list_firstEl)+1) 

new_element=[]
new_line=[]

dump_header()

for l in range(0,len(list_element)):
#      print list_element[l],int(list_element[l])-int(list_firstEl[j])+1
      if int(list_element[l]) == int(list_firstEl[j+1]):
         j=j+1
	 g.write('*ELEMENT, TYPE=C3D4, ELSET=EB'+str( j+1)+'\n')
#	 writeLine='*ELSET=EB', j+1
      fixedElNum=(int(list_element[l])-int(list_firstEl[j])+1)
      new_element.append(fixedElNum)
#      for i in range(0,3):
#            nodes=str(splitbycomma(l))
#      fixedLine=str(new_element[l])+ str(list_node[l])
      node1=str(list_node[l]).split(',')[0].strip("['']")
      node2=str(list_node[l]).split(',')[1].strip("'  ")
      node3=str(list_node[l]).split(',')[2].strip("'  ")
      node4=str(list_node[l]).split(',')[3].strip("'  ']")
      fixedLine=str(new_element[l])+','+ node1 +',    '+ node2+',    '+ node3+',    '+ node4
      new_line.append(fixedLine)
      writeLine=new_line[-1]
#      writeLine=writeLine.replace('[', '').replace(']', '')
      #      print str(new_element[l]),(list_node[l])
#      print writeLine
      print fixedLine
      g.write(writeLine + '\n')
     
     
"""
      fixedLine=str(new_element[l])+ (list_node[l])
      new_line.append(fixedLine)
      writeLine=(new_line[l])
#      print writeLine
      
#      print writeLine
 #     print newLine 
 #     print list_element[l],int(list_element[l])-int(list_firstEl[j])+1

"""
dump_footer()

f.close()
g.close()
exit()



""""
      print j,list_element[l],int(list_element[l])-int(list_firstEl[j])+1
      if int(list_element[l]) == int(list_firstEl[j+1]):
#	   print list_element[l],list_firstEl[j]
#           print j
           if (j < len(list_firstEl)-1 ):
	        j=j+1
"""


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
#     print list_element[l], new_element[l], list_firstEl[j-1], j #,list_node[l]
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
#     print list_element[l], new_element[l], list_firstEl[j] #,list_node[l]
#     g.write(str(new_element))	

#print list_element[-1] #,list_node
#print list_element[-1],list_node[-1]


f.close()
g.close()


 
