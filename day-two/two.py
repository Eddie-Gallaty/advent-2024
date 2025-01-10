#i will not be creating functions because im not a fancy guy!!
reports = []
with open("numbers.txt", 'r') as f:
    for line in f.readlines():
        reports.append(line.strip().split())

safe_reports = len(reports)

for report in reports:
    report = [int(x) for x in report]  
    isSafe = True 
    is_increasing = all(report[a] < report[a+1] for a in range(len(report) -1))
    is_decreasing = all(report[a] > report[a+1] for a in range(len(report) -1))    
    
    for x in range(len(report)-1): 
        abs_diff = abs(report[x] - abs(report[x+1]))
        if abs_diff < 1 or abs_diff > 3:
            isSafe = False 
            break 
    if isSafe and (is_increasing or is_decreasing): 
        print("Hello World")
        print(report)
    else:
        safe_reports -= 1         
print("number of safe reports after counting "+str(safe_reports))