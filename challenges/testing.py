"""
Your company needs a function that meets the following requirements:
  * For a given array of n integers, the function returns the index of the element with the minimum value in the array. 
    If there is more than one element with the minimum value, the returned index should be the smallest one.
  * If an empty array is passed to the function, it should raise an Exception.
  
Your task is to implement 3 classes that will produce test data and the expected results for the testing functions:
  * get_array() method in class TestDataEmptyArray has to return an empty array.
  * get_array() method in class TestDataUniqueValues has to return an array of size at least 2 with all unique elements, 
    while method get_expected_result() of this class has to return the expected minimum value index for this array.
  * get_array() method in class TestDataExactlyTwoDifferentMinimums has to return an array where there are exactly 
    two different minimum values, while method get_expected_result() of this class has to return the expected minimum 
    value index for this array.
"""

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
    
class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        return [5, 8, 2, 3, 1, 9]

    @staticmethod
    def get_expected_result():
        return 4

class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        return [8, 7, 2, 1, 6, 1]

    @staticmethod
    def get_expected_result():
        return 3
