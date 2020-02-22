# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 10:37:28 2020

@author: MOHANA D
"""

print("hello world") 
if 8>10: #use":" after if and else
 print("8 is bigger than 10")
else:
 print("10 is bigger than 8") 
 x=1 #x is int
 y="mohana" #y is str
 z=2j #z is complex
 a=0.2 #a is float
 print(x)
 print(y)
 print(z)
 print(a)
 x,y,z=("hi","hello","bye")
 print(x,y,z)
 x=y=z="dasari"
 print(x,y)
 print(z)
 x="ciao " #use space after word1 or before word2 to give space between two words
 y=" ragazzi"
 print(x + y)
 x=7
 y=3.4
 z=x+y
 print(z)
 
x="i am"
def myfunc(): #myfunc() is constant and is used as function
     print(x+" awesome")
myfunc() #this is used to read the given function

y=2 #here y is global variable
def myfunc():
    y=5 #here y is local variable and can be used only in function
    print(y+3)
myfunc() #this is used to run the respective function
print(y+9)    
x="i am"
def myfunc():
    global x #global keyword is uesd to change global function inside function
    x="you are"
    print(x+" dasari")
myfunc()    
print(x+"mohan")

x=3
def myfunc():
    global x #global keyword is uesd to change global function inside function
    x=2
    print(x+1)
myfunc()    
print(x+2)

x=range(3)
print(type(x))

x={"name":"John", "age":36} #for dict use flower brackets and use":"
type(x)
x = 5j+3
type(x)
import random

print(random.randrange(1,10000000))

a = "Hello, World!"
print(a[1])

b="dasari"
print(b[-5:-2])

a="dasari"
b=" mohana"
c=a+" "+b
print(c)

age=22
x="my age is {}" #use format() to combine the string and numbers by using {}
print(x.format(age))

onions = 3 #The format() method takes unlimited number of arguments, and are placed into the respective placeholders
price = 5
myorder = "I bought {} onions for {} rupees each."
print(myorder.format(onions,price))

txt = "We are the so-called \"Vikings\" from the north."
txt = "This will insert two \\\\\(backslash)."
print(txt) 

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

def myfunc() : #functions that returns a Boolean Value and myfunc() or myfunction()
  return True

print(myfunc())

#execute code based on the Boolean answer of a function
def myfunc():
    return True #use True not true
if myfunc():
    print("yes")
else:
    print("no")
    
#the isinstance() function, which can be used to determine if an object is of a certain data type 
x = 200
print(isinstance(x, float)) 
y="mohana"
print(isinstance(y,str))

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
  
x={
   "fruit":"mango", #use commas
   "quantity": "2kg",
   "price":100 #no need of commas in last line
   }
print(x)

#to get specific iteam we use
y=x["quantity"]
z=x.get("fruit")
#to change any value in dictionary
x["price"]= 150 
print(x)

x={
   "fruit":"mango", #use commas
   "quantity": "2kg",
   "price":100 #no need of commas in last line
   }
for y in x: #the for loop is used to return the values of only keys of the dictionry
    print(y)
for y in x.keys(): #we can also use this to reututn the keys values
    print (y)
    
x={
   "fruit":"mango", #use commas
   "quantity": "2kg",
   "price":100 #no need of commas in last line
   }
for z in x: 
    print(x[z])    #for loop is used to return the values of the dictionaries use z in square brackets of x or dictionary
for z in x.values(): #we can also use this method to return values
    print(z)
    
#to get both keys and values we use items() fuction
for y,z in x.items():
    print(y,z)
#to remove any item in dictionary use pop() fuction     
x={
   "fruit":"mango", 
   "quantity": "2kg",
   "price":100 
   }
x.pop("quantity") #always use keyword
print(x)
#we can use pop.item() function  to remove last item in the dictionary
x={
   "fruit":"mango", 
   "quantity": "2kg",
   "price":100 
   }
x.popitem()
print(x)
#The del keyword removes the item with the specified key name
x={
   "fruit":"mango", 
   "quantity": "2kg",
   "price":100 
   }
del x["quantity"] #don't use ":" in del 
print(x)
#The clear() keyword empties the dictionary
x={
   "fruit":"mango", 
   "quantity": "2kg",
   "price":100 
   }
x.clear()
print(x)

import datetime
x=datetime.datetime.now()
print("current date and time:",x)

print("Twinkle, twinkle, little star,\nHow I wonder what you are! \tUp above the world so high, \nLike a diamond in the sky. \nTwinkle, twinkle, little star, \nHow I wonder what you are!")
print(‘hello’ + ‘-‘ + ‘how’ + ‘-‘ + ‘are’ + ‘you’)
