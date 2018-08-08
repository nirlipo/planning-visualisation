"""This module will compute the visulisation file by using the stages predicates and animation"""
import json
import copy
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/../" +"extensions"))
import random_color
import custom_functions


def initialise_objects(object_list, animation_profile):
    """ This function initialise objects in the animation profile
    Args:
        object_list(List): the list to store all objects.
        animation_profile(Dictionary): the dict to store all information in animation profile.
    Returns:
        unsolved_objects(Dictionary): the objects that are not initialised.
    """
    unsolved_objects = {}
    for objectname in object_list:
        unsolved_objects[objectname] = {}
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
    objectnamelist = predicate["objectNames"]
    predicate_rule = predicates_rules[predicatename]
    for rulename in predicate_rule["rules"]:
        rule = predicate_rule[rulename]
        for key in rule:
            # 0 is on the left side of equation
            if key != "value" and key != "0":
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
    objects = predicate["objectNames"]
    left = objects[0]
    for rulename in predicates_rules[pname]["rules"]:
        propertyname = predicates_rules[pname][rulename]["0"]
        value = predicates_rules[pname][rulename]["value"]
        rule = predicates_rules[pname][rulename]
        if "function" in value:
            if value["function"] == "distributex":
                objects_dic[left][propertyname] = custom_functions.distributex(
                    left, space, 20, 80, False)
        elif "equal" in value:
            right_value = value["equal"]
            if right_value in rule:
                right_proterpy = rule[right_value]
                right_object = objects[int(right_value)]
                objects_dic[left][propertyname] = objects_dic[
                    right_object][right_proterpy]
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
    while predicates:
        predicate = predicates.pop(0)
        if predicate["name"] not in predicates_rules:
            continue
        if check_rule_complete(predicate, objects_dic, predicates_rules):
            applypredicates(predicate, objects_dic, predicates_rules, space)
        else:
            if not predicates:  # if the last predicate can not be solved
                return False
            predicates.append(predicate)
    return True


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
    for stage in stages:
        stage_dic = {}
        object_dic_copy = copy.deepcopy(objects_dic)
        predicates = stage["items"]
        solvepredicates(predicates, object_dic_copy, predicates_rules, space)
        stage_dic["visualSprites"] = object_dic_copy
        result["visualStages"].append(stage_dic)
    return result


def transfer(one_stage, initialobjects, panel_width, panel_height, padding=20):
    """This function converts the dictionary into the info needed in visualisation file.
    Args:
        one_stage(Dict): a dictionary contains the locaiton of objects for one stage/step
        initialise_objects(List): the list to store all objects that needed to be
                                  shown in the animation profile.
        panel_width(int): the width of the animation panel.
        panel_height(int): the height of the animation panel.
    Returns:
        transfered_stage(Dict): the dict to store all info needed in visualisation file.
    """
    # list that stores object name
    transfered_stage = {}
    temp = []
    # dict that stores new position info
    position_dic = {"minX": "",
                    "maxX": "",
                    "minY": "",
                    "maxY": ""}
    # new position info
    min_x = 0.0
    max_x = 0.0
    min_y = 0.0
    max_y = 0.0
    # generate new json file
    for i, obj in enumerate(initialobjects):
        temp.append(one_stage[obj])
        # get all information about position
        x_num = one_stage[obj]["x"]
        y_num = one_stage[obj]["y"]
        width = one_stage[obj]["width"]
        # set the panel with after we got the panel width
        if width == "panel_width":
            width = panel_width - 2 * padding
        height = one_stage[obj]["height"]
        # transfer the position info into position needed in Unity
        min_x = (x_num + padding) / panel_width
        max_x = (x_num + width + padding) / panel_width
        min_y = y_num / panel_height
        max_y = (y_num + height) / panel_height
        position_dic["minX"] = round(min_x, 3)
        position_dic["maxX"] = round(max_x, 3)
        position_dic["minY"] = round(min_y, 3)
        position_dic["maxY"] = round(max_y, 3)
        # update the old dict
        temp[i].update(position_dic)
        transfered_stage["visualSprites"] = temp
    return transfered_stage


def get_panel_size(result, padding=20):
    """This function will for loop all the objects in the visualisaiton dictionary,
    and try to find the max_x and max_y of the panel.
    .........max_y
    .        .
    .        .
    .        .
    ........max_x
    Args:
        result: visualisation dictionary that contain the location of each object
                for different stages.
        padding: padding between the object and the edge of the screen.
    Returns:
        max_x: the max x of objects.
        max_y: the max y of objects.

    """
    lists = result["visualStages"]
    max_x = 0
    max_y = 0
    for stage in lists:
        stageitems = stage["visualSprites"]
        for item in stageitems:
            if type(stageitems[item]["width"]) is int:
                new_x = stageitems[item]["x"] + \
                    stageitems[item]["width"] + 2 * padding
                if new_x > max_x:
                    max_x = new_x
            if type(stageitems[item]["y"]) is int:
                new_y = stageitems[item]["y"] + \
                    stageitems[item]["height"] + padding
                if new_y > max_y:
                    max_y = new_y
    return max_x, max_y


def generate_visualisation_file(result, object_list):
    """This function generates the visualisation file.
    Args:
        result(Dict): the dict to be converted.
        object_list: list of all the name of the objects.
    """
    final = {"visualStages": []}
    one_stage = {}
    sprite_list = []
    lists = result["visualStages"]
    panel_width, panel_height = get_panel_size(result)
    for item in lists:
        one_stage = item["visualSprites"]
        sprite_list.append(
            transfer(one_stage, object_list, panel_width, panel_height))
        final["visualStages"] = sprite_list

    return final


def add_fixed_objects(object_dic, animation_profile):
    """This function will added the custom object to the obj_dic
    Args:
        object_dic(Dictionary): a object dictionary contain the default objects.
        animation_profile(Dictionary): the dict to store all information in animation profile.
    """
    for obj_name in animation_profile["objects"]["customobj"]:
        object_dic[obj_name] = animation_profile["shape"][obj_name]
        object_dic[obj_name]["name"] = obj_name


def get_visualisation_json(predicates, animation_profile):
    """This function is the main function of this module, it will call the other functions
    to manipulate the visualisation file for the unity visualiser.

    Args:
        predicates(Dictionary): an dictionary contains the 1.objects name and the 2.predicates for
                                each stages.
        animation_profile(Dictionary): the dict to store all information in animation profile.

    """

    object_list = copy.deepcopy(predicates["objects"])
    stages = copy.deepcopy(predicates["stages"])
    predicates_rules = animation_profile["predicates_rules"]
    objects_dic = initialise_objects(object_list, animation_profile)
    add_fixed_objects(objects_dic, animation_profile)
    space = custom_functions.init_space(len(object_list))
    result = solve_all_stages(stages, objects_dic, predicates_rules, space)
    return generate_visualisation_file(result, list(objects_dic.keys()))
