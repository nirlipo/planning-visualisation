"""This module is designed to help with getting a list of predicates for INIT and GOAL states"""

#-----------------------------Authorship-----------------------------------------
#-- Authors  : Gang CHEN
#-- Group    : Planning Visualisation
#-- Date     : 13/August/2018
#-- Version  : 1.0
#--------------------------------------------------------------------------------
#-----------------------------Reviewer-------------------------------------------
#-- Authors  : Sharukh
#-- Group    : Planning Visualisation
#-- Date     : 23/August/2018
#-- Version  : 1.0
#--------------------------------------------------------------------------------
import re
# This python file aims to finish step 3 in our solution
#######################################################
# Input File: domain file
# Output : predicates for INIT stage and GOAL stage
#######################################################

def get_object_list(predicates_lists,str_init):
    init_condition = []
    for k, v in predicates_lists.items():
        temp_pattern = re.compile("\(" + v)
        pattern_subelements = temp_pattern.findall(str_init)
        if(pattern_subelements):
            number_of_objects = len(pattern_subelements[0].split()) - 1
            for val in pattern_subelements:
                data_object = {"name": k.replace(" ", ""), "objectNames": []}
                if(number_of_objects > 0):
                    for x in range(0, number_of_objects):
                        data_object["objectNames"].append(val.split()[x+1])
                else:
                    data_object["objectNames"] = ["No objects"]
                init_condition.append(data_object)
    return init_condition

def get_regex_list(predicates_lists):
    for k, v in predicates_lists.items():
        regular_expression = k.replace(" ", "")
        for x in range(0, v):
            regular_expression += "\s[\w\-]+"
        predicates_lists[k] = regular_expression

def get_problem_json(file_name, predicates_lists):
    """The function will parse the problem pddl and get the Initial predicates and
    and goal predicates for Step2 to use.
        Args:
            file_name()String: domain file name.
        Returns:
            result(Dictionary): a dictionary contains INIT and GOAL states(predicates).
    """
    # Prepare REGEX for each predicate
    try:
        get_regex_list(predicates_lists)
    except:
        raise ValueError("Empty string found")


    # Read input file
    str_file = file_name

    # Get INIT
    str_init = str_file[str_file.index("init") + len("init"):str_file.index("goal")]
    init_object_list = get_object_list(predicates_lists,str_init)
    init_data_object = {"init": init_object_list}

    # Get GOAL
    str_goal = str_file[str_file.index("goal"):]
    goal_object_list = get_object_list(predicates_lists, str_goal)
    goal_data_object = {"goal": goal_object_list, "goal-condition": ["and"]}

    # Get Result
    result = []
    result.append(init_data_object)
    result.append(goal_data_object)
    return result