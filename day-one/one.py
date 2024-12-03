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


for b in z:
    a+= abs(b)

for i in list1:
    print(i)
print(a)

#for x in list_content:
#    print(x)

#print(list1)


#for x in int_list:
 #   print(x)

#print(list1) 