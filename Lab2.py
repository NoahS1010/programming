
#MY FINAL CODE
def my_final_code():
    def height(h0,t):
        g = 9.8
        h = h0 - 0.5* g * t**2
        return round(h,2)

    def calculate_car_distance(time):
            speed = 20
            distance = speed * time
            return distance

    if __name__ == '__main__':
        h0 = int(input("Enter initial height: "))
        t = int(input("Enter time: "))
        h = height(h0,t)
        print(f"Height of the ball at time {t} second = {(h)} meters")
        time = int(input("Enter time for car (in seconds): "))
        distance = calculate_car_distance(time)
        print(f"The car will travel {round(distance)} meters in {(time)} seconds")
my_final_code()

#YOUR CODE
def your_code():
    def calculate_height(h0,t):
            g = 9.8
            height = h0 - 0.5 * g * t**2
            return round(height)

    def calculate_car_distance(t):
            speed = 20
            distance = speed * t
            return distance

    if __name__ == '__main__':
        print(calculate_height(50,3))
        print(calculate_car_distance(1))
        print(calculate_car_distance(3))
#your_code()

#MY EXTRA CODE
def my_extra_code():
    #part 1 height
    def find_height2():
        h0 = float(input("Enter initial height: "))
        t = int(input("Enter time: "))
        g = 9.8
        h = h0 - 0.5* g * t**2
        print(f"Height of the ball at time {t} second = {round(h,2)} meters")
    #find_height2()

    #part 2 car
    def car2():
        speed = 20
        t = float(input("Enter time for car (in seconds): "))
        distance = speed * t
        print(f"The car will travel {round(distance)} meters in {(t)} seconds")
    #car2()
#my_extra_code()