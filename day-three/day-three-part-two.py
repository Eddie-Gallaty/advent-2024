#mul is enabled at the start. once it hits a don't() it will be 
#disabled until it hits a do(). any mul() after do() is again enabled
#this continues until the end of the "puzzle.txt" file.
#i accomplished this one by using regex which i think is the obvious path. also i hate regex

import re

test_text = "mul(345,3221)asdfasdfmul(91,1)don't()mul(1,2)do()jhkjshdcanemul(12,124)jhkndon't()mul(123,456)do()mul(543,321)"
regex = re.compile(r'do\(\)|mul\(\d+,\d+\)|don\'t\(\)')
# the d+ tells it to look for a sequence of numbers:  1, 1231344321, etc

with open("puzzle.txt") as f:
    text = f.read()
    results = regex.findall(text)

test_results = regex.findall(test_text)

#mul() will be enabled by default until it hits don't()
mul_enabled = True
eval_mul = 0

#for res in results:
#    print(res)
for res in results:
    if  res == "do()":
      #  print("hello")
        mul_enabled = True
    elif res == 'don\'t()':
       # print("don't detected")
        mul_enabled = False
    elif res.startswith("mul(") and mul_enabled == True:
       # print(test)
        #this is taking mul() and forming twi groups, one for each set of ints
        match = re.match(r"mul\((\d+),(\d+)\)", res)
                
        if match:
            #casting to int using map. this is where the regex groups get extracted
            mul1, mul2 = map(int, match.groups())
            print(str(mul1) + " " + str(mul2))
            eval_mul += mul1 * mul2
# :)
print(eval_mul)

