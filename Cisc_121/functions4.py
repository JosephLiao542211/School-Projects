# CISC-121 2023W

# Name: <Joseph Liao>
# Student Number: <20366481>
# Email: <22jl41@queensu.ca>
# Date: 2023-03-16
# I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity

# Define a function that maps each uppercase letter to a prime number
def char_prime(my_char):
    # A list of the first 26 prime numbers
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
    # A list of the uppercase letters of the alphabet
    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
              'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # A dictionary mapping each uppercase letter to its corresponding prime number
    map = {}
    for i in range(len(letter)):
        map[letter[i]] = prime[i]

    # Return the prime number corresponding to the input uppercase letter
    return map[my_char]

# Define a function that calculates the prime product of a string
def primeify(my_string):
    # If the input string has length 1, return the prime number corresponding to the string
    if len(list(my_string)) == 1:
        return char_prime(*(my_string))
    # Otherwise, recursively calculate the prime product of the string
    else:
        return primeify(list(my_string)[:-1]) * char_prime(list(my_string)[-1])

# Define a function that checks whether two strings are anagrams
def is_anagram(string1, string2):
    # Calculate the prime product of each input string
    tstring1 = primeify(string1)
    tstring2 = primeify(string2)
    # If the prime products are equal, the input strings are anagrams
    if tstring2 == tstring1:
        return "These are anagrams"
    else:
        return "These are not anagrams"

# Define a function that performs counting sort on an array of integers
def counting(arr, exp):
    n = len(arr)
    # Initialize an output array with the same length as the input array
    output = [0] * (n)
    # Initialize a count array with 10 elements, each set to 0
    count = [0] * (10)

    # Count the number of occurrences of each element in the input array
    for i in arr:
        count[(i % (exp * (10))) // exp] += 1

    # Modify the count array to represent the final position of each element in the output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Place each element of the input array into its correct position in the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    #Runs the radix sort
  max1 = max(arr)
  exp = 1
    #adjusts the digits (ones,tens,thousands etc)
  while max1 / exp >= 1:
      counting(arr, exp)
      exp *= 10

  return arr

