import matplotlib.pyplot as plt


def plot_results(x, y, xlabel, ylabel, title):
    # General plotting function
    plt.plot(x, y, marker="o")

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.show()


def plot_multiple(series, xlabel, ylabel, title):
    for label, x, y in series:
        plt.plot(x, y, marker="o", label=label)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()
