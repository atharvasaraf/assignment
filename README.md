# Random Number Generator Homework Assignment

## Approach
Given that I am allowed to use `random.random` which uniform randomly samples a number between [0-1)
The region [0-1) has been divided into n-bins, where n is the total number of possible outcomes.
Each bin is of size equal to that particular outcome's probability

When method `RandomGen.next_num` is called, I sample a number(`random_val`) between [0-1) using `random.random`. I then identify the index of the bin to which `random_val` belongs. This index is identified by performing a binary search, using the `bisect.bisect` function on the cumulative sum of probabilites. The outcome corresponding to this index in the list of possible outcomes is then returned as the sampled outcome.

As a pre-processing step, I compute and store the cumulative sum of probabilities from the list of probabilities passed. This reduces lookup time-complexity for identifying the bin to O(log(n)). This step can be omitted and the bin could be identified on-the-fly, which will result in increased time-complexity O(n).

## File Structure
Standard python structure :
```
assignment_atharva_saraf
│   README.md
│   setup.py    
│   requirements.txt    
│   .gitignore    
│   example_config.py(sample config)
│   example.py (sample file)
│
│
└───venv (virutal env folder)
│ 
│  
└───random_generator (src)
│       random_gen.py
│       exceptions.py
│   
│   
└───tests (testing)
        test_random_gen.py
```
## Running Example and Tests

### Virtual Environment:
- Option 1 : use existing env 
    >`source venv/bin/activate`

- Option 2 : create new env and activate
    > `python3 -m venv {new_env_name}`  
    > `source {new_env_name}/bin/activate`

- Install dependency : 
    > `cat requirements.txt | xargs pip install`
- Above step is redundant if using option 1 (requirements are already installed)

### Running example
- from within environment run 
    > `python example.py`

### Running Tests
- from within environment run 
    > `pytest -v`

## Tests
1) Input validation for list of probabilities
    - Test checks for exception when probabilities do not sum upto 1
    - Test checks for exception if a negative probability is passed

2) Output distribution check
    - Test is set up to collect 100,000 samples from `RandomGen.next_num` and compute the % difference between the ideally expected frequency of outcomes and realised frequency of outcome for every possible outcome. The test then ensures that this difference is less than a threshold value for every outcome. Since this tests the behaviour of a random number generator, this test should be run with a seed value.

## Assumptions
The following assumptions have been made during development:
1) The length of the lists (possible outcomes & corresponding probabilities) are equal
2) The sum of probabilites given will be equal to 1
3) No negative probabilities will be given as input

The behaviour of the code will diverge from expectation if the above assumptions do not hold.
Input validation has been done to raise exceptions for the last two assumptions