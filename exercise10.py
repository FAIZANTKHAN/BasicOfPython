def calculate_area(base,height):
    print("Here the area of triangle for provided height and base")
    area = (1/2)*base*height
    return area

base=int(input("Enter the value of base"))
height=int(input("Enter the value of height"))

print(calculate_area(base,height))         
