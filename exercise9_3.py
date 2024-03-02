month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]

e=int(input("Enter expense amount to check it:"))

month=-1
for i in range(len(expense_list)):
    if e==expense_list[i]:
        month=i
        break


if month!=-1:
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend {e} in any month')
