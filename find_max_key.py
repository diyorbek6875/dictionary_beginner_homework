def find_max_key(data: dict):
    """
    Return the maximum int or float key in a dictionary.
    Args:
        data (dict): A dictionary of values
    Returns:
        int: The maximum key in the dictionary.
    """
    q=0
    for i in data.keys():
        if q<i:
            q=i
    return q

data = {
    78: 'a', 
    2745: 'b', 
    7557: 'c'
  }
print(find_max_key(data))
