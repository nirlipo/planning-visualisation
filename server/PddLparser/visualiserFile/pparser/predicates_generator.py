"""This module is designed to help with getting a list of steps for Step3 to use"""
import re
import sys
import server.PddLparser.visualiserFile.pparser.problem_parser

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
def get_stages(plan, problem_dic, problem_file, predicates_list):
    """The function is to get the list of steps for Step3 to use
        Args:
            plan: solution file
            problem_dic: problem dictionary contains the initial and goal stages
            problem_file: problem file name
        Returns:
            a list of steps containing information about all stages
    """

    # Initial stage
    stages = problem_dic[0]['init'].copy()

    with open(problem_file) as file:
        text = file.read()
        objects = re.findall(r'\b\S+\b', text[text.index("objects")
                                              + len("objects"):text.index("init")])

    # Getting the list of actions from results returned from planning.domain api
    try:
        actionlist = plan['result']['plan']
    except KeyError:
        sys.exit("No plan have been returned")
    cleanactionlist = remove_unused_char(actionlist)

    content = {"stages": [], "objects": objects}
    content['stages'].append({"items": stages.copy()})
    # 1. Go through the steps
    for counter in range(0, len(actionlist)):
        checklist = []
        init_object_list = server.PddLparser.visualiserFile.\
            pparser.problem_parser.\
            get_object_list(predicates_list, cleanactionlist[counter])
        checklist = (init_object_list)

        # 2. Find the difference between 2 steps
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
