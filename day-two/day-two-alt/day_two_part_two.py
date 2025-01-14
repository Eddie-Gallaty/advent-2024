reports = []
with open("num.txt", 'r') as f:
    for line in f.readlines():
        reports.append(line.strip().split())

test_list = ["1", "5", "5", "4", "5"]
test_list1 = ["5", "4", "3", "2", "1"]
test_list2 = ["5", "6", "7", "50", "1"]
test_list3 = ["5", "4", "3", "2", "8"]
num_reports = 0
list(map(int, test_list))
reports = [[int(i) for i in report] for report in reports] #jesus help me

modified_report = []

def isSafe(report, num_reports):
    
    safe = True
    isIncreasing = all((x < y for x, y in zip(report, report[1:])))
    isDecreasing = all ((x > y for x, y in zip(report, report[1:])))
   


    for x  in range(len(report) -1):
       bad_reports = 0
     #   print(report[x])
      # report = [int(i) for i in report] #casting all elements in report to int <--- WRONG WRONG WRONG WRONG WRONG 
       abs_diff = abs(report[x] - abs(report[x + 1]))
       if abs_diff < 1 or abs_diff > 3:
          bad_reports += 1
          modified_report.append(report[x+1:])
          break


          safe = False
    #print(modified_report)
    for rep in modified_report:
        for r in range(len(rep)-1):
            #print(rep[r])
            abs_diff = abs(rep[r]) - abs(rep[r + 1])
            print("hello")
            if abs_diff < 1 or abs_diff > 3:
                return False
            else:
                return modified_report
    #if safe and (isIncreasing or isDecreasing):
     # num_reports += 1


    return True


def isSafe_with_dampener(report):

    isIncreasing = all((x < y for x, y in zip(report, report[1:])))
    isDecreasing = all ((x > y for x, y in zip(report, report[1:])))


"""
for report in reports:
  #  print("testing " +str(isSafe(report)))
  num_reports = isSafe(report, num_reports)
"""

print(isSafe(list(map(int, test_list1)), num_reports))
