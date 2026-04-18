#Lab 9

import matplotlib.pyplot as plt

# Task 1: Curve Plot
def plot_curve(x_values, y_values):
    # Debug checks
    if len(x_values) == 0 or len(y_values) == 0:
        print("Error: Data is empty")
        return

    if len(x_values) != len(y_values):
        print("Error: Length mismatch")
        return

    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values)
    plt.title("Curve Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()

# Task 2: Hertzsprung-Russell Diagram
def plot_hr_diagram(temperature, luminosity):
    # Debug checks
    if len(temperature) == 0 or len(luminosity) == 0:
        print("Error: Data is empty")
        return

    if len(temperature) != len(luminosity):
        print("Error: Length mismatch")
        return

    plt.figure(figsize=(8, 5))

    # Scatter plot
    plt.scatter(temperature, luminosity)
    plt.title("Hertzsprung-Russell Diagram")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Luminosity (L)")

    # Reverse x-axis
    plt.gca().invert_xaxis()

    plt.show()

# Task 3: Density Plot (Heatmap)
def plot_density(data, color_map):
    # Debug check
    if len(data) == 0:
        print("Error: Data is empty")
        return

    # Split into x and y
    x = [point[0] for point in data]
    y = [point[1] for point in data]

    plt.figure(figsize=(8, 5))

    # 2D histogram (density plot)
    plt.hist2d(x, y, bins=20, cmap=color_map)

    plt.colorbar(label="Density")

    plt.title("Density Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    plt.show()

if __name__ == "__main__":

    # Task 1 example
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    plot_curve(x, y)

    # Task 2 example
    temperature = [5000, 6000, 7000, 8000]
    luminosity = [1.0, 1.5, 2.0, 2.5]
    plot_hr_diagram(temperature, luminosity)

    # Task 3 example
    data = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (2, 2), (3, 3)]
    plot_density(data, "viridis")

