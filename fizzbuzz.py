def fizbuz(liste):
    for i in liste :
        if not i%15:
            liste[liste.index(i)] = "FizzBuzz"
        elif not i%5 :
            liste[liste.index(i)] = "Buzz"
        elif not i%3 :
            liste[liste.index(i)] = "Buzz"
    return liste

liste = list(range(1,60))

print(fizbuz(liste))
