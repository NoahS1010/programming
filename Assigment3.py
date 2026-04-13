student_id = 2578028
d1 = student_id % 10 #last digit of student ID
d2 = (student_id // 10) % 10 #second-last digit of student ID
k = (d1 + d2) % 4 + 2
shift = d1 - d2
n_points = 20 + d1
frame_step = d2 + 1