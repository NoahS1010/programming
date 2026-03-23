def square_array_with_id():
    student_id = 2578028
    d1 = student_id % 10 #last digit of student ID
    d2 = (student_id // 10) % 10 #second-last digit of student ID
    k = (d1 + d2) % 4 + 2
    shift = d1 - d2
    rows_keep = (d1 % 2) + 2

    matrix = [
            [5, 10, 15, 20, 25],
            [30, 35, 40, 45, 50]
    ]

    rows = len(matrix)
    columns = len(matrix[0])
    print(f"\nThis matrix is {rows} rows by {columns} columns")
    print("\nMatrix: ")
    for row in matrix:
        print(row)
    #Print the last column in matrix
    last_column = [row[-1] for row in matrix]
    print("\nLast column: ", last_column)
    #print a sub-array containing all rows but only the first 3 columns
    print("\nsub-array of first 3 columns:")
    sub_array = [row[:3] for row in matrix]
    for row in sub_array:
        print(row)

    #MODIFYING
    special_row = d1 % rows
    special_col = d2 % 2
    print(f"\nChosen row = d1 % rows so {d1} % {rows} = {special_row}")
    old_row = matrix[special_row]
    new_row = [num + k for num in old_row]
    matrix[special_row] = new_row
    print("Old row: ", old_row)
    print("New row: ", new_row)
    print(f"start column = d2 % 2 so {d2} % {2} = {special_col}")
    sliced_sub_array = [row[special_col:] for row in matrix]
    print("\nSliced_sub_array: ")
    for row in sliced_sub_array:
        print(row)
square_array_with_id()  