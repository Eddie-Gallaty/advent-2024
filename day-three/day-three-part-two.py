import re

#1 find all the do
#2 figure out how to also include the mul(,)
#3 add to list
#4 remove all the do() and mul()
#5 run eval()
#6 ???
#7 profit

#text = "don't()7297jhmul(23,23)jskicnbdo()kahjsdmnbmul(4,3){"

#1 and 2 he he he
pattern = re.compile(r"(?:don't\(\).*?mul\(\d+,\d+\))|(?<!don't\(\))(mul\(\d+,\d+\)|do\(\))")

with open("puzzle.txt") as f:
    text = f.read()
    results = pattern.findall(text)

eval_num = 0
rep_mul = []


#3
reg = pattern.findall(text)

#4
new_list = [item for item in reg if item != "" and item != "do()"]

for result in new_list:
    # 1 and 2
    rep_mul.append(re.sub(r"mul\((\d+),(\d+)\)", r"\1 * \2", result)) #nasty
    #print(rep_mul)

for rep in rep_mul:
    eval_num += eval(rep)

print(eval_num)