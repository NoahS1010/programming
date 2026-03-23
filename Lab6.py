def temp_change_with_id():
    student_id = 2578028
    d1 = student_id % 10 #last digit of student ID
    d2 = (student_id // 10) % 10 #second-last digit of student ID
    k = (d1 + d2) % 4 + 2
    shift = d1 - d2
    rows_keep = (d1 % 2) + 2

    temperatures = [
        [21, 22, 23, 24],
        [25, 26, 27, 28],
        [29, 30, 31, 32]
    ]
    #Printing full original matrix
    print("Original Temperatures: ")
    for row in temperatures:
        print(row)
    #Print specific element in temperatures
    specific_element = temperatures[1][2]
    print("\nSpecific element[1][2]: ", specific_element)
    #Print first two rows element in temperatures
    first_two_rows = temperatures[:2]
    print("\nFirst two rows: ",first_two_rows)
    #Print the first column in temperatures
    first_column = [row[0] for row in temperatures]
    print("\nFirst column: ", first_column)
    #print 2×2 sub-array from the upper-left corner
    print("\n2×2 sub-array from the upper-left corner:")
    sub_array = [row[:2] for row in first_two_rows]
    for row in sub_array:
        print(row)
    #MODIFYING
    num_rows = len(temperatures)
    num_cols = len(temperatures[0])
    modified_row = d1 % num_rows
    modified_col = d2 % num_cols

    print("\nModifyng temperatures:")
    print(" The row that will be modifed is: ",modified_row)
    print(" The column that will be modifed is: ",modified_col)
    for a in range(num_cols):
        temperatures[modified_row][a] += shift
    for b in range(num_rows):
        temperatures[b][modified_col] *= k

    print("\nModified temperatures:")
    for row in temperatures:
        print(row)
    print("\nSub array:")
    sub_array_Mod = [row[:k] for row in temperatures[:rows_keep]]
    for row in sub_array_Mod:
        print(row)
temp_change_with_id()