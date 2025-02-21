n=int(input())
studentscore={}
for i in range(n):
    name,*mark=input().split()
    marks=list(map(float,mark))
    print(marks)
    studentscore[name]=marks
    print(studentscore)
studentname=input()
averagescore=sum(studentscore[studentname])/len(marks)
print(f"{averagescore:.2f}")
