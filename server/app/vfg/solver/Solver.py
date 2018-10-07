"""This module will compute the visulisation file by using the stages predicates and animation"""
#-----------------------------Authorship-----------------------------------------
#-- Authors  : Sai
#-- Group    : Planning Visualisation
#-- Date     : 13/August/2018
#-- Version  : 1.0
#--------------------------------------------------------------------------------
#-----------------------------Reviewer-------------------------------------------
#-- Authors  : Gang
#-- Group    : Planning Visualisation
#-- Date     : 27/August/2018
#-- Version  : 1.0
#--------------------------------------------------------------------------------
#-----------------------------Authorship-----------------------------------------
#-- Authors  : YD
#-- Group    : Planning Visualisation
#-- Date     : 16/September/2018
#-- Version  : 2.0
#--------------------------------------------------------------------------------
#-----------------------------Reviewer-------------------------------------------
#-- Authors  : Sai
#-- Group    : Planning Visualisation
#-- Date     : 17/September/2018
#-- Version  : 2.0
#--------------------------------------------------------------------------------
import json
import copy
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../' +"extension"))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' +"vfg/solver"))

import Custom_functions
import Initialise

# import pparser.predicates_generator  # Step3: manipulate the predicate for each step/stage

#######################################################
# Input File: the reuslt of Customer Function component
# Output : Visualisation Result
#######################################################

def check_rule_complete(predicate, objects_dic, predicates_rules):
    """This funtion will check whether the predicate can be solved.
    It will check all the referenced object value by using the predicates_rules,
    for example, (on a b) as an predicates, the animation rules will say to define
    the position of a, it must know b's x postion and y position first. If b's refereced
    value has not been defined, the check_rule_complete function will return false.

    Args:
        predicate(string): a predicate that need to be checked, eg.(on-table b).
        objects_dic(dictionary): the current objects dictionary that need to be solved.
        predicates_rules(dictinary): rules defined the animation rule for the predicates.
    Returns:
        True: if the predicate can be solved.
        False: if the predicate can not be solved.
    """
    
    pname = predicate["name"]
    predicate_rule = predicates_rules[pname]
    objects_list_ref=predicate_rule["objects"]
    objects = predicate["objectNames"]
    if "custom_obj" in predicate_rule:
        #addtional custom object not in the real pddl file
        custom_obj=predicate_rule["custom_obj"]
        #complete object list
        object_list=objects+custom_obj
        objects_list_ref=objects_list_ref+custom_obj
    else:
        object_list=objects
    obj_ref_dic=dict(zip(objects_list_ref,object_list))
    if "require" in predicate_rule:
        for obj_index in predicate_rule["require"]:
            for property in predicate_rule["require"][obj_index]:
                objectname=obj_ref_dic[obj_index]
                if objects_dic[objectname][property] is False:
                    return False
    return True


