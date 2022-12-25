import random
import logging
import bisect

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

    # additional list to store cummulative sum of probabilites
    _processed_cumsum_probab = []

    def __init__(self):
        return

    def next_num(self)-> int:
        """
        Returns one of the randomNums. When this method is called multiple times over a long period, it should return the numbers roughly with the initialized probabilities.
        """ 

        ## pseudo-random number generated uniform distribution 0-1
        random_val = random.random()
        
        ## binary search for idx of bin corresponding to random_val from cumsum_probab
        idx = bisect.bisect(self.processed_cumsum_probab, random_val)
        if idx >= len(self.random_nums):
            idx = len(self.random_nums) - 1

        next_random_num = self.random_nums[idx]
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

    def _calculate_cumsum(self, probabilites: list=[]):
        ## basic cummulative sum of probabilities list
        cumsum = [0]* len(probabilites)

        curr_cumsum = 0
        for idx, probab in enumerate(probabilites):
            curr_cumsum += probab
            cumsum[idx] = curr_cumsum
        return cumsum

    ## Basic setter getter functions
    @property
    def random_nums(self):
        return self._random_nums
    
    @property
    def probabilities(self):
        return self._probabilities

    @property
    def processed_cumsum_probab(self):
        return self._processed_cumsum_probab
    

    @random_nums.setter
    def random_nums(self, random_nums: list=None):
        self._random_nums = random_nums

    @probabilities.setter
    def probabilities(self, probabilities: list=None):
        ## Validate probabilities input before setting
        self.validate_probabilites(probabilities=probabilities)
        self._probabilities = probabilities

        ## calculate cumsum of probabilities and store
        self.processed_cumsum_probab = self._calculate_cumsum(probabilites=probabilities)
    
    @processed_cumsum_probab.setter
    def processed_cumsum_probab(self, cumsum_probab: list=None):
        self._processed_cumsum_probab = cumsum_probab
