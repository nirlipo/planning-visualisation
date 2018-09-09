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
import json
import copy
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/../" +"predicate_solver"))
import custom_functions
import initialise

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
    
    predicatename = predicate["name"]
    objectnamelist = copy.deepcopy(predicate["objectNames"])
    predicate_rule = copy.deepcopy(predicates_rules[predicatename])

    if ("left" in predicates_rules[predicatename]):
        objectnamelist.insert(0,0)
    if("right" in predicates_rules[predicatename]):
        objectnamelist.append(predicates_rules[predicatename]["right"])
    for rulename in predicate_rule["rules"]:
        rule = predicate_rule[rulename]
        for key in rule:
            # 0 is on the left side of equation
            if key != "value" and key != "0" and key!="action":
                if key=="require":
                    for objindex in rule[key]:
                        for att in rule[key][objindex]:
                            objectname=objectnamelist[int(objindex)]
                            if objects_dic[objectname][att] is False:
                                return False              
                else:
                    property_check = rule[key]
                    objectname = objectnamelist[int(key)]
                    if objects_dic[objectname][property_check] is False:
                        return False
    return True


def applypredicates(predicate,
                    objects_dic,
                    predicates_rules,
                    space):
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
    objects = copy.deepcopy(predicate["objectNames"])
    
    if ("left" in predicates_rules[pname]):
        left = predicates_rules[pname]["left"]
        objects.insert(0,0)
    else:
        left = objects[0]
    
    
    if("right" in predicates_rules[pname]):
        objects.append(predicates_rules[pname]["right"])
        
    for rulename in predicates_rules[pname]["rules"]:
        if "value" in predicates_rules[pname][rulename]:
            propertyname = predicates_rules[pname][rulename]["0"]
            value = predicates_rules[pname][rulename]["value"]
            rule = predicates_rules[pname][rulename]
            if "function" in value:
                if value["function"] == "distributex":
                    objects_dic[left][propertyname] = custom_functions.distributex(
                        left, space, 20, 80, False)
                elif value["function"] == "distribute_grid_around_pointx":
                    objects_dic[left][propertyname] = custom_functions.distribute_grid_around_pointx(
                        left, 0,100)
                elif value["function"] == "distribute_grid_around_pointy":
                    objects_dic[left][propertyname] = custom_functions.distribute_grid_around_pointy(
                        left, 1,100)
                elif value["function"] == "distribute_vertical":
                    node=objects[1]
                    objects_dic[left][propertyname]= custom_functions.distribute_vertical(objects_dic[left],objects_dic[node],4,propertyname,space)
                elif value["function"] == "apply_smaller":
                    obj2=objects[1]
                    objects_dic[left][propertyname]= custom_functions.apply_smaller(objects_dic[left],objects_dic[obj2],10,space)
                elif value["function"] == "shiftx":
                    obj2=objects[1]
                    objects_dic[left][propertyname]= custom_functions.shiftx(objects_dic[left],objects_dic[obj2])
                elif value["function"] == "distributey":
                    objects_dic[left][propertyname]= custom_functions.distributey(objects_dic[left],50)      
                elif value["function"] == "distribute_horizontal":
                    obj2=objects[1]
                    objects_dic[left][propertyname]= custom_functions.distribute_horizontal(objects_dic[left],objects_dic[obj2],space) 
            elif "equal" in value:
                right_value = value["equal"]
                if type(right_value) is not dict:#for color dic
                    if right_value in rule:
                        right_proterpy = rule[right_value]
                        right_object = objects[int(right_value)]
                        objects_dic[left][propertyname] = objects_dic[
                            right_object][right_proterpy]
                    else:
                        objects_dic[left][propertyname] = right_value
                else:
                    objects_dic[left][propertyname] = right_value

            elif "add" in value:
                rightvalue = 0
                for additem in value["add"]:
                    if additem in rule:
                        right_property = rule[additem]
                        right_object = objects[int(additem)]
                        addvalue = objects_dic[right_object][right_property]
                        rightvalue += addvalue
                    else:
                        rightvalue += additem
                objects_dic[left][propertyname] = rightvalue
        else:
            action=predicates_rules[pname][rulename]["action"]
            if "function" in action:
                object1,object2=objects
                x1=objects_dic[object1]["x"]+objects_dic[object1]["width"]/2
                y1=objects_dic[object1]["y"]+objects_dic[object1]["height"]/2
                x2=objects_dic[object2]["x"]+objects_dic[object2]["width"]/2
                y2=objects_dic[object2]["y"]+objects_dic[object2]["height"]/2
                if action["function"]=="draw_line":
                    key=pname+objects[0]+objects[1]
                    objects_dic[key]=custom_functions.draw_line(x1,y1,x2,y2,key)


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
            space["apply_smaller"]={} #For hanoi problem, reset each stage
            applypredicates(predicate, objects_dic, predicates_rules, space)
        else:
            if not predicates:  # if the last predicate can not be solved
                return False
            predicates.append(predicate)
        i+=1
    return True


def keysort(name,predicates_rules):
    if name in predicates_rules:
        if "priority" in predicates_rules[name]:
            return predicates_rules[name]["priority"]
        else:
            return 10
    else:
        return 10
def priority(predicates,predicates_rules):

    return sorted(predicates, key=lambda k: keysort(k["name"],predicates_rules))


def solve_all_stages(stages, objects_dic, predicates_rules, space):
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
    sublist = []
    index = 0
    for stage in stages:

        stage_dic = {}
        object_dic_copy = copy.deepcopy(objects_dic)
        predicates = stage["items"]
        sorted_predicates=priority(predicates,predicates_rules)
        solvepredicates(sorted_predicates, object_dic_copy, predicates_rules, space)
        stage_dic["visualSprites"] = object_dic_copy
        if "stageName" not in stage:
            stage_dic["stageName"]="Inital Stage"
            stage_dic["stageInfo"]="No step information"
            stage_dic["subgoal"] = ""
        else:
            stage_dic["stageName"]=stage["stageName"]
            stage_dic["stageInfo"]=stage["stageInfo"]


        result["visualStages"].append(stage_dic)
        index = index +1


    return result



def add_fixed_objects(object_dic, animation_profile):
    """This function will added the custom object to the obj_dic
    Args:
        object_dic(Dictionary): a object dictionary contain the default objects.
        animation_profile(Dictionary): the dict to store all information in animation profile.
    """
    
    for shape in animation_profile["objects"]["custom"]:
        objects=animation_profile["objects"]["custom"][shape]
        for obj_name in objects:            
            object_dic[obj_name] = animation_profile["shape"][shape]
            object_dic[obj_name]["name"] = obj_name