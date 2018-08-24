"""This module is designed to help with initialising the given objects"""

import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/../" +"predicate_solver"))
import random_color

# This component is used to initialise the environment and objects for Predicate Solver
# This is the preprocess for Predicate Solver
#######################################################
# Input File: A randomly selected color
# Output : A list of custom objects
#######################################################

def initialise_objects(object_list, animation_profile):
    """ This function initialise objects in the animation profile
    Args:
        object_list(List): the list to store all objects.
        animation_profile(Dictionary): the dict to store all information in animation profile.
    Returns:
        unsolved_objects(Dictionary): the objects that are not initialised.
    """
    unsolved_objects = {}

    predefine_objects = {}
    for predefine_type in animation_profile["objects"]["predefine"]:
        for objects in animation_profile["objects"]["predefine"][predefine_type]:
            predefine_objects[objects] = predefine_type

    for objectname in object_list:
        unsolved_objects[objectname] = {}
        if objectname in predefine_objects:
            obj_type = predefine_objects[objectname]
        else:
            obj_type = animation_profile["objects"]["default"]
        # update the value for each
        for objproperty in animation_profile["shape"][obj_type]:
            value = animation_profile["shape"][obj_type][objproperty]
            if value is not False:
                if value == "randomcolor":
                    unsolved_objects[objectname][
                        objproperty] = random_color.get_random_color()
                    continue
                unsolved_objects[objectname][objproperty] = value
            else:
                unsolved_objects[objectname][objproperty] = False
        unsolved_objects[objectname]["name"] = objectname
    return unsolved_objects