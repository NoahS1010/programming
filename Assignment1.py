#QUESTION_1 

#TASK_1_CODE
# Function 1: Conditional Statements – The If Statement
# This function checks if a number is positive, negative, or zero and returns the right message.
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

#TASK_2_UNDERSTANDING
    # input = number, which is variable of a value put into function (check_number)
    # output = string, Positive, Negative or Zero, depending on the input
    # main variable = number, which is value that function checks
    # functions used = if,elif,else, which compare number to zero to see if its smaller, bigger or equal to Zero

#TASK_3_MODIFICATIONS
#def check_number(number):
#    if number > 0:
#        return "The number is Positive!"
#    elif number < 0:
#        return "The number is Negative!"
#    else:
#       return "The number is Zero!"

# The code works well as is but the output could be more descriptive so I added more words.



#QUESTION_2

#TASK_1_CODE
# Function 2: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    shape = ""
    for i in range(1, rows + 1):
        shape += "*" * i + "\n"
    return shape.strip()  # Remove trailing newline at the end

#TASK_2_UNDERSTANDING
    # input = rows, which is variable that determines how many rows of stars
    # output = string, rows of stars shaped into a triangle
    # main variable = rows (# of rows), shape (stores stars) and i ( count in loop).  
    # functions used = for loop and range()

#TASK_3_MODIFICATIONS
#def star_shape(rows):
#    shape = ""
#    for i in range(1, rows + 1):
#        shape += ("* " * i) + "\n"
#    return shape.strip()

# Added a space in paranthesis with star so that stars would be more spread out and look better. Also added parenthesis to make it more organized.



#QUESTION_3

#TASK_1_CODE
# Function 3: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    num = 1
    result = ""
    while num <= limit:
        if num % 3 == 0:
            result += "Multiple of 3\n"
        else:
            result += str(num) + "\n"
        num += 1
    return result.strip()  # Remove trailing newline at the end

#TASK_2_UNDERSTANDING
    # input = limit, which is variable that tells us how high to count
    # output = string of numbers 1 to limit number. If number divisble by 3, then it'll return Multiple of 3
    # main variable = limit (max number counted to), num (number being currently checked) and result (holds final output string).  
    # functions used = while loop and %, which sees if num is divisible by 3 without remainders

#TASK_3_MODFICATIONS
#def count_multiples_of_3(limit):
#    num = 1
#    result = ""
#    while num <= limit:
#        if num % 2 == 0:
#            result += "Even number\n"
#        elif num % 3 == 0:
#            result += "Multiple of 3\n"
#        else:
#            result += str(num) + "\n"
#        num += 1
#    return result.strip()

#Added to see if divisble by 2 (even) and if its not then check if divisble by 3.



#QUESTION_4

#TASK_1_CODE
# Function 4: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    return total

#TASK_2_UNDERSTANDING
    # input = start and end, which are variables that determines range of numbers
    # output = sum of all the even numbers inside the range
    # main variable = start (start of range), end (end of range), num (number being currently checked) and total (stores sum of all numbers) 
    # functions used = for loop range() and %, which sees if num is even and adds it to sum

#TASK_3_MODIFICATIONS
#def sum_of_even_numbers(start, end):
#    total = 0
#    even_count = 0
#    for num in range(start, end + 1):
#        if num % 2 == 0:
#            total += num
#            even_count = even_count + 1
#    return total, even_count

#Added even_count to see how many even numbers are in the range.

if __name__ == "__main__":
    print("QUESTION 1")
    number = int(input("Enter a number: "))
    result = check_number(number)
    print(result)
    print("\nQUESTION 2")
    rows = int(input("Enter a number: "))
    result = star_shape(rows)
    print(result)
    print("\nQUESTION 3")
    limit = int(input("Enter a number: "))
    result = count_multiples_of_3(limit)
    print(result)
    print("\nQUESTION 4")
    start = int(input("Enter a number: "))
    end = int(input("Enter a greater number: "))
    result = sum_of_even_numbers(start,end)
    print(result)