print("Using for loop figure out how many times you got heads")
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count=0
for i in result:
    if i=="heads":
        count+=1
print("Heads count is:",count)
