#almost identical to the original. turns out i cant figure another way to do this. 

reports = []
with open("num.txt", 'r') as f:
    for line in f.readlines():
        reports.append(line.strip().split())

test_list = ["1", "5", "6", "4", "5"]
test_list1 = ["5", "5", "3", "2", "1"]
test_list2 = ["5", "6", "7", "50", "1"]
test_list3 = ["5", "4", "3", "2", "1"]
test_list4 = ["1", "2", "3", "4", "5"]
num_reports = 0
list(map(int, test_list))

modified_report = []

def isSafe(report):
    report = [int(x) for x in report] # blanket casting int 
    safe = True
    isIncreasing = all((x < y for x, y in zip(report, report[1:])))
    isDecreasing = all ((x > y for x, y in zip(report, report[1:])))

    for x  in range(len(report) -1):
       bad_reports = 0
     #   print(report[x])
      # report = [int(i) for i in report] #casting all elements in report to int <--- WRONG WRONG WRONG WRONG WRONG 
       abs_diff = abs(report[x] - abs(report[x + 1]))
       if abs_diff < 1 or abs_diff > 3:
          #dified_report.append(report[x+1:])
          return False
     # num_reports += 1
    return isIncreasing or isDecreasing

def isSafe_with_dampener(report):
    for r in range(len(report)):
        modified_rep = report[:r] + report[1 + r:]
        if isSafe(modified_rep):
            return True

print(isSafe_with_dampener(test_list))

for report in reports:
    if isSafe_with_dampener(report):
        num_reports +=1

print(num_reports)