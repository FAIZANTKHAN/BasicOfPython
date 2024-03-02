for i in range(5):
    print(f"You ran {i+1} miles")
    tired=input("Are you tired?")
    if tired =='Yes':
        break

if i==4:
    print("Hurray! You are rock star! You just finished 5 km race!")
else:
    print("You didn't finish 5 km but hey congrates anyways!You still ran {i+1} miles")
