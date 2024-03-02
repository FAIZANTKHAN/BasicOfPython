def pattern(row):
    for i in range(row):
        s=""
        for j in range(i+1):
            s=s+'*'
        print(s)

r=int(input("Enter the no. of rows"))
print(pattern(r))
