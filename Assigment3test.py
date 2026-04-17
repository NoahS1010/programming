# Assignment 3

import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# -----------------------------
# Part 0 — Student ID Setup
# -----------------------------
student_id = 2578028
d1 = student_id % 10 #last digit of student ID
d2 = (student_id // 10) % 10 #second-last digit of student ID
k = (d1 + d2) % 4 + 2
shift = d1 - d2
n_points = 20 + d1
frame_step = d2 + 1

print("Student ID:", student_id)
print("k =", k)
print("shift =", shift)
print("n_points =", n_points)
print("frame_step =", frame_step)

# -----------------------------
# Component A1 — 2D Line Plot
# -----------------------------
x = list(range(1, n_points + 1))
y = [i**2 for i in x]

# Debugging checks
if len(x) == 0 or len(y) == 0:
    print("Error: Data is empty")
elif len(x) != len(y):
    print("Error: Length mismatch")
else:
    plt.figure(figsize=(8, 5))
    plt.plot(x, y)
    plt.title("Simple Line Plot")
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.show()

# -----------------------------
# Component A2 — Distribution Plot
# -----------------------------
data_values = [random.randint(0, 50) for _ in range(50)]

print("First 10 values:", data_values[:10])

plt.figure(figsize=(8, 5))
plt.hist(data_values, bins=10)
plt.title("Distribution of Data")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# Component B1 — Personalized 2D Plot
# -----------------------------
y2 = [k * i + shift for i in x]

print("First 5 (x, y2) pairs:")
print(list(zip(x[:5], y2[:5])))

plt.figure(figsize=(8, 5))
plt.plot(x, y2, linestyle='--', marker='o')
plt.title(f"ID: {student_id} | k={k}, shift={shift}")
plt.xlabel("X Values")
plt.ylabel("Y2 Values")
plt.show()

# -----------------------------
# Component B2 — 3D Scatter Plot
# -----------------------------
x3 = list(range(1, n_points + 1))
y3 = [i + shift for i in x3]
z3 = [k * i for i in x3]

print("First 5 (x, y, z):")
print(list(zip(x3[:5], y3[:5], z3[:5])))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x3, y3, z3)

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("3D Scatter Plot")

plt.show()

# -----------------------------
# Component B3 — Animation
# -----------------------------
x_anim = list(range(n_points))
y_anim = [k * i + shift for i in x_anim]

fig, ax = plt.subplots()
line, = ax.plot([], [])

ax.set_xlim(0, n_points)
ax.set_ylim(min(y_anim), max(y_anim))

def update(frame):
    print("Animating frame:", frame)  # Required debug
    line.set_data(x_anim[:frame], y_anim[:frame])
    return line,

ani = FuncAnimation(
    fig,
    update,
    frames=range(1, n_points, frame_step),
    repeat=False
)

plt.title("Animated Line Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
