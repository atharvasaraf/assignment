from random_generator import RandomGen
from example_config import RANDOM_NUMS, PROBABILITIES

def example_random_generation():
    
    randomizer_obj = RandomGen()
    randomizer_obj.random_nums = RANDOM_NUMS
    randomizer_obj.probabilities = PROBABILITIES
    counts = {x:0 for x in RANDOM_NUMS}

    number_to_index_map = {RANDOM_NUMS[x]:x for x in range(len(RANDOM_NUMS))}
    iterations = 100000

    for _ in range(iterations):
        num = randomizer_obj.next_num()
        counts[num] += 1
    
    divergence = {}
    for num, actual_occurence in counts.items():
        expected_occurence = PROBABILITIES[number_to_index_map[num]]* iterations
        div_for_num = abs(expected_occurence - actual_occurence)*100 / expected_occurence
        divergence[num] = div_for_num
    
    print(f"Input Numbers:")
    print(RANDOM_NUMS)

    print(f"Probabilites: ")
    print(PROBABILITIES)

    print(f"After {iterations} iterations occurence of numbers:")
    print(counts)

    print(f"Divergence (%) from expected for numbers:")
    print(divergence)

if __name__ == "__main__":
    example_random_generation()