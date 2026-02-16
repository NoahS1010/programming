def hollow_square(n):
    result = ""
    row = 1

    while row <= n:
        if row == 1 or row == n:
            result += "*" * n
        else:
            result += "*" + " " *(n-2) + "*"
        
        if row != n:
            result += "\n"

        row += 1     #row = row + 1
    return result

if __name__ == '__main__':
    n = int(input("Enter:"))
    result = hollow_square(n)
    print(result)

def number_pattern(n):
    result = ""
    row = 1

    while row <= n:
        number = 1
        line = ""

        while number <= row:
            line += str(number)
            number += 1 
        result += line
        
        if row != n:
            result += "\n"
        row += 1
    
    return result

if __name__ == '__main__':
    n = int(input("Enter:"))
    result = number_pattern(n)
    print(result)

def sum_of_natural_numbers(n):
    total = 0
    count = 1

    while count <= n:
        total += count
        count += 1
    
    return total

if __name__ == '__main__':
    n = int(input("Enter:"))
    result = sum_of_natural_numbers(n)
    print(result)

def centered_star_pyramid(n):
    result = ""
    row = 1

    while row <= n:
        spaces = " " * (n - row)
        stars = "*" * (2*row-1)
        result += spaces + stars

        if row != n:
            result += "\n"
        
        row += 1
   
    return result

if __name__ == '__main__':
    n = int(input("Enter:"))
    result = centered_star_pyramid(n)
    print(result)