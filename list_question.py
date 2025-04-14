hat = [1, 2, 3, 4, 5]


print("length of hat is: ",len(hat))

del hat[len(hat)-1]
print("hat after removing last element is: ",hat)

num=int(input("Enter a number to replace the middle element: "))
hat[len(hat) // 2] = num
print("hat after replacing middle element is: ",hat)