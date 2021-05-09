print( "Get all Prime numbers in a range\n")
num1 = int(input("Enter number in the range: "))

prime_list = []

def is_prime(num) :
    result = "Prime"
    for t in range (2,num) :
        if not num%t :
            result = "Not Prime"
            break
    return result

def get_all_prime(num1) :
    for x in range(num1) :
        if is_prime(x) == "Prime" :
            prime_list.append(x)
    return prime_list


get_all_prime(num1)
print("\n", prime_list)
