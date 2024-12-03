from pathlib import Path

content = Path('numbers-list.txt').read_text()
list_content  = content.split()
int_list =[x for x in content]

#print(list_content)
list1 = list_content[1::2]
list2 = list_content[0::2]

print("list 1 " + str(len(list1)))
print("list 2 "+ str(len(list2)))
print(len(list_content))
list1.sort()
list2.sort()

a = 0 
z = [ int(x) - int(y) for x, y in zip(list1,list2)]

#this is part ones answer
for b in z:
    a+= abs(b)
print(a)

#part 2

#for x in list1:
   # print(list2.count(x))

my_dict1 = dict(enumerate(list1))
my_dict2 = dict(enumerate(list2))

for value in my_dict1.values():
    print(value)

testlist1 = [1, 2, 2 ,2, 3, 3, 4, 0]
testlist2 = [1, 2, 2 ,2, 3, 4, 4, 0]

testdict1 = dict(enumerate(testlist1))
testdict2 = dict(enumerate(testlist2))

#for key in testdict1.keys():
 #   if key in testdict2 and testdict1[key] == testdict2[key]:
#        print(testdict2[key])



alpha = 0
beta = 0
omega = 0
zeta = 0
for key in testdict1.keys():
    print("starting " + str(alpha))
    if key in testdict2 and testdict1[key] == testdict2[key]:
        alpha += 1
        zeta = key
        print(str(alpha) + " first if")
    if key != zeta:
        print("hello")
        alpha = 0
        print(str(alpha) + " 2nd if")
    else:
        beta = key * alpha
        print(str(beta) + " this is beta")
        omega += beta
        alpha = 0
        print(str(alpha) + " 3rd if")
    
    print(omega)
print(omega)


#for x in list_content:
#    print(x)

#print(list1)


#for x in int_list:
 #   print(x)

#print(list1) 