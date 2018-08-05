"""This module is designed to help with getting a list of steps for Step3 to use"""
import re
import sys


# This python file aims to finish step 3 in our solution
#######################################################
# Input File: api file
# Input File: problem file
# Input File: solution file
# Output : predicates for all stages
#######################################################

#######################################################
# This function is designed to remove all the redundant characters
# for each action in the action list, so that the action can be directly used.
def remove_unused_char(action_list):
    """The function is to remove all the useless characters from api file.
        Args:
            action_list: an array of actions.
        Returns:
            clean_action_list: a cleaned action list.
    """
    clean_action_list = []
    for action in action_list:
        effect_element = action['action']
        clearnedstr = (effect_element[effect_element.index("effect")
                                      + len("effect"):])
        clean_action_list.append(clearnedstr[:-1])
    return clean_action_list


#######################################################
# Main function for getting the predicates for each stage
def get_stages(plan, problem_dic, problem_file):
    """The function is to get the list of steps for Step3 to use
        Args:
            plan: solution file
            problem_dic: problem dictionary contains the initial and goal stages
            problem_file: problem file name
        Returns:
            a list of steps containing information about all stages
    """
    #print(plan)

    # Initial stage
    stages = problem_dic[0]['init'].copy()
    text = problem_file
    
    objects = re.findall(r'\b\S+\b', text[text.index("objects")
                                              + len("objects"):text.index("init")])
    # Getting the list of actions from results returned from planning.domain api
    try:
        actionlist = plan['result']['plan']
    except KeyError:
        sys.exit("No plan have been returned")
    cleanactionlist = remove_unused_char(actionlist)

    # stages = []
    # for var in initstage:
    #    stages.append(var)

    # Patterns that will be used for matching
    # otpattern is for predicate on-table and etc...
    otpattern = re.compile(r'on-table\s\w')
    clpattern = re.compile(r'clear\s\w')
    onpattern = re.compile(r'on\s\w\s\w')
    afpattern = re.compile(r'arm-free')
    ahpattern = re.compile(r'holding\s\w')

    #######################################################
    # This for-loop will extract all the predicates and place them into a stage json list
    # 1. Find all the related predicates by using findall function for each stage
    # 2. Compare the current stage with the previous stage to get all the added actions
    #    and removed actions
    # 3. Append the result obtained from step 2 here to a output variable - content
    # 4. Repeatedly doing step 1 to step 3 here till the api solution has been digested
    content = {"stages": [], "objects": objects}
    content['stages'].append({"items": stages.copy()})
    # 1.
    for counter in range(0, len(actionlist)):
        checklist = []
        otname = otpattern.findall(cleanactionlist[counter])
        clname = clpattern.findall(cleanactionlist[counter])
        onname = onpattern.findall(cleanactionlist[counter])
        afname = afpattern.findall(cleanactionlist[counter])
        ahname = ahpattern.findall(cleanactionlist[counter])

        # Search for all the predicates in the provided strings
        for predicateot in otname:
            data_object = {"name": predicateot.split()[0], "objectNames": []}
            data_object["objectNames"].append(predicateot.split()[1])
            checklist.append(data_object)
        for predicatecl in clname:
            data_object = {"name": predicatecl.split()[0], "objectNames": []}
            data_object["objectNames"].append(predicatecl.split()[1])
            checklist.append(data_object)
        for predicateon in onname:
            data_object = {"name": predicateon.split()[0], "objectNames": []}
            data_object["objectNames"].append(predicateon.split()[1])
            data_object["objectNames"].append(predicateon.split()[2])
            checklist.append(data_object)
        for predicateaf in afname:
            data_object = {"name": predicateaf.split()[0]}
            if len(predicateaf) > 8:
                if predicateaf.split()[1] is None:
                    data_object["objectNames"] = ["No objects"]
                else:
                    data_object["objectNames"] = []
                    data_object["objectNames"].append(predicateaf.split()[1])
            else:
                data_object["objectNames"] = ["No objects"]
            checklist.append(data_object)
        for predicateah in ahname:
            data_object = {"name": predicateah.split()[0], "objectNames": []}
            data_object["objectNames"].append(predicateah.split()[1])
            checklist.append(data_object)

        # 2.
        addactionlistarr = []
        removeactionlistarr = []
        for var in checklist:
            if var in stages:
                removeactionlistarr.append(var)
            else:
                addactionlistarr.append(var)

        # Append the list to get the final result
        for addvar in addactionlistarr:
            stages.append(addvar)
        for rmvar in removeactionlistarr:
            stages.remove(rmvar)

        # 3.
        # Append everything to get the final output - content
        result = {"items": stages.copy(),
                  "add": addactionlistarr,
                  "remove": removeactionlistarr}
        content['stages'].append(result)
    return content
