import pytest

from random_generator.random_gen import RandomGen
from random_generator.exceptions import RandomGenInputInvalidException

class TestRandomGen(object):
    ## Simple fixture setup for tests
    random_nums_input = [-1, 0, 1, 2, 3]
    probabilities_input = [0.01, 0.3, 0.58, 0.1, 0.01]
    randomizer_obj = RandomGen()
    
    def test_next_num_output_valid(self):
        ## Test to ensure that output does not contain numbers not in random_nums_input

        ## Setup random numbers and their respective probabilities
        self.randomizer_obj.random_nums = self.random_nums_input
        self.randomizer_obj.probabilities = self.probabilities_input
        
        ## Iterate and call next_num 10000, recording the frequency of output in dictionary
        output_freq = {}
        for _ in range(10000):
            output = self.randomizer_obj.next_num()
            if output not in output_freq:
                output_freq[output] = 0
            output_freq[output] += 1
        
        ## Identify those outputs that were not expected
        wrong_outputs = [x for x in output_freq if x not in self.random_nums_input]
        assert len(wrong_outputs) == 0
        
    def test_distribution_of_inputs(self):
        ## Test to ensure that the maximum divergence % for n-iterations is less that threshold
        ## seed should be set in this case

        ## Setup random numbers and their respective probabilities
        self.randomizer_obj.random_nums = self.random_nums_input
        self.randomizer_obj.probabilities = self.probabilities_input
        
        ## temporary required variables 
        number_to_index_map = {self.random_nums_input[x]:x for x in range(len(self.random_nums_input))}
        no_of_iterations = 100000

        ## setting seed
        import random
        random.seed(1)
        
        ## perform iterations and record frequency of output numbers
        output_freq = {}
        for _ in range(no_of_iterations):
            output = self.randomizer_obj.next_num()
            if output not in output_freq:
                output_freq[output] = 0
            output_freq[output] += 1
        
        ## calculate divergence from expected frequency of output
        divergence = {x:0 for x in self.random_nums_input}
        for num, actual_occurence in output_freq.items():
            expected_occurence = self.probabilities_input[number_to_index_map[num]]* no_of_iterations
            div_for_num = abs(actual_occurence - expected_occurence) / expected_occurence
            divergence[num] = div_for_num
        
        ## identify those outputs, whose divergence exceeds threshold
        outlier_outputs = []
        MAX_DIVERGENCE_THRESHOLD = 0.04
        for num, div in divergence.items():
            if div >= MAX_DIVERGENCE_THRESHOLD:
                outlier_outputs.append(num)
        assert len(outlier_outputs) == 0

    def test_invalid_inputs(self):
        ## Test to ensure exceptions are raised on passing wrong probabilites as input

        ## No negative probability
        negative_probability_distribution = [0.01, 0.3, 0.58, 0.1, -0.01]            
        with pytest.raises(RandomGenInputInvalidException) as _:
            self.randomizer_obj.probabilities = negative_probability_distribution
        
        ## sum of probability list passed should be 1
        wrong_probability_distribution = [0.01, 0.3, 0.38, 0.1, -0.01]
        with pytest.raises(RandomGenInputInvalidException) as _:
            self.randomizer_obj.probabilities = wrong_probability_distribution
        
        return