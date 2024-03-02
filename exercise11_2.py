def circle_op(r):
    diameter=2*r
    circumference=2*3.14*r
    area=3.14*r**2
    return  diameter,circumference,area;

if __name__=="__main__":
    radius=int(input("Enter the value of radius"))
    print(circle_op(radius))