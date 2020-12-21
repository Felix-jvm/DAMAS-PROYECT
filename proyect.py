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

##### THE UPDATE FUNCTION #####

def update(start,end,origin,towards):                                        
 
 os.system('clear')

 for c in range(len(data)):

  for e in data[c]:                 
   
   if start>-1 and end>-1: 
    
    if c>=start and c<=end and len(e)>1:
      viewer[int(e[1].location[0])][int(e[1].location[1])]=[e[1].image]

   elif len(e)>1:
    
    viewer[int(e[1].location[0])][int(e[1].location[1])]=[e[1].image]
    
    
   if origin!=-1:
    if len(data[int(origin[0])][int(origin[1])])<=1: 
     viewer[int(origin[0])][int(origin[1])]=[''] 
    
  if towards!=-1 and len(data[int(towards[0])][int(towards[1])])<=1:
   
   viewer[int(towards[0])][int(towards[1])]=[''] 

  print(viewer[c])

shift='white'
upside='black'
status=['white','black']
c=0


##### THE WHITE CLASS #####

class white(object):

 def __init__(self,name):
  self.name=name
  self.image='☻' 
  self.location=[]

 ##### THE CALL THE QUEEN METHOD ####  

 def callthequeen(self,vindex,friendclas,queenimage,origin,towards):
    
  data[int(self.location[0])][int(self.location[1])] [1]=queen(friendclas,queenimage)

  data[int(self.location[0])][int(self.location[1])] [1].location=self.location

  update(-1,-1,origin,towards)

 ##### THE MOVE METHOD #####

 def move(self,origin,towards,become,queenimage,friendclas):

  global status
  global shift
  global upside

  if 'black' in self.name:

   ##IF THE PIECE ON THE ORIGIN INDEX IS A BLACK INSTANCE THEN THIS BLOCK OF CODE IS EXECUTED   
    if int(origin[0])-int(towards[0])==1:
     
      if int(towards[1])-int(origin[1])==1 or int(towards[1])-int(origin[1])==-1:
  
        if len(data[int(towards[0])][int(towards[1])])>1:
  
            if data[int(towards[0])][int(towards[1])] [1].image==self.image:  
             
              print('IT IS FROM THE SAME TEAM')
           
            else:

              if int(towards[0])-1>=0 and int(towards[0])-1<=len(data)-1 and int(towards[1])+(int(towards[1])-int(origin[1]))>=0 and int(towards[1])+(int(towards[1])-int(origin[1]))<=len(data[0])-1 and len(data[int(towards[0])
              -1][int(towards[1])+(int(towards[1])-int(origin[1]))])<=1:

                if shift in self.name:  
                
                    data[int(towards[0])-1][int(towards[1])+(int(towards[1])-int(origin[1]))]=data[int(origin   [0])]  [int(origin[1])] 
     
                    data[int(towards[0])-1][int(towards[1])+(int(towards[1])-int(origin[1]))] [1].location=[int   (towards[0])-1,int(towards[1])+(int(towards[1])-int(origin[1]))] 
                    
                    data[int(origin[0])][int(origin[1])]=['']
     
                    data[int(towards[0])][int(towards[1])]=['']
   
                    if self.location==become:
   
                     self.callthequeen(0,'black',queenimage,origin,towards) 
                  
                    update(-1,-1,origin,towards) 
                    
                    if shift==status[0]:
                     shift=status[1]
                     upside=status[0]
                    else:
                     shift=status[0]
                     upside=status[1]  

                else:
                  print('IS NOT TURN OF THE '+upside.upper()+' TEAM YET') 
                

              else:
               print('THE CATCH CANNOT BE ACOMPLISHED') 

        else:
         
         if shift in self.name:

           data[int(towards[0])][int(towards[1])]=data[int(origin[0])][int(origin[1])]
           
           data[int(towards[0])][int(towards[1])] [1].location=[towards[0],towards[1]]
           
           data[int(origin[0])][int(origin[1])]=['']
   
           if self.location==become:
   
            self.callthequeen(0,'black',queenimage,origin,-1) 
           
           update(-1,-1,origin,-1)

           if shift==status[0]:
             shift=status[1]
             upside=status[0]
           else:
             shift=status[0]
             upside=status[1]

         else:
          print('IS NOT TURN OF THE '+upside.upper()+' TEAM YET') 


      else:
       print('THE MOVEMENT CANNOT BE ACOMPLISEHD')
    
    else:
     print('THE MOVEMENT CANNOT BE ACOMPLISHED') 



  elif 'white' in self.name:
  
 ##IF THE PIECE ON THE ORIGIN INDEX IS A WHITE INSTANCE THEN THIS BLOCK OF CODE IS EXECUTED 
   if int(origin[0])-int(towards[0])==-1:
    
     if int(towards[1])-int(origin[1])==1 or int(towards[1])-int(origin[1])==-1: 
        
        if len(data[int(towards[0])][int(towards[1])])>1:

          if data[int(towards[0])][int(towards[1])] [1].image==self.image:

            print('IT IS FROM THE SAME TEAM')
          
          else:

            if int(towards[0])+1>=0 and int(towards[0])+1<=len(data)-1 and int(towards[1])+(int(towards[1])-int(origin[1]))>=0 and int(towards[1])+(int(towards[1])-int(origin[1]))<=len(data[0])-1 and len(data[int(towards[0])+1][int(towards[1])+(int(towards[1])-int(origin[1]))])<=1:

              if shift in self.name:

                 data[int(towards[0])+1][int(towards[1])+(int(towards[1])-int(origin[1]))]=data[int(origin[0] )][int(origin[1])]  
 
                 data[int(towards[0])+1][int(towards[1])+(int(towards[1])-int(origin[1]))] [1].location=[int (towards[0])+1,int(towards[1])+(int(towards[1])-int(origin[1]))]
 
                 data[int(origin[0])][int(origin[1])]=['']
                 
                 data[int(towards[0])][int(towards[1])]=['']
                  
                 if self.location==become:
                   
                   self.callthequeen(7,'white',queenimage,origin,towards)
                 
                 update(-1,-1,origin,towards)
                 
                 if shift==status[0]:
                   shift=status[1]
                   upside=status[0]
                 else:
                   shift=status[0]
                   upside=status[1]
                
              else:
               print('IS NOT TURN OF THE '+upside.upper()+' TEAM YET')
               
            else:
               print('THE CATCH CANNOT BE ACOMPLISHED')   

        else:
       
         if shift in self.name:

           data[int(towards[0])][int(towards[1])]=data[int(origin[0])][int(origin[1])]
           
           data[int(towards[0])][int(towards[1])] [1].location=[towards[0],towards[1]]
           
           data[int(origin[0])][int(origin[1])]=[''] 
 
           if self.location==become:
  
            self.callthequeen(7,'white',queenimage,origin,-1) 
          
           update(-1,-1,origin,-1) 

           if shift==status[0]:
             shift=status[1]
             upside=status[0]
           else:
             shift=status[0]
             upside=status[1]

         else:
          print('IS NOT TURN OF THE '+upside.upper()+' TEAM YET') 

     else:
       print('THE MOVEMENT CANNOT BE ACOMPLISEHD')           

   else:
       print('THE MOVEMENT CANNOT BE ACOMPLISHED')
  

