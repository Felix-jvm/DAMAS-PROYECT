import tkinter
import os

'''
GRAPHIC USER INTERFACE
'''
##CREATES THE WINDOW
window=tkinter.Frame(width=800,height=480)
window.pack()

##CREATES THE ORIGINLABEL
originlabel=tkinter.Label(text='ORIGIN')
originlabel.pack()
originlabel.place(x=290,y=50)

##CREATES THE DESTINATIONLABEL
destinationlabel=tkinter.Label(text='TOWHERE')
destinationlabel.pack()
destinationlabel.place(x=270,y=80)

##CREATES THE ORIGININPUT
origininput=tkinter.Entry()
origininput.pack()
origininput.place(x=340,y=50)

##CREATES THE DESTINATIONINPUT
destinationinput=tkinter.Entry()
destinationinput.pack()
destinationinput.place(x=340,y=80)

##CREATES THE CHECK BUTTON
checkbuton=tkinter.Button(text='CHECK',command=lambda:check(origininput.get(),destinationinput.get()))
checkbuton.pack()

checkbuton.place(x=340,y=110)
##CREATES THE CLEAN METHOD

'''
LOGIC
'''
data=[   
[['-'],[''],['-'],[''],['-'],[''],['-'],['']],

[[''],['-'],[''],['-'],[''],['-'],[''],['-']],

[['-'],[''],['-'],[''],['-'],[''],['-'],['']],

[['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-']],

[['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-']],

[[''],['-'],[''],['-'],[''],['-'],[''],['-']],

[['-'],[''],['-'],[''],['-'],[''],['-'],['']],

[[''],['-'],[''],['-'],[''],['-'],[''],['-']]
]
 
viewer=[   
[['-'],[''],['-'],[''],['-'],[''],['-'],['']],

[[''],['-'],[''],['-'],[''],['-'],[''],['-']],

[['-'],[''],['-'],[''],['-'],[''],['-'],['']],

[[' '],[' '],[' '],[''],[''],[''],[''],['']],

[[' '],[' '],[' '],[''],[''],[''],[''],['']],

[[''],['-'],[''],['-'],[''],['-'],[''],['-']],

[['-'],[''],['-'],[''],['-'],[''],['-'],['']],

[[''],['-'],[''],['-'],[''],['-'],[''],['-']]
]

##### THE CHECK METHOD #####

def check(origin,towards):
 
 
  if len(origin)==2 and int(origin[0])>=0 and int(origin[0])<=len(data)-1 and int(origin[1])>=0  and int(origin[1]) <=len(data[0])-1: 
   
   if len(towards)==2 and int(towards[0])>=0 and int(towards[0])<=len(data)-1 and int(towards[1])>=0 and int(towards [1])<=len(data[0])-1:
    
     if len(data[int(origin[0])][int(origin[1])])>1:
      
      if data[int(origin[0])][int(origin[1])] [1].image=='♛':
 
       data[int(origin[0])][int(origin[1])] [1].movequeen(origin,towards)
      
      elif data[int(origin[0])][int(origin[1])] [1].image=='♕':
       
       data[int(origin[0])][int(origin[1])] [1].movequeen(origin,towards)
      
      elif data[int(origin[0])][int(origin[1])] [1].image=='☻':
 
       #data[int(origin[0])][int(origin[1])] [1].move(origin,towards,1,1,7,'♛','white') 
       data[int(origin[0])][int(origin[1])] [1].move(origin,towards,7,'♛','white') 
      else:
       data[int(origin[0])][int(origin[1])] [1].move(origin,towards,0,'♕','black') 
       #data[int(origin[0])][int(origin[1])] [1].move(origin,towards,-1,1,0,'♕','black')
 
     else:
      print('THE ORIGIN IS CURRENTLY EMPTY')
   else:
    print('THERE IS SOMETHING WRONG WITH THE TOWARDS NUMBER') 
         
  else:
   print('THERE IS SOMETHING WRONG WITH THE ORIGIN NUMBER')



##### COORDENATES OF WHERE THE INSTANCES OF PAWNS MUST BE ON THE DATA LIST#####

firstindices=[
         [0,     0, 2, 4, 6],
         [1,     1, 3, 5, 7],
         [2,     0, 2, 4, 6],
] 

secondindices=[
          [5,     1,3,5,7],
          [6,     0,2,4,6],
          [7,     1,3,5,7],             
]

insections=[]



##### THE DISPLAY THE PIECES FUNCTION #####

def displaythepieces(clas,name,number,send,receive,start,end):
 
 counter=0

 for a in range(number):
  receive.append(clas(name+str(a))) 
 
 for l in range(len(send)): 

  for i in range(len(send[l])):
  
   if i>0:
    data[send[l][0]] [send[[l][0]][i]].append (receive[counter])
    
    data[send[l][0]] [send[[l][0]][i]].append (receive[counter].image)
    
    data[send[l][0]] [send[[l][0]][i]] [1] .location=[str(send[l][0]),str(send[[l][0]] [i] )]
   
    counter+=1
                          
 update(start,end,-1,-1)



displaythepieces(white,'white',12,firstindices,insections,0,2)

insections=[] 

displaythepieces(black,'black',12,secondindices,insections,5,7) 