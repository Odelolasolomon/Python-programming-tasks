def func1(string):
    
    """
    Arguments:
    string----  a text 
    
    Variables ;
    Length--- a variable that stores the length of the string or text
    
    Returns:
    false if does not meet criteria and true if it does
    """
  
  # create varible length to store the length of the string
    length = len(string)
  
  # comapare the string characterwise from left to right with itself on the right side till the middle level
    #if a character  does  not match we do not have a palindrome but if all those characters match 
    #we must have a palindrome
    for i in range(0, length // 2):
        if (string[i] != string[length - i - 1]):
            return False

        return True

def func2(a, b):
    # Save the frequencies of letters and digits
    char_frequency = {}
    for char in a:
        if char.isalnum():
            char_frequency[char] = char_frequency.get(char, 0) + 1

    # If there are fewer than 3 different letters or digits, return None
    if len(char_frequency) < 3:
        return None

    # Convert the dictionary items to a list of tuples
    char_frequency_list = list(char_frequency.items())

    # Sort the list by frequency in descending order
    char_frequency_list.sort(key=lambda x: x[1], reverse=True)

    # Find k-th most frequent item
    count = 0
    for i in range(len(char_frequency_list)):
        # Increment count only if frequency is not the same as previous
        if i == 0 or char_frequency_list[i][1] != char_frequency_list[i - 1][1]:
            count += 1

        if count == b:
            return char_frequency_list[i][0]

    return None  # Return None if k is greater than the number of distinct characters


# Driver program
if __name__ == '__main__':
    input_string = "Solomonmmmnnnn"  # put any string here
    k_value = 3
    result = func2(input_string, k_value)

    if result is not None:
        print(f"The {k_value}-th most frequent character is: {result}")
    else:
        print(f"There is no {k_value}-th most frequent character.")



        
def func3(string):
    # Initialize counters
    uppercase_count = 0
    lowercase_count = 0
    digit_count = 0
    punctuation_count = 0

    # Define punctuation symbols
    punctuation_symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    # Iterate through each character in the input string
    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char in punctuation_symbols:
            punctuation_count += 1

    # Return the counts as a tuple
    return (uppercase_count, lowercase_count, digit_count, punctuation_count)

# Example usage:
if __name__ == '__main__':
    input_str = "Solomon"
    counts = func3(input_str)
    print("Uppercase Count:", counts[0])
    print("Lowercase Count:", counts[1])
    print("Digit Count:", counts[2])
    print("Punctuation Count:", counts[3])
    