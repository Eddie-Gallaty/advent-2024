from pathlib import Path
from collections import Counter

content = Path('num1.txt').read_text()
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
print("part one answer " + str(a))

#part 2

# I SPENT THREE HOURS ON THIS BECAUSE I HAD MY LISTS IN THE WRONG ORDER :)))))))))))))) 
omega = 0
for x in list2:
   val = list1.count(x)
  # print(val)
   omega += val * int(x)
print("part two answer " + str(omega))   





