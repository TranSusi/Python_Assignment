# Using Loop, 'for..in'

# Using Xrange to iterate over a sequence of numbers
for y in range(6):
    print(y) #Prints out 0,1,2,3,4
    
for y in range(4,7):
    print(y) #prints put (4,5,6)

    
for x in range(4,10,2):
    print(x) #prints out 4,6,8

count = 0
while count < 6:
    print(count)
    count = count + 1 

    # Using Loop, White loop for iteration

a = ['foo', 'bar', 'baz']
while a:
    print(a.pop(-1))

music = ['fun', 'sad', 'empty', 'boring', 'meaningful']
while music:
    print(music) # prints out every words on string 'music with the same order as this string

        #Using Pop() to pop up and return the value with given index from the list
   
    print(music.pop(-1)) #prints out string 'music' from the beginning of the list 'music', 1 mean, every element of the list 'music'


# Using 'BREAK', 'CONTINUE' in While Loop to terminate the loop sooner
n = 7
while n > 0:
    n -= 1    # the same as n=n-1
    if n == 2:
        break
    print(n)
print('Loop ended.')

n = 7
while n > 0:
    n -= 1    # the same as n=n-1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

#using ELSE/ ELIF
age = 1
gender = ['male', 'female']
if age < 18:
    if gender == 'male':
        print('litle boy')
    else:
        print('little girl')
elif age >= 18 and age < 70:
    if gender == 'male':
        print('Mr')
    else:
        print('Mrs')
else:
    if gender == 'male':
        print('grandpa')
    else:
        print('grandma')

# Using ELSE/ ELIF/ for..in/ range/ %
# Prints out 0,1,2,3,4,5, then prints out "number is 5", use 'while..else'

amount = 0
while(amount < 6):
    print(amount)
    amount +=1
else:
    print("amount is %d" % (amount))

#Exercise: prints out even numbers from alist (same order). Not print number> 200

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544
  
]
for i in numbers:
    if i == 200:
        break

    if i % 2 == 1:
        continue
    print(i)

#Using FUNCTIONS

#print outs  2 persons's names with their ages
def i(name, age):
    i('Susi', '20')
    i('Nini', '30')
    print('give gratitude to your friends' + 'Mr' + name + '.' 'Your age'+ age + 'just a number')

# Using Functions- Def, Return

#  Prints out strings:
# 'Passion is an element of a fulfilled life'
#' high-risk taste is an element of a fulfilled life'
# 'meaningful action is an element of a fullfilled life' 

def list_elements():                                            # create a funtion with def...(), return ...
    return "Passion", "self disciplined" , "meaningful action"

# Concatenate/join/connect the elements (passion,self-disciplined,etc)= (a)
# to 'is an element of a fulfilled life' (b)
# into full sentence/string (n)

def full (elements):
    return " %s is an element of a fulfilled life." % elements

def full_sentences():
    l_e = list_elements()       # Exercute function list_elements(). The program will run from line 109

    for elements in l_e:        # Loop to make sure 3 *elements* are joined to make 3 full sentences/ strings
        print(full (elements))
full_sentences()

def b():
    return ('hihi')

#Using CLASS, OBJECTS
#Create new data type is student with objects that defines *student* including name, major, gpa.
class Student:
    def _self_(person, name, major, gpa):
        person.name = name
        person.major = major
        person.gpa = gpa

from  Student import student
student1 = Student ('Susi', 'math', 3.5)
student2 = Student ('Jimmy', 'history', 3.7)
student3 = Student ('Alex', 'music', 3.9)
student1 = Student ()
print (student1.gpa)

#Using Class, then Def, then Return
#-------------------------------------------------------------------------------#
# Print outs:  Mercedes is a black convertible car worth $50000.00.
#              Volvo is a white van car worth $11000.00.
# define the Vehicle class

#------------------------------------------------------------
class transport: 
    name = ''
    color = ''
    kind = ''
    price = 1000.00

def trans_descript(self):
    trans_des ('%s is a %s %s  woth $%.2f.' % (self.name, self.color, self.kind, self.price) )
    return trans_des

car1 = transport()
car1.name = 'Mercedes'
car1.color = 'black'
car1.kind = 'convertible'
car1.price = 50000.00 

car2 = transport()
car2.name = 'Volvo'
car2.color = 'white'
car2.kind = 'van'
car2.price = 11000.00 

print(car1.trans_descript())
print(car2.trans_descript)

# Using Dictionany-> a= {.....}, For...in..

# Add Kate's number, Delete Kim's number and prits out these numbers

number_folder = {  
    "Kate" : 938477890,
    "Ken" : 938377359,
    "Kim" : 947662281
}  

# name of dictionay[] = ..... (if wanna add)
# using DELETE + name of dictinary [] (if wanna delete)
number_folder["Kate"] =  938477000,
del number_folder["Kim"]  

