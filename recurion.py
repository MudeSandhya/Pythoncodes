def even(num1,num2):
    if num1>num2:
        return
    if num1%2==0:
        print(num1)
    even(num1+1,num2)
even(10,31)
