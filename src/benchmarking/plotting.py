import matplotlib.pyplot as plt


def plot_results(x, y, xlabel, ylabel, title):
    # General plotting function
    plt.plot(x, y, marker="o")

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.show()
