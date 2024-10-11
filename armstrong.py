# Function to check if a number is an Armstrong number
def is_armstrong(num):
    # Convert the number to a string to calculate the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of digits raised to the power of number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == num

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is an Armstrong number
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