# Using If.. in/ If... to check value that is added or deleted. If..in-> print out 1 sentence, if..not in-> print another sentence
if "Kate" in number_folder:  
    print("Kate is listed in the number folder") 
    
if "Kim" not in number_folder:      
    print("Kim is not listed in the number folder") 
#--------------------------------------------------------------------------------------------

# Using Modules-> Import...
# Import a modules form other file

import draw

def playgame():
    name : ''
    author : ''
    kind : 'online'

def game_des():
    des = game_des()
    draw.draw_game (des)

# Use If to show that if this script is executed, then 
# game_des() will be executed
if __name__ == '__game_des__':
    game_des()

#---------------------------------------------------------------------------------
# Use NUMPY ARRAY
## Print out weights in lbs from the list of weights (88.35, 22.45, 37.90, 54.93, 49,28,34,19)

weight_kg = [22.45, 37.90, 54.93, 49.28, 34.19] # Create an array ...= [....], from a given list

import numpy as np              # Give *numpy* as a varriable *np*

npw_kg = np.array(weight_kg)  # Create a numpy array np_w_kg, from weight_kg

npw_lbs = npw_kg * 2.2         # Boolen Calculation: * -> Create np_weight_lbs from np_weight_k     

print(npw_lbs)   
#---------------------------------------------------------------------------------
#Using Pandas
#Use Import pandas as pd, read_csv function
#Access observations from DataFrame, use ( rows)

import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

print(cars[0:2])   # Print out first 2 observations
print(cars[5:7])    #Print out 6th and 7th observation        

#----------------------------------------------------------------
#Using Generator

# Print out 10 random integers:
import random       # Import a python external modules:'random'-> Use import random

def lottery():       # Definite *lottery* program from modules random-> Use def lottery()
    # returns 9 numbers between 1 and 50
    for n in range(9):               # Run sequently/ all number from 1-40-> use loop: for..in. Return 4 numbers-> use range(5)
        yield random.randint(1, 40)  # iterate,then extract the value and iterate upon, not release output-> use yield as a generator
                                     # yield ( name of module. function randint()). Randint: return intergers from randome module

    # returns a 10th number between 1 and 15
    yield random.randint(1,15)

for ran_number in lottery():
       print("the next number is... %d" %(ran_number))

#-------------------------------------------------------------------
#Using LIST COMPREHENSION

# Example 1: print out positive numbers from the list, as integers.

list_num = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]  # create a list as a string .... =[]
result = [int(n) for n in numbers if x > 0]              #1 Iterate, use for.n.in + name of the list
                                                         #2 Condition: positive numbers-> use 'if n > 0--> have a loop: for...in..If n>0
                                           #3  then, return to the intergers-> use functions: int(n)-> put this before loop
                                                        #4 put this function and condition into [] as a string. Then put a name 'result'
print(result)
#-------------------------------------------------------------------------------------------------------------------------

# Using Multiple Function Arguments

#Example: print out 6( it is sum (0,1,2,3))


def sum(start: int, **numbers): # use function: def sum(argument 1, **kwargument, argument 3,etc)
    for _, sum1 in numbers.items(): #Loop with for...in, module 'numbers' with item() method
        start += sum1
    return start

print(sum(start = 0, a = 1, b = 2, c = 3))
#---------------------------------------------------------------------------------
# Use Regular Expections (Regexp)

import re   #re modules for Rege
# Print out 'heart' if it is found in the below sentence
sentence = "The rainbow is in my heart"
result = re.search("heart", sentence) #use search method()
print(result)

#Split the sentece only at the first occurrence:
result1= re.split("\s", sentence) #use split() methof to chunk *sentences* into many pieces
print(result1)

#Replace white-space characters with the number 5:
result2 = re.sub("\s", "5", sentence)                      # The special sequence /s:Returns the value when string contains a white space 
print(x)
#------------------------------------------------------------------------

#Exceptional Handling 
#Exercise : Print out 'Great! you will get.... gifts with blank as an interge number". Inform the user if not integer number is received.

try:
    n = int(input("Please enter a number: "))
        break
except ValueError:                            # not interger number-> certain error *ValueError*
print("Sorry. Not a valid number.  Try again please!")
else:
    print ('Great! You will get %d gifts', % (n))

#-----------------------------------------------------
#Set

#Example: print out vaulues use 'intersection', 'union', 'diffrence','symetric.different' methods
a = ["Susi", "Sarah", "Sean"]
b = ["Sarah", "Scarlett"]

A = set(a)
B = set(b)

print(A.difference(B))    #return value that exist in set A, not exist in set B
print(A.intersection(B)) #returns values that exists into both set A and set B
print(A.union(B))         #return all values in both sets, including values that are repeated in both sets
print(A.symmetric.difference(B)) # return values that exist only one of 2 sets, no matterr if it is set A or set B
#------------------------------------------------------------------------------------------------------------
#Serialization

