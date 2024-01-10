import numpy as np

def mother_evaluation_old(dungeon, score_modifier, window_size, desired_sum):
    """
    Evaluate the dungeon array based on the described criteria.

    Parameters:
    - dungeon: NumPy array representing the dungeon layout.
    - score_modifier: The value to be added to the score when encountering a window of the desired sum.
    - window_size: Size of the convolution window.
    - desired_sum: The desired sum for the convolution window.

    Returns:
    - Score based on the evaluation criteria.
    """
    score = 0

    for i in range(dungeon.shape[0] - window_size + 1):
        for j in range(dungeon.shape[1] - window_size + 1):
            window_sum = np.sum(dungeon[i:i+window_size, j:j+window_size])

            if window_sum == desired_sum:
                score += score_modifier

    return score

# def mother_evaluation(dungeon, score_modifier, window_size, desired_sum):
#     """
#     Evaluate the dungeon array based on the described criteria.

#     Parameters:
#     - dungeon: NumPy array representing the dungeon layout.
#     - score_modifier: The value to be added to the score when encountering a window of the desired sum.
#     - window_size: Size of the convolution window.
#     - desired_sum: The desired sum for the convolution window.

#     Returns:
#     - Score based on the evaluation criteria.
#     """
#     # Create a rolling window view of the dungeon array
#     rolled_dungeon = np.lib.stride_tricks.sliding_window_view(dungeon, (window_size, window_size))

#     # Calculate the sum of each window
#     window_sums = np.sum(rolled_dungeon, axis=(2, 3))

#     # Count occurrences where the sum matches the desired_sum
#     matching_windows = np.count_nonzero(window_sums == desired_sum)

#     # Calculate the overall score
#     overall_score = matching_windows * score_modifier

#     return overall_score

def mother_evaluation(dungeons, score_modifier, window_size, desired_sum):
    """
    Evaluate an array of dungeons based on the described criteria.

    Parameters:
    - dungeons: NumPy array of shape (n, w, w) representing multiple dungeon layouts.
    - score_modifier: The value to be added to the score when encountering a window of the desired sum.
    - window_size: Size of the convolution window.
    - desired_sum: The desired sum for the convolution window.

    Returns:
    - NumPy array of scores based on the evaluation criteria for each dungeon.
    """
    
    if len(dungeons.shape) == 2:
        dungeons = dungeons[np.newaxis, ...]
    
    # Create a rolling window view of the dungeons array
    rolled_dungeons = np.lib.stride_tricks.sliding_window_view(dungeons, (1, window_size, window_size))

    # Calculate the sum of each window for all dungeons
    window_sums = np.sum(rolled_dungeons, axis=(3, 4, 5))


    # Count occurrences where the sum matches the desired_sum for each dungeon
    matching_windows = np.count_nonzero(window_sums == desired_sum, axis=(1,2))

    # Calculate the overall scores for each dungeon
    overall_scores = matching_windows * score_modifier

    return overall_scores

def evaluator_creator(n, max_dungeon_width, count_wall=False):
    desired_sum = 0 if not count_wall else n**2
    
    def evaluator(dungeon):
        """
        Evaluate the dungeon array based on the described criteria.

        Parameters:
        - dungeon: NumPy array representing the dungeon layout.
        - desired_sum: The desired sum for the convolution window (default is 4).

        Returns:
        - Score based on the evaluation criteria.
        """
        return mother_evaluation(dungeon, score_modifier=calculate_score_modifier(n, max_dungeon_width), window_size=n, desired_sum=desired_sum)

    return evaluator

def overall_evaluation(dungeon):
    """
    Calculate the overall score from all evaluated functions.

    Parameters:
    - dungeon: NumPy array representing the dungeon layout.

    Returns:
    - Overall score calculated from all evaluated functions.
    """


    overall_score = 0 # TODO

    return overall_score


# overall_score = overall_evaluation_function(mutated_dungeon)



# # Evaluate the score for the first dungeon layout
# score1 = evaluate_function1(mutated_dungeon)
# score2 = evaluate_function2(mutated_dungeon)
# score3 = evaluate_function3(mutated_dungeon)
# score4 = evaluate_function4(mutated_dungeon)
# score5 = evaluate_function5(mutated_dungeon)
# plot_dungeon(mutated_dungeon)
# score1, score2, score3, score4, score5, ' = ', overall_score




# # time comparison of the evaluation mothers

# import timeit
# import numpy as np

# # Original version with for loops
# def original_evaluation_function(dungeon, score_modifier, window_size, desired_sum):
#     score = 0

#     for i in range(dungeon.shape[0] - window_size + 1):
#         for j in range(dungeon.shape[1] - window_size + 1):
#             window_sum = np.sum(dungeon[i:i+window_size, j:j+window_size])

#             if window_sum == desired_sum:
#                 score += score_modifier

#     return score

# # Revised version using NumPy array operations
# def revised_evaluation_function(dungeon, score_modifier, window_size, desired_sum):
#     rolled_dungeon = np.lib.stride_tricks.sliding_window_view(dungeon, (window_size, window_size))
#     window_sums = np.sum(rolled_dungeon, axis=(2, 3))
#     matching_windows = np.count_nonzero(window_sums == desired_sum)
#     overall_score = matching_windows * score_modifier

#     return overall_score

# # Example usage
# num_samples = 5
# random_dungeons = generate_random_samples(num_samples)

# # Measure execution time for the original version
# original_time = timeit.timeit(lambda: original_evaluation_function(random_dungeons[0], score_modifier=2, window_size=3, desired_sum=0), number=1000)

# # Measure execution time for the revised version
# revised_time = timeit.timeit(lambda: revised_evaluation_function(random_dungeons[0], score_modifier=2, window_size=3, desired_sum=0), number=1000)

# print(f"Original version time: {original_time} seconds")
# print(f"Revised version time: {revised_time} seconds")

def calculate_score_modifier(n, max_dungeon_width):
    pass  # TODO