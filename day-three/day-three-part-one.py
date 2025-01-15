#part one of day three 
import re 

regex = re.compile(r'mul\(\d{1,3},\d{1,3}\)') #gross

with open("puzzle.txt") as f:
    text = f.read()
    results = regex.findall(text)
eval_num = 0
rep_mul = []
#todo
#1. strip mul out, parens, and replace , with a *
#2. add to new list - not needed
#3. cast list to int - not actually needed with eval()
#4 perform multiplication and then add all to a final var

#1
for result in results:
    #2
    rep_mul.append(re.sub(r"mul\((\d+),(\d+)\)", r"\1 * \2", result)) #nasty
    #print(rep_mul)

rep_mul
for mul in rep_mul:
    #3 and 4.
    eval_num += eval(mul)

# :)
print(eval_num)