def applypredicates(predicate,
                    objects_dic,
                    predicates_rules,
                    gstate):
    """update the value of realated obj in the objects_dic by applying the animation rules.
    For example, (on-table a) will set the a's x value by using distributex function and a's
    y value to 0.
    Args:
        predicate(String): a predicate that need to be solved.
        objects_dic(dictionary): a objects dictionary that contain all the objects
                                 and its attributes.
        predicates_rules(dictionary):rules defined the animation rule for the predicates
        space(array): an array that will be used for distributex funtion, it remeber the current
                      obj that in the space.
    """
    pname = predicate["name"]
    predicate_rule=predicates_rules[pname]
    objects_list_ref=predicate_rule["objects"]
    #objects in the real pddl file
    objects = copy.deepcopy(predicate["objectNames"])
    if "custom_obj" in predicate_rule:
        #addtional custom object not in the real pddl file
        custom_obj=predicate_rule["custom_obj"]
        #complete object list
        object_list=objects+custom_obj
        objects_list_ref=objects_list_ref+custom_obj
    else:
        object_list=objects

    obj_ref_dic = dict(zip(objects_list_ref, object_list))
    for rulename in predicate_rule["rules"]:
        if "value" in predicate_rule[rulename]:
            rule = predicate_rule[rulename]
            left,propertyname=get_objname_property(rule["left"],obj_ref_dic)
            value = predicate_rule[rulename]["value"]
            if "function" in value:
                fproperty = value["function"]
                fname = fproperty["fname"]
                obj_indexs=fproperty["obj_indexs"]
                if "settings" in fproperty:
                    settings=fproperty["settings"]
                else:
                    settings={}
                state=gstate[fname]
                obj_list=[]
                for obj_index in obj_indexs:
                    objname=obj_ref_dic[obj_index]
                    obj_list.append({objname:objects_dic[objname]})
                objects_dic[left],gstate[fname] = Custom_functions.customf_controller(fname,obj_list,settings,state,False)
            elif "equal" in value:
                right_value = value["equal"]
                print(predicate_rule)
                if type(right_value) is not dict:
                    objects_dic[left][propertyname[0]] = right_value
                else:
                    if "r" in right_value:#for color
                        objects_dic[left][propertyname[0]] = right_value
                    else:
                        right_object,right_property=get_objname_property(right_value,obj_ref_dic)
                        objects_dic[left][propertyname[0]]=objects_dic[right_object][right_property]

            elif "add" in value:
                rightvalue = 0
                for additem in value["add"]:
                    if type(additem) is dict:

                        right_object,right_property = get_objname_property(additem,obj_ref_dic)
                        addvalue = objects_dic[right_object][right_property]
                        rightvalue += addvalue
                    else:
                        rightvalue += additem
                objects_dic[left][propertyname[0]] = rightvalue
        else:
            action=predicate_rule[rulename]["action"]
            if "function" in action:
                fproperty = action["function"]
                fname = fproperty["fname"]
                obj_indexs = fproperty["obj_indexs"]
                if "settings" in fproperty:
                    settings=fproperty["settings"]
                else:
                    settings={}
                state=gstate[fname]
                obj_list=[]
                for obj_index in obj_indexs:
                    objname=obj_ref_dic[obj_index]
                    obj_list.append({objname:objects_dic[objname]})

                key,value=Custom_functions.customf_controller(fname,obj_list,settings,state,False)
                objects_dic[key]=value
def get_objname_property(dictionary,obj_ref_dic):
    object_index, propertyname = list(dictionary.items())[0]
    objname = obj_ref_dic[object_index]
    return objname,propertyname


def solvepredicates(predicates, objects_dic, predicates_rules, space):
    """This function will pop an predicate from a list of predicates, and try to solve
    it, the predicate will be put back to the predicates list if it can not be solved at
    one turn. The funtion will return true if all the predicates has been solved.
    Args:
        predicates(list of String): a list of predicates that need to be solved.
        objects_dic(dictionary): a dictionary of objects that its attribtes has to be solved
        predicates_rules(dictonaru): animation rules of predictates.
        space(array):an array that will be used for distributex funtion, it remeber the current obj
              that in the space.

    """
    i=0
    while (predicates and i<2000):
        predicate = predicates.pop(0)
        if predicate["name"] not in predicates_rules:
            continue
        if check_rule_complete(predicate, objects_dic, predicates_rules):

            applypredicates(predicate, objects_dic, predicates_rules, space)
        else:
            if not predicates:  # if the last predicate can not be solved
                return False
            predicates.append(predicate)
        i+=1
    return True


def keysort(name,predicates_rules):
    """This funtion will return weight for each predicates, default 10(not important).
    """

    if name in predicates_rules:
        if "priority" in predicates_rules[name]:
            return predicates_rules[name]["priority"]
        else:
            return 10
    else:
        return 10
def priority(predicates,predicates_rules):
    """This funtion will return sorted predicates based on the priority point
    """
    return sorted(predicates, key=lambda k: keysort(k["name"],predicates_rules))


