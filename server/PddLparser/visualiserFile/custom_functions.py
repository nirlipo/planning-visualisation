"""This module contain all the customer funtion we designed to help position the objects"""

__all__ = ['init_space', 'distributex']

def init_space(size):
    """The funtion initialise an space for distributex function
    Args:
        size(int): the max number of item in space
    Returns:
        space: an array of integer
    """
    space = []
    for i in range(size):
        space.append(i)
    return space


def distributex(obj, space, spacebtw, width, remove):
    """The function return the x location of object of an given space"""
    if not remove:
        if obj in space:
            objindex = space.index(obj)
            return objindex * (width + spacebtw)
        else:
            for num, value in enumerate(space):
                if num == value:
                    space[num] = obj
                    return num * (width + spacebtw)
    else:
        if obj in space:
            objindex = space.index(obj)
            space[objindex] = objindex
            return True
    return False
