# import sys
#
# print(sys.version.split()[0])
#
# countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
# is_italy = 'ITA' in countries
#
# # Enter your solution here
# assert is_italy, "ITA"


def max_min_diff(numbers):
    """
    Calculates the difference between the maximum and minimum number
    in the given list.

    :param numbers: A list of numbers.
    :return: The difference between the maximum and minimum number
    in the list.
    :raises ValueError: If the list is empty.
    """
    # Enter your solution here
    assert len(numbers) != 0, "the list cannot be empty"
    return max(numbers) - min(numbers)


# Enter your solution here
list1 = []
print(max_min_diff(list1))
