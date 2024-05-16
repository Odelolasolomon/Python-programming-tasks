def is_prime(num):
    """
    Argument:
    num---- an integer
    
    Returns:
    Boolean
    """
    #returns false if the integer is less than 2
    if num < 2:
        return False
    #iterate over the range from 2 and square root of the number
    for i in range(2, int(num**0.5) + 1):
        #return false if there is no remainder after divding the integer by i, True if otherwise
        if num % i == 0:
            return False
    return True


def generate_primes(start, end):
    """
    Argumemts:
    start---- first positive integer
    end------ second positive integer
    
    Returns:
    primes ---- prime numbers between the two positive integers
    """
    
    #if the integers are negative, throw an error
    if start < 0 or end < 0:
        raise ValueError("Both start and end must be positive integers.")
    
    #for loop to iterate over the range of the start to end integers 
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

try:
    start = int(input("Enter the starting positive integer: "))
    end = int(input("Enter the ending positive integer: "))

    result = generate_primes(start, end)
    print("Prime numbers between", start, "and", end, "are:", result)

except ValueError as e:
    print(f"Error: {e}")
