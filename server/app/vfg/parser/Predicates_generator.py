"""This module is designed to help with getting a list of steps for Step3 to use"""
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
#-----------------------------Authorship-----------------------------------------
#-- Authors  : Sunmuyu Zhang
#-- Group    : Planning Visualisation
#-- Date     : 07/Septemeber/2018
#-- Version  : 2.0
#--------------------------------------------------------------------------------
#-----------------------------Reviewer-------------------------------------------
#-- Authors  : Sai
#-- Group    : Planning Visualisation
#-- Date     : 09/Septemeber/2018
#-- Version  : 2.0
#--------------------------------------------------------------------------------
import re
import sys
import os
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import Problem_parser

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
# This function is designed to return the action name of the current step
def get_action_name(current_step):
    """The function is to remove all the useless characters from api file.
        Args:
            current_step: an array of the current step.
        Returns:
            action_name: a cleaned action name.
    """
    # find the predicate name
    action = current_step[current_step.index("action")
                                      + len("action"):current_step.index(":parameters")].rstrip().replace(" ","")
    # find all the parameters followed by that object
    objects = current_step[current_step.index("parameters")
                                      + len("parameters"):current_step.index(":precondition")].rstrip()
    action_name = action + " " + objects
    return action_name


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
    objects = re.findall(r'\b\S+\b', problem_file[problem_file.index("objects")
                                              + len("objects"):problem_file.index("init")])

    finalstage = problem_dic[1]['goal'].copy()

    # Getting the list of actions from results returned from planning.domain api
    try:
        actionlist = plan['result']['plan']
        #print(actionlist)
    except KeyError:
        sys.exit("No plan has been returned")
    cleanactionlist = remove_unused_char(actionlist)

    # Adding initial stage
    content = {"stages": [], "objects": objects,"subgoals":[]}
    content['stages'].append({
        "items": stages.copy(),
        "add": "",
        "remove": "",
        "stageName": "Initial Stage",
        "stageInfo": "No Step Information"
        })

    for counter in range(0, len(actionlist)):
        init_object_list = Problem_parser.get_object_list(predicates_list, cleanactionlist[counter])
        checklist = (init_object_list)

        # 1. Find the difference between 2 steps
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

        # 2.
        # Get the action name of this step from the plan
        action_name = get_action_name(actionlist[counter]['action'])
        #print(action_name)


        # 4.
        # Get the step information about the current step
        # Replacing \n with \r\n in order to display it correctly
        step_info_with_padding = actionlist[counter]['action'].replace("\n", "\r\n")
        step_info = step_info_with_padding[step_info_with_padding.index("(:action"):]

        # 5.
        # Append everything to get the final output - content
        result = {"items": stages.copy(),
                  "add": addactionlistarr,
                  "remove": removeactionlistarr,
                  "stageName": action_name,
                  "stageInfo": step_info,
                  }

        content['stages'].append(result)



    return content


