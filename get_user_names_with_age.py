def get_user_names_with_age(data:list, age:int) -> list:
    """
    Return a list of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        list: A list of users with the given age
    """
    a=''
    for i in data:
        if i['age']==age:
            a=i['name']
        
    return a
age=int(input('How old is unknown object>>>>'))
data = [
  {
    'name': 'John', 
    'age': 27
  }, 
  {
    'name': 'Mary', 
    'age': 42
  }
]
print(get_user_names_with_age(data,age))
