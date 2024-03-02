sugar_check=int(input("Enter your fasting sugar level"))

if 80>sugar_check :
    print("Sugar is low")
elif sugar_check>100:
    print("Sugar is high")
else:
    print("Please check one more time")
    
