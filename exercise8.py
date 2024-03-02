india=["mumbai","banglore","chennai","delhi"]
pakistan=["lahore","karachi","islamabad"]
bangladesh=["dhaka","khulna","rangpur"]

belong_to=input("Enter the city name to check")

if belong_to in india:
    print("Indian City")
elif belong_to in pakistan:
    print("Pakistani City")
elif belong_to in bangladesh:
    print("bangladesi City")
else:
    print("Dont know brother")
