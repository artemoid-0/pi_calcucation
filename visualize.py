import csv
import matplotlib.pyplot as plt


# Функция для чтения данных из CSV файла
def read_csv_data(filename):
    precisions = []
    divergence_indices = []
    times_taken = []

    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Пропуск заголовка
        for row in reader:
            precisions.append(int(row[1]))
            divergence_indices.append(int(row[2]))
            times_taken.append(float(row[3]))

    return precisions, divergence_indices, times_taken


# Функция для построения 3D-графика
def plot_3d_graph(precisions, divergence_indices, times_taken):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(precisions, divergence_indices, times_taken, c='r', marker='o')

    ax.set_xlabel('Precision (Iterations)')
    ax.set_ylabel('Divergence Index')
    ax.set_zlabel('Time Taken (seconds)')

    plt.title('3D Plot of Precision vs Divergence Index vs Time Taken')
    plt.show()


# Функция для построения 2D-графиков
def plot_2d_graphs(precisions, divergence_indices, times_taken):
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))

    # Precision vs Divergence Index
    axs[0].plot(precisions, divergence_indices, 'b-')
    axs[0].set_xlabel('Precision (Iterations)')
    axs[0].set_ylabel('Divergence Index')
    axs[0].set_title('Precision vs Divergence Index')

    # Precision vs Time Taken
    axs[1].plot(precisions, times_taken, 'g-')
    axs[1].set_xlabel('Precision (Iterations)')
    axs[1].set_ylabel('Time Taken (seconds)')
    axs[1].set_title('Precision vs Time Taken')

    # Divergence Index vs Time Taken
    axs[2].plot(divergence_indices, times_taken, 'r-')
    axs[2].set_xlabel('Divergence Index')
    axs[2].set_ylabel('Time Taken (seconds)')
    axs[2].set_title('Divergence Index vs Time Taken')

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    # Чтение данных из CSV файла
    precisions, divergence_indices, times_taken = read_csv_data('pi_comparison.csv')

    # Построение 3D-графика
    plot_3d_graph(precisions, divergence_indices, times_taken)

    # Построение 2D-графиков
    plot_2d_graphs(precisions, divergence_indices, times_taken)