###### THE BLACK CLASS ######

class black(white):
 
 def __init__(self,name):
  self.name=name
  self.image='☺'
  self.location=[]


##### THE QUEEN CLASS #####

class queen(object):

 def __init__(self,friendclas,queenimage):
   self.name=friendclas
   self.image=queenimage
   self.location=[]
   self.indices=[[],[]]
   self.steps=[]
   #self.registry=[]
   self.lastindex=[]

 #### THE CHECK POSITION METHOD####

 def checkposition(self,v,h,origin,towhere):   
  lou=0000
  
  global c
  global status
  global shift
  global upside 
  next=[]

  if len(self.lastindex)<1:
   self.lastindex=[int(origin[0]),int(origin[1])] 

  #IF THE CURRENT LOCATION ISNT EMPTY THEN IT CHECKS IF THE INSTANCE ON THE CURRENT LOCATION IS A FRIEND INSTANCE OR A RIVAL ONE
  if len(data[v][h])>1:
   if self.name in data[v][h] [1].name:
    
    return 'THERE IS A PIECE FROM THE SAME TEAM ON THE TOWARDS PLACE'
   else:
    #CHECKS IF THE FORWARD INSTANCE CAN BE EATEN 
    next=[self.indices[0][0],self.indices[1][0]]
    
    if v+next[0]<=len(data)-1 and h+next[1]<=len(data[0])-1 and len(data[v+next[0]][h+next[1]])<=1:
      
      if shift in self.name:

        data[v+next[0]][h+next[1]]=data[self.lastindex[0]][self.lastindex[1]]
     
        data[v+next[0]][h+next[1]] [1].location=[v+next[0],h+next[1]]
         
        data[self.lastindex[0]][self.lastindex[1]]=['']
     
        #data[int(towhere[0])][int(towhere[1])]=['']
        
        data[v][h]=['']
 
        update(-1,-1,self.lastindex,[v,h])
        
        if shift==status[0]:
          shift=status[1]
          upside=status[0]
        else:
          shift=status[0]
          upside=status[1] 
      
      else:
        print('IS NOT TURN OF THE '+upside.upper()+' TEAM YET') 

    else:
    
     return 'THE CATCH CANNOT BE ACOMPLISHED' 

  else:
   
   if shift in self.name:
   
    data[v][h]=data[self.lastindex[0]][self.lastindex[1]]
    data[v][h] [1].location=[v,h]
    data[int(self.lastindex[0])][int(self.lastindex[1])]=['']
    update(-1,-1,self.lastindex,-1) 
    
    if shift==status[0]:
      shift=status[1]
      upside=status[0]
    else:
      shift=status[0]
      upside=status[1]

   else:
    print('IS NOT TURN OF THE '+upside.upper()+' TEAM YET')

  self.lastindex=[v,h]  



 ##### THE MOVEQUEEN METHOD #####

 def movequeen(self,origin,towhere):

   output=None
 
   self.indices=[[],[]]
 
   self.steps=[int(towhere[0])-int(origin[0]),int(towhere[1])-int(origin[1])]
   
   if int(self.steps[0])>0:
    for a in range(1,self.steps[0]+1,1):
     self.indices[0].append(a)
   else:
    for e in range(-1,self.steps[0]-1,-1):
     self.indices[0].append(e)  
 
   if int(self.steps[1])>0:
    for a in range(1,self.steps[1]+1,1):
     self.indices[1].append(a)
   else:
    for e in range(-1,self.steps[1]-1,-1):
     self.indices[1].append(e)
     
   
   if len(self.indices[0])==len(self.indices[1]):
     for u in range(len(self.indices[0])):
      
      output=self.checkposition(int(origin[0])+self.indices[0][u],int(origin[1])+self.indices[1][u],origin,towhere) 
      
      if output!=None:
       print(output)
       output=None
       return
       
   else:
     print('THE MOVEMENT YOU WANNA DO ISNT ALLOWED')



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