def solve_all_stages(stages, objects_dic, predicates_rules, space,actionlist,problem_dic):
    """This funtion will run through each stage which contains a list of predicates, solve the
    predictaes and get the solved visualistaion file.
    Args:
        stages(dictionary): a dictinonary which contain list of predicates
                            for different stages/steps.
        objects_dic(dictonary): a dictionary of objects which need to be solved.
        predicates_rules: animation rules for the predicates
        space(array):an array that will be used for distributex funtion, it remeber the current obj
              that in the space
    Returns:
        result: visualisation dictionary that contain the location of each object
                for different stages
    """
    result = {}
    result["visualStages"] = []
    result["subgoals"] = []
    stepNum = []
    stepindex = 1;
    # define subgoals dict
    subgoals = {"subgoals": []}
    finalstage = problem_dic[1]['goal'].copy()
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
                    # print(item)
                    str = "(" + item["name"] + " "
                    for name in item["objectNames"]:
                        str = str + name + " "

                    str += ")"
                    objectlist = item["objectNames"]
                    stepNum.append(stepindex)
                    stepNames = action_name_list[stepindex-1]
                    # print(stepNames)
                    # sub = {"name": str, "stepNum": stepindex, "stepName": action_name, "objects": objectlist}
                    sub = {"name": str, "stepNum": stepindex, "stepName": stepNames,  "objects": objectlist}

                    subgoals["subgoals"].append(sub)
            stepindex = stepindex + 1



    # print(subgoals)
    # print(dedupe(subgoals["subgoals"]))
    for stage in stages:

        stage_dic = {}
        object_dic_copy = copy.deepcopy(objects_dic)
        predicates = stage["items"]
        sorted_predicates=priority(predicates,predicates_rules)

        # For hanoi problem, reset each stage
        # For logistics problem, reset each stage
        for fname in space["reset_function"]:
            space[fname]={}
        solvepredicates(sorted_predicates, object_dic_copy, predicates_rules, space)
        stage_dic["visualSprites"] = object_dic_copy
        if "stageName" not in stage:
            stage_dic["stageName"]="Inital Stage"
            stage_dic["stageInfo"]="No step information"

        else:
            stage_dic["stageName"]=stage["stageName"]
            stage_dic["stageInfo"]=stage["stageInfo"]


        result["visualStages"].append(stage_dic)

    result["subgoals"] = subgoals["subgoals"]

    return result

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

def add_fixed_objects(object_dic, animation_profile):
    """This function will added the custom object to the obj_dic
    Args:
        object_dic(Dictionary): a object dictionary contain the default objects.
        animation_profile(Dictionary): the dict to store all information in animation profile.
    """
    
    for visual in animation_profile["objects"]["custom"]:
        objects=animation_profile["objects"]["custom"][visual]
        for obj_name in objects:            
            object_dic[obj_name] = animation_profile["visual"][visual]
            object_dic[obj_name]["name"] = obj_name

def get_visualisation_json(predicates, animation_profile,actionlist,problem_dic):
    """This function is the main function of this module, it will call the other functions
    to manipulate the visualisation file for the unity visualiser.

    Args:
        predicates(Dictionary): an dictionary contains the 1.objects name and the 2.predicates for
                                each stages.
        animation_profile(Dictionary): the dict to store all information in animation profile.

    """

    object_list = copy.deepcopy(predicates["objects"])
    stages = copy.deepcopy(predicates["stages"])
    # subgoals = copy.deepcopy(predicates["subgoals"])
    predicates_rules = animation_profile["predicates_rules"]
    objects_dic = Initialise.initialise_objects(object_list, animation_profile)
    space = Initialise.initialise_custom_functions()
    add_fixed_objects(objects_dic, animation_profile)
    result = solve_all_stages(stages, objects_dic, predicates_rules, space,actionlist,problem_dic)
    # print(result["subgoals"])
    return result
