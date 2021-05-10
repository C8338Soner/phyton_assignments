print("How many prime number?")
num1 = int(input("Enter a number:"))
prime = [1]
exercises =[]
for i  in reversed(range(1,num1+1)) :
    for ii in range(1,num1) :
        if not i%ii :
            exercises.append(i)
    if len(exercises)>2:
        exercises.clear()
    else:
        prime.extend(set(exercises)) 


print("in number", num1, ", there are ",len(prime), "prime numbers")
print("these are: ", sorted(prime))
