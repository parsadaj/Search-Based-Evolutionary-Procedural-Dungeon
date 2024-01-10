import numpy as np
from scipy.ndimage import binary_closing, binary_opening


def apply_mutation1(dungeon, stride=1, window_size=2):
    """
    Apply mutation operation 1 to the dungeon array using a 2 by 2 convolutional operator.
    mutation operation 1 frees some space from the random noise.

    Parameters:
    - dungeon: NumPy array representing the original dungeon layout.

    Returns:
    - Updated NumPy array representing the modified dungeon layout.
    """
    updated_dungeon = np.zeros_like(dungeon)

    for i in range(0, dungeon.shape[0], stride):
        for j in range(0, dungeon.shape[1], stride):
            window_sum = np.sum(dungeon[i:i+window_size, j:j+window_size])

            # if only there is one wall there, remove it
            if window_sum == 1:
                updated_dungeon[i:i+window_size, j:j+window_size] = 0
            elif window_sum == 3:
                updated_dungeon[i:i+window_size, j:j+window_size] = 1
            else:
                updated_dungeon[i:i+window_size, j:j+window_size] = dungeon[i:i+window_size, j:j+window_size]

    return updated_dungeon


# # Apply mutation1 to the first dungeon layout
# mutated1_dungeon = apply_mutation1(sample_dungeon)
# plot_dungeon(mutated1_dungeon)

def apply_mutation2(dungeon, stride=3, window_size=5):
    """
    Apply mutation operation 2 to the dungeon array using a 6 by 6 convolutional operator.
    mutation operation 2 creates walls betweem large free spaces.

    Parameters:
    - dungeon: NumPy array representing the original dungeon layout.

    Returns:
    - Updated NumPy array representing the modified dungeon layout.
    """
    updated_dungeon = dungeon.copy()

    for i in range(0, dungeon.shape[0], stride):
        for j in range(0, dungeon.shape[1], stride):
            window_sum = np.sum(dungeon[i:i+window_size, j:j+window_size])

            # if its a big free space, randomply put walls on one of its sides
            if window_sum == 0:
             # Randomly choose one side (top, bottom, left, right)
                side = np.random.choice(['top', 'bottom', 'left', 'right'])

                if side == 'top' and i - 1 >= 0:
                    updated_dungeon[i-1:i+1, j:j+window_size] = 1
                elif side == 'bottom' and i + window_size < dungeon.shape[0]:
                    updated_dungeon[i+window_size-1:i+window_size+1, j:j+window_size] = 1
                elif side == 'left' and j - 1 >= 0:
                    updated_dungeon[i:i+window_size, j-1:j+1] = 1
                elif side == 'right' and j + window_size < dungeon.shape[1]:
                    updated_dungeon[i:i+window_size, j+window_size-1:j+window_size+1] = 1
                
    return updated_dungeon

# mutated2_dungeon = apply_mutation2(apply_mutation1(apply_mutation1(mutated1_dungeon)))
# plot_dungeon(mutated2_dungeon)

def apply_mutation3(dungeon, closing_size=2, opening_size=2):
    """
    Apply mutation operation 3 to the dungeon array using morphological closing and opening.

    Parameters:
    - dungeon: NumPy array representing the original dungeon layout.
    - closing_size: Size of the closing kernel (default is 3).
    - opening_size: Size of the opening kernel (default is 3).

    Returns:
    - Updated NumPy array representing the modified dungeon layout.
    """
    updated_dungeon = dungeon.copy()
    updated_dungeon = binary_closing(updated_dungeon, structure=np.ones((closing_size, closing_size)))
    updated_dungeon = binary_opening(updated_dungeon, structure=np.ones((opening_size, opening_size)))

    return updated_dungeon

# mutated3_dungeon = apply_mutation3(mutated2_dungeon)
# plot_dungeon(mutated3_dungeon)

# def update_dungeon(dungeon):
#     """
#     Update the dungeon array using mutation operations 1 and 2.

#     Parameters:
#     - dungeon: NumPy array representing the original dungeon layout.

#     Returns:
#     - Updated NumPy array representing the modified dungeon layout.
#     """
#     updated_dungeon = np.copy(dungeon)

#     # Perform mutation 1 randomly 1 or 2 times
#     mutation1_iterations = np.random.choice([1, 2])
#     for _ in range(mutation1_iterations):
#         updated_dungeon = apply_mutation1(updated_dungeon)

#     # Perform mutation 2 once
#     updated_dungeon = apply_mutation2(updated_dungeon)
    
#     # Perform mutation 3 once
#     # updated_dungeon = apply_mutation3(updated_dungeon)

#     return updated_dungeon


# # # Update the first dungeon layout
# # updated_dungeon = update_dungeon(sample_dungeon)
# # plot_dungeon(updated_dungeon)

# # dungeon = generate_random_samples(1)[0]
# # for i in range(50):
# #     if i % 5 == 0:
# #         print("Iteration: {}". format(i+1))
# #         print(print_dungeon(dungeon))
# #         print("-"*25)
# #         print()
        
# #     dungeon = update_dungeon(dungeon)
# # plot_dungeon(apply_mutation3(dungeon))

def mutate(dungeon):
    """
    Randomly apply one of the three mutation operations to the dungeon array.

    Parameters:
    - dungeon: NumPy array representing the original dungeon layout.

    Returns:
    - Updated NumPy array representing the modified dungeon layout.
    """
    mutation_type = np.random.choice([1, 2]) #, 3])

    if mutation_type == 1:
        return apply_mutation1(dungeon)
    elif mutation_type == 2:
        return apply_mutation2(dungeon)
    # elif mutation_type == 3:
    #     return apply_mutation3(dungeon)

# # Mutate the first dungeon layout
# mutated_dungeon = mutate(sample_dungeon)
# plot_dungeon(mutated_dungeon)