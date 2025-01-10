reports = []
with open("num.txt", 'r') as f:
    for line in f.readlines():
        reports.append(line.strip().split())
    #print(reports)
test_list = ["1", "4", "3", "4", "5"]
test_list1 = ["5", "4", "3", "2", "1"]
test_list2 = ["5", "6", "7", "50", "1"]
test_list3 = ["5", "4", "3", "2", "8"]

is_inc = 0
is_desc = 0
not_inc = 0
not_desc = 0
neither = 0
notSafeAbs = 0
num_reports = len(reports)


def isSafe(report):#, is_inc, is_desc, not_inc, not_desc, neither, notSafeAbs):
    #report = int(report)
    isIncreasing = all((x < y for x, y in zip(report, report[1:])))
    isDecreasing = all ((x > y for x, y in zip(report, report[1:])))
    for x in report in range(len(report) -1):
        print(x)
        #abs_num = int(report[x]) - int(report[x + 1])
      # abs_num = abs(abs_num)
       # y = abs(x) - abs(x+1)
       # y = abs(y)
       # print(str(abs_num))
       
        #if abs_num < 1 or abs_num >= 3:
           #print("here")

        return False

for report in reports:
  #  print("testing " +str(isSafe(report)))
    if not isSafe(report):
        num_reports += 1

print(num_reports)


    

#print("There are "+str(is_inc)+" reports that are increasing")
#print("There are "+str(is_desc)+" reports that are decreasing")
#print("There are "+str(not_inc)+" reports that are NOT increasing")
#print("There are "+str(not_desc)+" reports that are NOT decreasing")
#print("There are "+str(neither)+" reports that are NEITHER increasing nor decreasing")
#print("There are "+str(notSafeAbs)+" reports that are NOT safe abs");
#print("testing " +str(isSafe(test_list1)))