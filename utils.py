import numpy as np
import matplotlib.pyplot as plt

def generate_random_samples(n, rows=20, cols=20):
    """
    Generate n random dungeon layouts.

    Parameters:
    - n: Number of samples to generate
    - rows: Number of rows in the dungeon grid (default is 20)
    - cols: Number of columns in the dungeon grid (default is 20)

    Returns:
    - A NumPy array of size (n, rows, cols) representing random dungeon layouts.
    """
    samples = np.random.choice([0, 1], size=(n, rows, cols))
    return samples

# # Example usage:
# num_samples = 5
# random_dungeons = generate_random_samples(num_samples)
# print(random_dungeons.shape)  # Output: (5, 20, 20)

# sample_dungeon = random_dungeons[0]


def print_dungeon(dungeon):
    """
    Convert the dungeon layout to a string representation.

    Parameters:
    - dungeon: NumPy array representing the dungeon layout.

    Returns:
    - A string representation of the dungeon layout with '#' for walls and '.' for empty spaces.
    """
    dungeon_str = '\n'.join([' '.join(['#' if cell == 1 else '.' for cell in row]) for row in dungeon])
    return dungeon_str

# # Example usage:
# for idx, dungeon in enumerate(random_dungeons):
#     print(f"Sample {idx + 1}:\n{print_dungeon(dungeon)}\n")
#     break

def plot_dungeon(dungeon):
    """
    Plot the dungeon using Matplotlib without axis labels.
    
    Parameters:
    - dungeon: NumPy array representing the dungeon layout.
    """
    fig, ax = plt.subplots()
    ax.imshow(dungeon, cmap='Greys')
    ax.set_xticks([])
    ax.set_yticks([])
    # ax.axis('off')  # Turn off axis labels
    
    for spine in ax.spines.values():
        spine.set_edgecolor('white')
        spine.set_linewidth(2)
 
# plot_dungeon(sample_dungeon)