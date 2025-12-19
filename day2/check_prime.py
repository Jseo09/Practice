def is_prime(num):
    if num == 2:
        return True 
    elif num == 1: 
        return False 
    for x in range(2, int(num)-1):
        if num % x == 0:
            return False
    return True

print(is_prime(75))
