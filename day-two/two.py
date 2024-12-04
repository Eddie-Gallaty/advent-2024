
list1 = ["19 20 21 23 24 25 28 26"]
#with open("numbers.txt", 'r') as f:
 #   for line in f.readlines():
  #      list1.append(line.rstrip('\n'))


##what im going to do is check if the first two numbers are greater than, less than, or equal,
#store in a var, and then do the same for the next.
for num in list1:
    numbers = num.split()


    print(" ".join(numbers))