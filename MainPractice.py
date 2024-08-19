#My Python Journey


# multiline variable
a,b,c, = 30, 22.5, 'Roso'
print (a)
print (b)
print (c)

#CHecking Data type

print (type(a))

print (type(b))

print (type(c))

#WORKING WITH STRING
variable="This is a variable"

print(variable)

#Multiline text

var="""So i attempted to 
write a multiline 
text and it worked 
"""

print (var)

#String_Concatenation

Fname = "felix"
Lname= "owholo"

full_name = Fname + " " + Lname


print (Fname)
print (Lname)
print(full_name)
print("Hello, my names are"+ " "+ full_name.title())

#string formatting
print("Hello, my name is {} {}".format(Fname,Lname))


print(f"My first name is {Fname} and my last name is {Lname}")

print(f"I am {Fname.title()} {Lname.title()}")

#lets experiment cases
#lower
print (full_name.lower())

#UPPER
print(full_name.upper())

#Title_Case
print(full_name.title())


#Working with white spaces

lvar="  leftside spaces"
rvar="rightside spaces  "
bvar="   bothside spaces   "


#Observed the spaces before the trim
print(lvar)
print(rvar)
print(bvar)

#Observed the trimmed write up
print(lvar.lstrip())
print(rvar.rstrip())
print(bvar.strip())

#lets work with numbers
num=1
b=4
a,bb,c,d,e,ds=12,21,43,3,6,54

print(num)
print(b)
print(a)
print(ds)
print(d)
print(num+b+ds)
print(c*b)

name= "Felix"
age=50

print("Hello"+" " + name+ "," + " "+"Happy"+ " "+str(age)+"th Birthday")

# WORKING WITH VARIABLES
fname= 'Felix'
lname= 'Owholo'
age= 38
loc= 'Agbarho'

print("Hello Everyone! My First Name is {0}, and my surname is {1}. I am {2} years old. I am currently staying at {3}. I also have a business at {3}".format(fname,lname,age,loc))

# WORKING WITH INPUT
fname = input('What is your Firstname?: ')
lname = input('What is your Surname: ')
full_name = fname + ' ' + lname
print(f'Hello and welcome Mr. {full_name.title()}.')
age = int(input('How old you?'))
print(f"Great! You are {age} years old.")
dob = (input('When is your next Birthday?'))
print(f"This is Great news, we'll come celebrate with you on {dob.title()} ")

# Perform the 4 most used mathematical operations and return 8 as answer
print(4+4)
print(12-4)
print(16//2)
print(2*4)

# pick a favorite number and use it to make a sentence

favnum=3

print("My favorite number is"+ " " + str(favnum))

import this

# working with list

[1,2,3,4,]


["Cookie Dough", "Strawberry", "Chocolate"]

ice_cream = ["Cookie Dough", "Strawberry", "Chocolate"]

# Adding to a list
ice_cream.append("Salted Caramel")

type(ice_cream)

ice_cream[0]
ice_cream[-1]

# Nesting a list

nested_list=["Cookie Dough", "Strawberry", "Chocolate",["scoops", "spoons"]]

nested_list

nested_list[3]

nested_list[3][1]

motorcycles=['honda', 'yamaha', 'suzuki']

motorcycles.append('ducati')
print(motorcycles)

# Inserting to a List at an index
motorcycles.insert(0, 'ninfang')

print(motorcycles)

# deleting from a list at index

del motorcycles[0]
print(motorcycles)

motorcycles.pop()
print(motorcycles)

last_owned = motorcycles.pop()


print ("The last motorcycle I owned was a " +last_owned.title()+".")

#tuples

tup=(1,2,3,4,1,3,2)

type(tup)

#tuples cannot be edited


# Filtering

ages = [15 ,12 ,45, 12, 18 ,16, 14,17, 23, 45, 23, 65, 19]

def myfunc(x):
    if x < 18:
        return False
    else:
        return True
adults = filter(myfunc, ages)

for x in adults:
    print(x)

# functions
def que_g():
    fname = input('What is your Firstname?: ')
    lname = input('What is your Surname: ')
    full_name = fname + ' ' + lname
    print(f'Hello and welcome Mr. {full_name.title()}.')
    age = int(input('How old you?: '))
    print(f"Great! You are {age} years old.")
    dob = (input('When is your next Birthday?: '))
    print(f"This is Great news, we'll come celebrate with you on {dob.title()} ")

print(que_g())

