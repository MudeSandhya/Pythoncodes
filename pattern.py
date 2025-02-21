start=1
stop=2
num=stop
for i in range(2,6):
    for j in range(start,stop):
        num=num-1
        print(num,end="")
    print("\r")
    start=stop
    stop=stop+i
    num=stop


