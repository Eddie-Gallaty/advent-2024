reports = []
with open("num.txt", 'r') as f:
    for line in f.readlines():
        reports.append(line.strip().split())

test_list = ["1", "4", "3", "4", "5"]
test_list1 = ["5", "4", "3", "2", "1"]
test_list2 = ["5", "6", "7", "50", "1"]
test_list3 = ["5", "4", "3", "2", "8"]

reports = [[int(i) for i in report] for report in reports] #jesus help me

def isSafe(report, num_reports):
    
    safe = True
   
    isIncreasing = all((x < y for x, y in zip(report, report[1:])))
    isDecreasing = all ((x > y for x, y in zip(report, report[1:])))

    for x  in range(len(report) -1):
     #   print(report[x])
      # report = [int(i) for i in report] #casting all elements in report to int <--- WRONG WRONG WRONG WRONG WRONG 
       abs_diff = abs(report[x] - abs(report[x + 1]))
       if abs_diff < 1 or abs_diff > 3:
          safe = False

    if safe and (isIncreasing or isDecreasing):
       num_reports += 1

    return num_reports

for report in reports:
  #  print("testing " +str(isSafe(report)))
  num_reports = isSafe(report, num_reports)

print(num_reports)
