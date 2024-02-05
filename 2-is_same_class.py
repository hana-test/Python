
def is_same_class(obj, a_class):
    """ This function compares the types of the inputs"""
    """Check if an object is exactly an instance of a given class.
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False

a = 0
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__)) #  accesses a class's name as a string.
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))
