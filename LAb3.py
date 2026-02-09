
def yourcode():
    # Function 1: Check if the given number is a proper day number and return "It is a Weekday!" if it is, or "It is a Weekend!" if it is not.
    def check_weekday_or_weekend(day_number):
        if day_number < 1 or day_number > 7:
            return "Not a proper day number!"
        
        if 1 <= day_number <= 5:
            return "It is a Weekday!"
        else:
            return "It is a Weekend!"

    # Function 2: Check if the given number is a proper day number and return the corresponding day name.
    def get_day_name(day_number):
        if day_number == 1:
            return "It is a Monday!"
        elif day_number == 2:
            return "It is a Tuesday!"
        elif day_number == 3:
            return "It is a Wednesday!"
        elif day_number == 4:
            return "It is a Thursday!"
        elif day_number == 5:
            return "It is a Friday!"
        elif day_number == 6:
            return "It is a Saturday!"
        elif day_number == 7:
            return "It is a Sunday!"
        else:
            return "Not a proper day number!"
        
    if __name__ == '__main__':
        day_number = int(input("Enter:"))
        result = check_weekday_or_weekend(day_number)
        print(result)
        if result != "Not a proper day number!":
            print(get_day_name(day_number))

#yourcode()


#20% extra:
def mycode():
    def weekday_end(x):
            if x >= 1 and x <= 7:
                if x < 6:
                    return "It is a Weekday!"
                else: 
                    return "It is a Weekend!"
            else:
                return "Not a proper day number!"

    if __name__ == '__main__':
        while True:
            x = int(input("Enter:"))
            answer = weekday_end(x)
            print(answer)
            if answer != "Not a proper day number!":
                break

    def weeknames(x):
            if x >= 1 and x <= 7:
                if x == 1:
                    return "It is a Monday!"
                elif x == 2:
                    return "It is a Tuesday!"
                elif x == 3:
                    return "It is a Wednesday!"
                elif x == 4:
                    return "It is a Thursday!"
                elif x == 5:
                    return "It is a Friday!"
                elif x == 6:
                    return "It is a Saturday!"
                elif x == 7:
                    return "It is a Sunday!"
            else:
                return "Not a proper day number!"

    if __name__ == '__main__':
        while True:
            x = int(input("Enter:"))
            answer = weeknames(x)
            print(answer)
            if answer != "Not a proper day number!":
                break
mycode()