"""This module is designed to help with getting a list of predicates for INIT and GOAL states"""
import re
# This python file aims to finish step 3 in our solution
#######################################################
# Input File: domain file
# Output : predicates for INIT stage and GOAL stage
#######################################################
def get_problem_json(file_name):
    """The function will parse the problem pddl and get the Initial predicates and 
    and goal predicates for Step2 to use.
        Args:
            file_name()String: domain file name.
        Returns:
            result(Dictionary): a dictionary contains INIT and GOAL states(predicates).
    """
    otpattern = re.compile(r'on-table\s\w')
    clpattern = re.compile(r'clear\s\w')
    onpattern = re.compile(r'on\s\w\s\w')
    afpattern = re.compile(r'arm-free')
    ahpattern = re.compile(r'holding')
    andpattern = re.compile(r'and')

    
    strfile = file_name
    stinit = strfile[strfile.index("init") + len("init"):strfile.index("goal")]

    # Patterns that will be used for matching
    # otpattern is for predicate on-table and etc...
    ot_name = otpattern.findall(stinit)
    cl_name = clpattern.findall(stinit)
    on_name = onpattern.findall(stinit)
    af_name = afpattern.findall(stinit)
    ah_name = ahpattern.findall(stinit)



    #######################################################
    # This for-loop will extract all the predicates for INIT stage
    # 1. Find all the related predicates by using findall function
    # 2. Append the result obtained from step 1 here to a output variable
    goal_found = strfile[strfile.index("goal"):]
    goal_ot_name = otpattern.findall(goal_found)
    goal_cl_name = clpattern.findall(goal_found)
    goal_on_name = onpattern.findall(goal_found)
    goal_af_name = afpattern.findall(goal_found)
    goal_ah_name = ahpattern.findall(goal_found)
    goal_and_name = andpattern.findall(goal_found)

    init_data = []
    goal_data = []
    goal_condition = []
    result = []

    for val in goal_and_name:
        data_object = {"objectNames": []}
        data_object["objectNames"].append(val.split()[0])
        goal_condition.append(data_object)
    for predicateot in goal_ot_name:
        data_object = {"name": predicateot.split()[0], "objectNames": []}
        data_object["objectNames"].append(predicateot.split()[1])
        goal_data.append(data_object)
    for predicatecl in goal_cl_name:
        data_object = {"name": predicatecl.split()[0], "objectNames": []}
        data_object["objectNames"].append(predicatecl.split()[1])
        goal_data.append(data_object)
    for predicateon in goal_on_name:
        data_object = {"name": predicateon.split()[0], "objectNames": []}
        data_object["objectNames"].append(predicateon.split()[1])
        data_object["objectNames"].append(predicateon.split()[2])
        goal_data.append(data_object)
    for predicateaf in goal_af_name:
        data_object = {"name": predicateaf.split()[0]}
        if len(predicateaf) > 8:
            if predicateaf.split()[1] is None:
                data_object["objectNames"] = ["No objects"]
            else:
                data_object["objectNames"] = []
                data_object["objectNames"].append(predicateaf.split()[1])

        else:
            data_object["objectNames"] = ["No objects"]
        goal_data.append(data_object)
    for predicateah in goal_ah_name:
        data_object = {"name": predicateah.split()[0]}
        if len(predicateah) > 8:
            if predicateah.split()[1] is None:
                data_object["objectNames"] = ["No objects"]

            else:
                data_object["objectNames"] = []
                data_object["objectNames"].append(predicateah.split()[1])
        else:
            data_object["objectNames"] = ["No objects"]
        goal_data.append(data_object)

    #######################################################
    # This for-loop will extract all the predicates for INIT stage
    # 1. Find all the related predicates by using findall function
    # 2. Append the result obtained from step 1 here to a output variable
    goal_data_object = {"goal": goal_data, "goal-condition": goal_condition}
    for predicateot in ot_name:
        data_object = {"name": predicateot.split()[0], "objectNames": []}
        data_object["objectNames"].append(predicateot.split()[1])
        init_data.append(data_object)
    for predicatecl in cl_name:
        data_object = {"name": predicatecl.split()[0], "objectNames": []}
        data_object["objectNames"].append(predicatecl.split()[1])
        init_data.append(data_object)
    for predicateon in on_name:
        data_object = {"name": predicateon.split()[0], "objectNames": []}
        data_object["objectNames"].append(predicateon.split()[1])
        data_object["objectNames"].append(predicateon.split()[2])

        init_data.append(data_object)
    for predicateaf in af_name:
        data_object = {"name": predicateaf.split()[0]}
        if len(predicateaf) > 8:
            if predicateaf.split()[1] is None:
                data_object["objectNames"] = ["No objects"]
            else:
                data_object["objectNames"] = []
                data_object["objectNames"].append(predicateaf.split()[1])

        else:
            data_object["objectNames"] = ["No objects"]
        init_data.append(data_object)
    for predicateah in ah_name:
        data_object = {"name": predicateah.split()[0]}
        if len(predicateah) > 8:
            if predicateah.split()[1] is None:
                data_object["objectNames"] = ["No objects"]

            else:
                data_object["objectNames"] = []
                data_object["objectNames"].append(predicateah.split()[1])
        else:
            data_object["objectNames"] = ["No objects"]
        init_data.append(data_object)

    init_data_object = {"init": init_data}
    result.append(init_data_object)
    result.append(goal_data_object)
    return result
