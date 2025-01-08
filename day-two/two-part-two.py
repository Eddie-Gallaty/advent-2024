# this was some BULL

reports = []
with open("numbers.txt", 'r') as f:
    for line in f.readlines():
        reports.append(line.strip().split())

test_report = ["14", "23", "45", "11", "67"], ["13", "44", "55", "66", "88"], ["11", "22", "33", "44", "55"]
safe_reports = len(reports)

def isSafe(report):
    report = [int(x) for x in report] # blanket casting int 
    is_increasing = all(report[a] < report[a+1] for a in range(len(report) -1))  #increase check 
    is_decreasing = all(report[a] > report[a+1] for a in range(len(report) -1))  #decrease check (all is a cool function)
    for x in range(len(report)-1): #this is looping through each of the numbers of the report. 
            abs_diff = abs(report[x]  - report[x+1]) # getting the difference between the index and its neighbor (going right)
            if abs_diff < 1 or abs_diff > 3: #if it is not within the ranges, set it to false. equal to or greater than 1 and less than or equal to 3
                return False
    return is_increasing or is_decreasing

def isSafe_with_dampener(report):
        for x in range(len(report)):
            print(report[:x] + report[1 + x:])
            modified = report[:x] + report[1 + x:]
            if isSafe(modified):
                return True
        return False

for report in reports:
    if not isSafe(report) and not isSafe_with_dampener(report):
        safe_reports -= 1

print("number of safe reports after counting "+str(safe_reports))
#print(isSafe_with_dampener(test_report))


