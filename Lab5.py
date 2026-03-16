
def sensor_List_Builder_and_Calibrator():
    student_ID = 2578028
    d1 = student_ID % 10 #last digit of student ID
    d2 = (student_ID // 10) % 10 #second-last digit of student ID
    k = (d1 + d2) % 4 + 2
    shift = d1 - d2
    rows_keep = (d1 % 2) + 2

    readings_amount = int(input("How many readings will you enter: "))
    readings = []
    for i in range(readings_amount):
        readings.append(float(input("Enter a reading: ")))
    if len(readings) == 0:
        print("The list is empty")
        return
    print("Full list: ",readings) #Full readings list
    print("First reading: ",readings[0]) #First reading in readings list
    print("Last reading: ",readings[-1]) #Last reading in readings list
    if len(readings) >= 4:
        print("The slice from index 1 to index 3 is: ",readings[1:4]) #The slice from index 1 to index 3
    else:
        print("Not enough readings to print index 1 to 3")
    print("The sum of all the readings in the list is: ",sum(readings))
    second_list_shift = [reading + shift for reading in readings]
    third_list_k = [reading * k for reading in readings]
    element_wise_sum = [a + b for a, b in zip(readings,second_list_shift)]
    print("The original list is: ",readings)
    print("The shifted list is: ",second_list_shift)
    print("The list multiplied by k is: ",third_list_k)
    print("the element wise sum of the original list and the shifted list is:",element_wise_sum)

sensor_List_Builder_and_Calibrator()