#Exercise: print out the JSON string with key-value pair "Me" : 800 added to it.

import json                                #import model: json-> import json


def worker(sala_js, name, salary1):
    money = json.loads(sala_js) #json.loads():takes a string and turns it back into the json object datastructure:
    money[name] = salary1



    return json.dumps(money)#To encode a data structure to JSON,then takes an object and returns a String

money = '{"Susin" : 3000, "Sophia" : 2000 }'
new_money = worker(money, "Him", 8000)
decoded_money = json.loads(new_money)
print(decoded_money["Susin"])
print(decoded_money["Sophia"])
print(decoded_money["Him"])

#-----------------------------------------------------------------------------------------
#Partial Functions

#Print out 10 from calculation: 5 x 2

from functools import partial # import modules partial, from argurment *functools* for returning other functions
def multiply(a,b):            
        return a * b

# create a new function with varriable *multiply*  and number 2
result = partial(multiply,2)
print(result(5))       #default values replace variables from the left->  *2* replace to a, *5 ( in *result(5)*its is called) replace to b
 #------------------------------------------------------------------------------------------------                      

 #Code introspection

# Define the transport class
class transport: 
    name = ''
    color = ''
    kind = ''
    price = 1000.00

def trans_descript(self):
    trans_des ('%s is a %s %s  woth $%.2f.' % (self.name, self.color, self.kind, self.price) )
    return trans_des

# Print a list of all attributes of the transport class-> use dir()
print(dir(trans_descript)

#------------------------------------------------------------------------------------
#Closures

#Example 1: Make a nested loop and a python closure to make functions to get multiple multiplication functions using closures.
# That is using closures, one could make functions to create multiply_with_7() 
def multiply_a(x):      #function outside
    def multiply_b(num):# function inside-> means we have a closure, use nested loop ( def..def..return..return)
        return num*x
    return multiply_b

multiplywith7 = multiply_a(3)
print(multiplywith7(7))

#Example 2: make a cool 'Greeting' with decoration as stars and %
def star(func):
    def inner(*args, **kwargs): #Use inner function to make other functions
        print("*" * 10)
        func(*args, **kwargs)
        print("*" * 10)
    return inner

def percentage(func):
    def inner(*args, **kwargs):
        print("%" * 10)
        func(*args, **kwargs)
        print("%" * 10)
    return inner

def print(content):
    print(content)
printer = star(percentage(printer))

def printer(content):
    print(content)
printer("Hello")
#----------------------------------------------------------------------------------------------
#SQL in SSMS

#example 1: Create a table with columns as varriables: in order
#1: variables: Field name: studentid,forename,surname,address, phonenum
#2 data types for the field: interger, character varrying (32), character varrying (60),character varrying (100)
#3 Other defininitions key: not null primary, not null, not null

#Note that the attributes have to be placed on the table in the same order as below.

#STUDENT
#Field name	Data type for the field	   Other definitions key
#studentid	integer	                    not null primary 
#forename	character varying(32)	    not null
#surname	character varying(60)	    not null
#address	character varying(100)	
#phonenum	character varying(15)


CREATE TABLE   STUDENT (
   StudentID   INTEGER      PRIMARY KEY,
   ForeName    VARCHAR(32)    NOT NULL,
   SurName     VARCHAR(60)    NOT NULL, 
   Address     VARCHAR(100),
   PhoneNum    VARCHAR(15)
);

#--------------------------------------------------------------------------------------

#ML in Python
#Practice with the 
#
#
#
#

#Import Data: use module import: framework scipy, numpy,pandas, matplotlib,sklean
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

#Load the data:
#1.Import library: use the dataset as the “hello world” dataset in machine learning and statistics. 
#2.Load dataset:  csv-> use read-csv. or download:  iris.csv 
#3.Summary dataset:
#3.A.Dimensions of the dataset- use Shape
#3.B Peek at the data itself- Use head
#3.C. Statistical summary of all attributes-use describe()
#3.E.Class Distribution: bread down data baisng on class- use Groupby
#4. Data visualise-#Use Univariate Plots, #Use Multivariate plots
#5. Create data models and check algorism
#6 Validation  for dataset
#7. Make predictions


#1.Import library

from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split

#2.Load dataset csv-> use read-csv. or download:  iris.csv f
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

#3. Summary dataset
#3.A.Dimensions of the dataset- use Shape

print(dataset.shape) #Use shape

#3.B. Peek at the data itself- Use head
print(dataset.head(20))

#3.C. Statistical summary of all attributes-use describe()
print(dataset.describe())

#3.E.Class Distribution: bread down data baisng on class- use Groupby
print(dataset.groupby('class').size())

#4. Data visualise-#Use Univariate Plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

# Data visualisation- Use Multivariate plots
scatter_matrix(dataset)
pyplot.show()

#6 Validation  for dataset
Split-out validation dataset
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train, X _validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

#7Make predictions
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

