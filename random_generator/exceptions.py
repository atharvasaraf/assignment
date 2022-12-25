class RandomGenInputInvalidException(Exception):
    def __init__(self, message="Input given invalid"):
        super().__init__(message)
