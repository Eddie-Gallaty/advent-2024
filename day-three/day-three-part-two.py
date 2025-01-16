import re
text = "from()%mul(296,219)what()select()mul(684,974{where()where()how()~(,{who()mul(106,612)!why()select()select(533,857)who()/^%mul(465,917)?how()do()/?%why()mul(901): select(646,127)mul(395,446)/+,mul(883,551)@'&,?, ?mul(840,262)mul(593,805)from()<~{why(302,32)@do():what()!mul(458,211)how()$mul(804,650)-)mul(708,773)~~do(){',,^why())$why()/mul(987,695)^mul(130,150)mul(311,404)who()what()-do()~~where()why()"
pattern = re.compile(r'\bdo\(\)')

#1 find all the do
#2 figure out how to also include the mul(,)
#3 add to list
#4 remove all the do() and mul()
#5 run eval()
#6 ???
#7 profit

reg = pattern.findall(text)

print(reg)