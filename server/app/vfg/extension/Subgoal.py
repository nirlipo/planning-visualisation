"""This component generate the subgoal data"""
#-----------------------------Authorship-----------------------------------------
#-- Authors  : Ella
#-- Group    : Planning Visualisation
#-- Date     : 5/Oct/2018
#-- Version  : 1.0
#--------------------------------------------------------------------------------
#-----------------------------Reviewer-------------------------------------------
#-- Authors  : Yi Ding
#-- Group    : Planning Visualisation
#-- Date     : 5/Oct/2018
#-- Version  : 1.0
#--------------------------------------------------------------------------------


def get_subgoal(stages,final_goal,actionlist):
    stepNum = []
    stepindex = 1;
    # define subgoals dict
    subgoals = []
    finalstage = final_goal
    action_name_list = []
    for counter in range(0, len(actionlist)):
        action_name = get_action_name(actionlist[counter]['action'])
        action_name_list.append(action_name)

        # predicate in each step
    for a in stages:
        # predicate in final step

        if a["stageName"] != "Initial Stage":

            for item in a["items"]:
                if item in finalstage:
                    str = "(" + item["name"] + " "
                    for name in item["objectNames"]:
                        str = str + name + " "

                    str += ")"
                    objectlist = item["objectNames"]
                    stepNum.append(stepindex)
                    stepNames = action_name_list[stepindex - 1]
                    # print(stepNames)
                    # sub = {"name": str, "stepNum": stepindex, "stepName": action_name, "objects": objectlist}
                    sub = {"name": str, "stepNum": stepindex, "stepName": stepNames, "objects": objectlist}

                    subgoals.append(sub)
            stepindex = stepindex + 1
    return subgoals

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