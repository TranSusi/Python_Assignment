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
    
