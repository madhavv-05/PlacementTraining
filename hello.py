
import math
"""
name=input("Enter your name: ")

print(name)

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))

sum=num1+num2


print("sum of ",num1," and ",num2," is: ",sum)


l=int(input("enter length of triangle:  "))
b=int(input("eter base of triangle:  "))

h=((l**2+b**2)**0.5)

print("hypotaneuse of triangle is: ",h)


+----------+
|                      |
|                      |
|                      |
|                      |
|                      |
+----------+

print("+----------+")
print("|          |\n|          |\n|          |\n|          |\n|          |")

print("+----------+")


var=0
print(var==0)

var=1
print(var==0)




sheep_counter = 10


if sheep_counter >=120:
    print("make_a_bed")
    print("take_a_shower")
    print("sleep_and_dream")
print("feed the sheens")


sheep_counter = 130
weather_is_good = True
if sheep_counter >=120:
    if weather_is_good:
        print("make_a_bed")
        print("take_a_shower")
        print("sleep_and_dream")
    else:
        print("I cannot go out")
else:
    print("Not able to count sheep")

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

number1=int(input("Enter number 1: "))
number2=int(input("Enter number 2: "))
if number1 > number2: arger_number = number1
else:larger_number = number2

print("The larger number is:", larger_number)


number1=int(input("Enter number 1: "))
number2=int(input("Enter number 2: "))
number3=int(input("Enter number 3: "))

largest=number1

if(number2>largest): largest=number2
if(number3>largest): largest=number3

print("largest number is: ",largest)





Write a program that utilizes the concept of conditional execution, takes a string as input, and:
prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)




plant=input("W=Enter name of the plant:  ")

if plant=="Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant=="spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else: 
    print("Spathiphyllum! Not ", plant)




largest=-999999999
number=int(input("Enter a number: "))



while number!=-1:
    if(number>largest):
        largest=number
    number=int(input("Enter a number(enter -1 to stop): "))

print("largest number is: ",largest)


Write a program that reads a sequence of numbers and counts how many numbers are even and how many are odd. The program terminates when zero is entered.


number=int(input("Enter a number: "))
even=0
odd=0


while number!=0:
   
    if(number%2==0):
        even=even+1

    else:
        odd=odd+1
    number=int(input("Enter a number(enter 0 to stop): "))

print("even numbers are: ",even)
print("odd numbers are: ",odd)



for counter in range(100):
    print("current value of counter is: ",counter)


    
for counter in range(2,8,3):
    print("current value of counter is: ",counter)


power=1
for exp in range(16):
    print("2 to the power of ",exp," is ",power)
    power*=2

 



import time

for counter in range(5):
    if counter==2:
        continue
    print(counter+1, " mississippi")
    
    time.sleep(1)

print("Ready or not, Here I come!")



largest=-9999999999
number=int(input("Enter a number(enter -1 to stop): "))
while True:
    if number==-1:
        break
    if(number>largest):
        largest=number
    number=int(input("Enter a number(enter -1 to stop): "))

print("largest number is: ",largest)




word=input("Enter a word: ")
word_upper=word.upper()

for letter in word_upper:
    if letter in ["A","E","I","O","U"]:
        continue
    print(letter)



blocks=int(input("Enter numbe rof blocks: "))
sum=0
for counter in range(blocks):
    if sum>blocks:
        break
    
    
    sum+=counter
    

print("height is ",counter-1)





block_size= int(input("Enter the number of blocks: "))
 
blocks_needed_at_level = 0 
height = 0  

for _ in range(block_size):  
    if (blocks_needed_at_level + (height + 1)) <= block_size:  
        height += 1
        blocks_needed_at_level += height
    else:
        break  

print("Maximum height of the pyramid:", height)



c0=int(input("Enter a number: "))
steps=0


while (c0!=1):
    if c0%2==0:
        c0=c0/2
        steps+=1
        print(c0)
    else:
        c0=(c0*3)+1
        steps+=1
        print(c0)

print("Number of steps neede are: ",steps)



numbers=[10,20,23,30]
print("original list conatins: ",numbers)

numbers[0]=100
print("new list constains: ",numbers)


numbers = [10, 5, 7, 2, 1]
print ("first element content: ", numbers [0] )
print ("second element content: ", numbers [1] )
print ("third element content: ", numbers [2])
print ("fourth element content: ", numbers [3] )
print ("fifth element content: ", numbers [4])

numbers[0]=11
print ("first element content: ", numbers [0] )

numbers[1]=numbers[5]
print ("new list is:")
print ("first element content: ", numbers [0] )
print ("second element content: ", numbers [1] )
print ("third element content: ", numbers [2])
print ("fourth element content: ", numbers [3] )
print ("fifth element content: ", numbers [4])



numbers = [10, 5, 7, 2, 1]
print("size of numbers is: ",len(numbers))


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print("List: ", list)
print("5th element: ", list[4])

del list[0]
print("List: ", list)
print("5th element: ", list[4])

del list[4]
print(" List: ", list)
print("5th element: ", list[4])

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
for count in range(len(list)-1):
    del list[0]
    print(list)
print("List: ", list)

del list
print("List: ", list)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(list[-1])

print(list)
for count in range(len(list)):
    #print("count:", count) # 0 1 2 4 5227 8:9
    print("list[-",count+1,"]:", list[-1*(count+1)])

    """

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list.append(80)
list.insert(1,10)

print(list)

for li in list:
    print(li)

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
print(my_list)

