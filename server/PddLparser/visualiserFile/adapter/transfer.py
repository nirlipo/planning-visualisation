"""This component transfers the result generated by Predicate Solver into the final visualisation file"""
import copy
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/../" +"predicate_solver"))
import initialise
import solver


# This python file aims to finish step 4 in our solution
#######################################################
# Input File: the reuslt of initialise componenet
# Input File: the result of solver componenet
# Output : Visualisation File
#######################################################

def transfer(one_stage, initialobjects, panel_size,shiftx,shifty, padding=20):
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
    for obj in one_stage:
        if "x" not in one_stage[obj] or "y" not in one_stage[obj]:
            continue
        one_stage[obj]
        # get all information about position
        x_num = one_stage[obj]["x"]
        y_num = one_stage[obj]["y"]
        width = one_stage[obj]["width"]
        # set the panel with after we got the panel width
        if width == "panel_size":
            width = panel_size - 2 * padding
        height = one_stage[obj]["height"]
        # transfer the position info into position needed in Unity
        min_x = (x_num + padding+shiftx) / panel_size
        max_x = (x_num+shiftx + width + padding) / panel_size
        min_y = (y_num+shifty+padding) / panel_size
        max_y = (y_num +shifty+ height+padding) / panel_size
        position_dic["minX"] = round(min_x, 3)
        position_dic["maxX"] = round(max_x, 3)
        position_dic["minY"] = round(min_y, 3)
        position_dic["maxY"] = round(max_y, 3)
        # update the old dict
        one_stage[obj].update(position_dic)
        temp.append(one_stage[obj])
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
    min_x = 0
    min_y = 0
    for stage in lists:
        stageitems = stage["visualSprites"]

        for item in stageitems:
            if "x" not in stageitems[item] or "y" not in stageitems[item]:
                continue
            x = stageitems[item]["x"]
            y = stageitems[item]["y"]

            if type(stageitems[item]["width"]) is int:
                new_x = x + stageitems[item]["width"]
                if new_x > max_x:
                    max_x = new_x
                if x < min_x:
                    min_x = x
            if type(stageitems[item]["height"]) is int:
                new_y = y + stageitems[item]["height"]
                if new_y > max_y:
                    max_y = new_y
                if y < min_y:
                    min_y = y
    return max(max_x, max_y) + 2 * padding, abs(min_x), abs(min_y)


def generate_visualisation_file(result, object_list,animation_profile):
    """This function generates the visualisation file.
    Args:
        result(Dict): the dict to be converted.
        object_list: list of all the name of the objects.
    """
    final = {"visualStages": []}
    one_stage = {}
    sprite_list = []
    lists = result["visualStages"]
    panel_size,shiftx,shifty= get_panel_size(result)
    for item in lists:
        one_stage = item["visualSprites"]
        transfered_stage=transfer(one_stage, object_list, panel_size,shiftx,shifty)
        transfered_stage["stageName"]=item["stageName"]
        transfered_stage["stageInfo"]=item["stageInfo"]
        sprite_list.append(transfered_stage)
    final["visualStages"] = sprite_list
    final["transferType"]=1
    final["imageTable"]=animation_profile["imageTable"]

    return final

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
    objects_dic = initialise.initialise_objects(object_list, animation_profile)
    solver.add_fixed_objects(objects_dic, animation_profile)
    # space ={}
    # space["distributex"]=custom_functions.init_space(len(object_list))
    # space["distribute_vertical"]={}
    # result = solver.solve_all_stages(stages, objects_dic, predicates_rules, space)
    result = solver.solve_all_stages(stages, objects_dic, predicates_rules, object_list)

    return generate_visualisation_file(result, list(objects_dic.keys()),animation_profile)