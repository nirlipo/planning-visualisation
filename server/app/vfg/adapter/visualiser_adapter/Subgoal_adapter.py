"""This component transfer the subgoal data to the format that visualiser could accept"""
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
def generate_subgoal(subgoals):
    """This function transfers the subgoal structure into the final one
    """
    m_keys = []
    m_values = []
    for subgoal in dedupe(subgoals):
        m_keys.append(subgoal["name"])
        m_values.append(subgoal["objects"])
    subgoal_pool = {"m_keys": m_keys, "m_values": m_values}

    step_list = []
    values = []
    for subgoal in subgoals:
        if subgoal["stepNum"] not in step_list:
            step_list.append(subgoal["stepNum"])

    # print(step_list)
    for step in step_list:
        value = []
        for subgoal in subgoals:
            if subgoal["stepNum"] == step:
                value.append(subgoal["name"])
        values.append(value)
    pool_map = {"m_keys": step_list,"m_values":values}
    subgoal_transfer = {"subgoalPool": subgoal_pool,"subgoalMap": pool_map}
    # print(pool_map)
    return subgoal_transfer


# def generate_subgoal(subgoals):
#     """This function transfers the subgoal structure into the final one
#     """
#
#     subgoal_pool = []
#     for subgoal in dedupe(subgoals):
#         temp = {subgoal["name"]: subgoal["objects"]}
#
#         subgoal_pool.append(temp)
#     print(subgoal_pool)
#     step_list = []
#     for subgoal in subgoals:
#         if subgoal["stepNum"] not in step_list:
#             step_list.append(subgoal["stepNum"])
#
#     subgoal_map = []
#     for step in step_list:
#         value = []
#         for subgoal in subgoals:
#             if subgoal["stepNum"] == step:
#
#                 value.append(subgoal["name"])
#         temp = {step: value}
#         subgoal_map.append(temp)
#     subgoal_transfer = {"subgoalPool": subgoal_pool,"subgoalMap": subgoal_map}
#     return subgoal_transfer


#######################################################
# This function is designed to combine the subgoal
# with the same name into one dict.
def dedupe(items):
    """The function is to convert subgoal list into correct format
           Args:
               items: subgoal list
           Returns:
               subgoal list in correct format
       """
    seen = []
    result = []

    for item in items:
        if item["name"] not in seen:
            seen.append(item["name"])
    for se in seen:
        numlist = []
        namelist = []
        objectlist = []
        for item in items:
            if item["name"] == se:
                numlist.append(item["stepNum"])
                namelist.append(item["stepName"])
                objectlist = item["objects"]
        result.append({"name":se,"stepNum":numlist,"stepName": namelist,"objects":objectlist})

    return result
