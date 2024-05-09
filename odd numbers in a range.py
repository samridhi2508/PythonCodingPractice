start=int(input('enter the start range'))
end=int(input('enter the end range'))
for num in range(start,end+1):
    if (num%2!=0):
        print(num)