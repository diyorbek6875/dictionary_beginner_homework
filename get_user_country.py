def get_user_country(data:list, name:str) -> list:
    """
    Return the country of a user with a given name

    Args:
        data (dict): A dictionary of values
        name (str): The name of the user to search for
    Returns:
        str: The country of the user with the given name
    """
    
    b=''
    for i in data:
        if i['name']==name:
            b=i['country']
    return b
data = [
  {
    'name': 'John', 
    'country': 'USA'
  }, 
  {
    'name': 'Mary', 
    'country': 'UK'
  },
  {
    'name': 'Henry', 
    'country': 'UK'
  },
  {
    'name': 'Sam', 
    'country': 'MEX'
  },
  {
    'name': 'Kevin', 
    'country': 'RUS'
  },
  {
    'name': 'Dustin', 
    'country': 'GER'
  }
]
name=input('Say my name   ')
print(get_user_country(data,name))