#Multiples -- Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise
for i in range(1, 1000, 2):
    print (i)
#Multiples -- Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000
for m in range(5, 1000000, 5):
    print (m)
#Sum List -- Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b
#Average List -- Create a program that prints the average of the values in the list: c = [1, 2, 5, 10, 255, 3]
c = [1, 2, 5, 10, 255, 3]
dSum = sum(c)
eLen = len(c)
fAvg = (dSum / eLen)
print fAvg