#i will not be creating functions because im not a fancy guy!!
reports = []
with open("numbers.txt", 'r') as f:
    for line in f.readlines():
        reports.append(line.strip().split())

safe_reports = len(reports)

for report in reports:
    report = [int(x) for x in report] # blanket casting int 
    isSafe = True # reset to true each start of a new iteration
    is_increasing = all(report[a] < report[a+1] for a in range(len(report) -1))  #increase check 
    is_decreasing = all(report[a] > report[a+1] for a in range(len(report) -1))  #decrease check (all is a cool function)
    
    #this bit took me about 6 hours of troubleshooting and reading docs. i deleted 4 different ways of trying before i landed on this
    for x in range(len(report)-1): #this is looping through each of the numbers of the report. 
        abs_diff = abs(report[x] - abs(report[x+1])) # getting the difference between the index and its neighbor (going right)
        if abs_diff < 1 or abs_diff > 3: #if it is not within the ranges, set it to false. equal to or greater than 1 and less than or equal to 3
            isSafe = False #set this bad boy to false
            break # jumping to the next as soon as it fails the compare check
    if isSafe and (is_increasing or is_decreasing):  #bool checks
        print("Hello World")
        print(report)
    else:
        safe_reports -= 1     #minus one from the safe reports list is report fails the bool checks
    
#Answer for part one :)           
print("number of safe reports after counting "+str(safe_reports))