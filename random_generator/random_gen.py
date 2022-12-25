import random
import logging

from random_generator.exceptions import RandomGenInputInvalidException

## basic logging setup
logging.basicConfig(
    level=logging.WARN,
    format='%(asctime)s %(name)s %(levelname)s:%(message)s',
)
logger = logging.getLogger(__name__)

class RandomGen(object):
    ## Class variables

    # set of numbers to sample from
    _random_nums = []
    # set of probabilites for corresponding numbers
    _probabilities = []

    def __init__(self):
        return

    def next_num(self)-> int:
        """
        Returns one of the randomNums. When this method is called multiple times over a long period, it should return the numbers roughly with the initialized probabilities.
        """ 

        ## pseudo-random number generated uniform distribution 0-1
        random_val = random.random()
        
        ## variable to store output
        next_random_num = None

        ## bin lower bound is initially set to 0
        curr_bin_lower_bound = 0

        ## iterating over probabilities to identify bin
        for idx, probab in enumerate(self.probabilities):

            if random_val < curr_bin_lower_bound + probab:
                ## bin identified, update answer and break
                if idx < len(self.random_nums):
                    next_random_num = self.random_nums[idx]
                break

            ## current bin is wrong, update lower bound of bin
            curr_bin_lower_bound += probab
        
        ## loop terminated, but no answer found, default to None
        if next_random_num is None:
            logger.warn(f"No matching bin found for value {random_val}, returning None")

        return next_random_num

    def validate_probabilites(self, probabilities: list=[])-> None:

        ## incase of clearing input, sum and negative input validation tests are not applicable
        if len(probabilities) == 0:
            logging.info("Resetting probability distribution values")
            return

        ## summing values in probabilities for validation
        sum = 0
        for _, val in enumerate(probabilities):

            ## sign validation : no probability can be negative
            if val < 0:
                raise RandomGenInputInvalidException(f"Received negative probability as input : {val}")
            sum += val

        ## sum validation : sum of probability list should be 1        
        if abs(sum - 1) > 1e-4:
            raise RandomGenInputInvalidException(f"Given probabilities sum up to :{sum}, and not expected value (1)")
        return

    ## Basic setter getter functions
    @property
    def random_nums(self):
        return self._random_nums
    
    @property
    def probabilities(self):
        return self._probabilities

    @random_nums.setter
    def random_nums(self, random_nums: list=None):
        self._random_nums = random_nums

    @probabilities.setter
    def probabilities(self, probabilities: list=None):
        ## Validate probabilities input before setting
        self.validate_probabilites(probabilities=probabilities)
        self._probabilities = probabilities
