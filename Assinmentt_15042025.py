# Question 1: Write a program to print the first 10 natural numbers using for loop
for i in range(1, 11):
    print(i)


# Question 2: Write a program to print all the even numbers within the range of 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)


# Question 3: Write a program to calculate the sum of all numbers from 1 to a given number - 15
total = 0
for i in range(1, 16):
    total += i
print("Sum:", total)

# Question 4: Write a program to calculate the sum of all the odd numbers within the given range of 15
sum = 0
for i in range(1, 16):
    if i % 2 != 0:
        sum += i
print("Sum of odd numbers:", sum)


# Question 5: Write a program to print a multiplication table of a given number 15
num = 15
for i in range(1, 11):
    print(num," x ",i," = ",num*i)
   


# Question 6: Write a program to display numbers from a list using a for loop [1,2,4,6,88,125]
numbers = [1, 2, 4, 6, 88, 125]
for num in numbers:
    print(num)


# Question 7: Write a program to count the total number of digits in a number 129475
number = 129475
count = 0
while number > 0:
    count += 1
    number = number // 10
print("Total digits:", count)


# Question 8: Write a program to check if the given string is a palindrome - madam
string = "madam"
reversed_string = ""

for i in range(len(string) - 1, -1, -1):
    reversed_string += string[i]

if string == reversed_string:
    print("Palindrome")
else:
    print("Not a palindrome")



# Question 9: Write a program that accepts a word from the user and reverses it using a for loop

word = input("Enter a word: ")
reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print("Reversed word:", reversed_word)



# Question 10: Write a program to check if a given number is an Armstrong number 153
num = 153
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print(num," is an Armstrong number")
else:
    print(num," is not an Armstrong number")


# Question 11: Write a Python program to sum all the items in a list
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print("Sum:", total)


# Question 12: Write a Python program to multiply all the items in a list
numbers = [1, 2, 3, 4]
product = 1
for num in numbers:
    product *= num
print("Product:", product)


# Question 13: Write a Python program to get the largest number from a list
numbers = [3, 8, 1, 99, 67]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)


# Question 14: Write a Python program to get the smallest number from a list

numbers = [3, 8, 1, 99, 67]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print("Smallest number:", smallest)



# Question 15: Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2
words = ['abc', 'xyz', 'aba', '1221']
count = 0
for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1
print("Matching strings:", count)


# Question 16: Write a Python program to remove duplicates from a list.
original_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)
print("List without duplicates:", unique_list)


# Question 17: Write a Python program to check if a list is empty or not.
my_list = []
if not my_list:
    print("The list is empty.")
else:
    print("The list is not empty.")


# Question 18: Write a Python program to clone or copy a list.
list = [1, 2, 3, 4]
copy = []
for item in list:
    copy.append(item)
print("Cloned list:", copy)


# Question 19: Write a Python program to find the list of words that are longer than n from a given list of words.

words = ["hello", "okay","abccdh", "world", "hi", "mouse"]
n = 3
result = []
for word in words:
    if len(word) > n:
        result.append(word)
print("Words longer than", n, ":", result)


# Question 20: Write a Python function that takes two lists and returns True if they have at least one common member.

def common_member(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = [1, 2, 3]
list2 = [4, 5, 3]
print("lists have at leats one common number: ",common_member(list1, list2))

