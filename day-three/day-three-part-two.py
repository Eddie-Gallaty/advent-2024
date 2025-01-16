import re
text = "don't()7297jhmul(23,23)jskicnbdo()kahjsdmnbmul(4,3){"
pattern = re.compile(r"(?:don't\(\).*?mul\(\d+,\d+\))|(?<!don't\(\))(mul\(\d+,\d+\)|do\(\))")

with open("puzzle.txt") as f:
    text = f.read()
    results = pattern.findall(text)
eval_num = 0
rep_mul = []

regex = re.compile(r'mul\(\d{1,3},\d{1,3}\)') #gross
#1 find all the do
#2 figure out how to also include the mul(,)
#3 add to list
#4 remove all the do() and mul()
#5 run eval()
#6 ???
#7 profit

reg = pattern.findall(text)
new_list = [item for item in reg if item != "" and item != "do()"]

print(new_list)