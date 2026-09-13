import random
from pathlib import Path

# create datasets folder
datasets = Path("datasets")
datasets.mkdir(parents=True, exist_ok=True)

# set increasing array sizes from 1k to 10 mil
sizes = [
    1_000,
    5_000,
    10_000,
    50_000,
    100_000,
    500_000,
    1_000_000,
    2_000_000,
    5_000_000,
    10_000_000,
]

# set max value in each array
max_value = 10000000

# Fix seed for reproducibility
seed = 42

def generate_dataset(n, seed = seed):
    random.seed(seed)
    return [random.randint(1, max_value) for _ in range(n)]

def save_dataset(data, n):
    filepath = f"datasets/data_{n}.txt"
    with open(filepath, "w") as f:
        for value in data:
            f.writelines(f"{value}\n")

def generate_all_datasets():
    for n in sizes:
        data = generate_dataset(n)
        save_dataset(data, n)
        print(f"Generated dataset of size {n}")

if __name__ == "__main__":
    generate_all_datasets()
