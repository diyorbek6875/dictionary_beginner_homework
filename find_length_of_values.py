def find_length_of_values(data: dict) -> int:
    """
    Return the sum of the length of all values in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The sum of the length of all values in the dictionary.
    """
    a=''
    for i in data.values():
        a=a+str(i)
    return len(a)
data = { 
    'a': 'abc',
    'b': 'def', 
    'c': 'ghi'
  }
print(find_length_of_values(data))