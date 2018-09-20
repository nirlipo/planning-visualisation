"""This module is designed to help with getting a set of coordinates for Solver"""
#-----------------------------Authorship-----------------------------------------
#-- Authors  : Yi Ding
#-- Group    : Planning Visualisation
#-- Date     : 16/Sep/2018
#-- Version  : 2.0
#--------------------------------------------------------------------------------
#-----------------------------Reviewer-------------------------------------------
#-- Authors  : Sunmuyu Zhang
#-- Group    : Planning Visualisation
#-- Date     : 16/Sep/2018
#-- Version  : 2.0
#--------------------------------------------------------------------------------
import re
import numpy as np
"""This module contain all the customer funtion we designed to help position the objects"""
#######################################################
# Output : A set of coordinates that satisfying the requirements of Solver
#######################################################

__all__ = ['customf_controller','distributey','distribute_grid_around_pointx']

def customf_controller(fname,obj_dic,settings,state,remove):
    if fname == "distributex":
        return distributex(obj_dic, settings,state,remove)
    elif fname == "distribute_grid_around_point":
        return distribute_grid_around_point(obj_dic, settings,state,remove)
    elif fname == "distribute_within_objects_vertical":
        return distribute_within_objects_vertical(obj_dic, settings,state,remove)
    elif fname == "apply_smaller":
        return apply_smaller(obj_dic, settings,state,remove)
    elif fname == "align_middle":
        return align_middle(obj_dic, settings,state,remove)
    elif fname == "distributey":
        return distributey(obj_dic, settings,state,remove)
    elif fname == "distribute_within_objects_horizontal":
        return distribute_within_objects_horizontal(obj_dic, settings,state,remove)
    elif fname == "calculate_label":
        return calculate_label(obj_dic, settings,state,remove)

def distributex(obj_list, settings, state, remove):
    """This funtion will return the x position of an object. used for block domain
    Args:
        obj_list(Array): Array of objects dictionary
        settings(dictionary): a dictionary for settings
        state(dictionary): state of the world
        remove(Boolean): whether remove the object from the state
    Returns:
        Returns:
            1. updated attribute dictionary and state
            2. Boolean if an object is removed from the state or unknown problem happen and state

    """

    #intialise the state to an integer array
    if not state:
        state=[0]
    #default function settings
    default_setting={
        "spacebtw":20
    }
    #update default settings
    for setting in default_setting:
        if setting in settings:
            default_setting[setting]=settings[setting]
    if len(obj_list)>1:
        return False

    #object name
    obj,objdic=list(obj_list[0].items())[0]
    width=objdic["width"]
    if not remove:
        if obj in state:
            objindex = state.index(obj)
            objdic["x"]= objindex * (width + default_setting["spacebtw"])
            return objdic, state
        else:
            for num, value in enumerate(state):
                if num == value:
                    state[num] = obj
                    state.append(num+1)
                    objdic["x"] = num * (width + default_setting["spacebtw"])
                    return objdic, state
    else:
        if obj in state:
            objindex = state.index(obj)
            state[objindex] = objindex
            return True
    return False

def distributey(obj_list,settings,state,remove):
    """The function return the y location of object based on the number in object name
    Args:
        obj_list(Array): Array of objects dictionary
        settings(dictionary): a dictionary for settings
        state(dictionary): state of the world
        remove(Boolean): whether remove the object from the state
    Returns:
        updated attribute dictionary and state

    """
    #default function settings
    default_setting={
        "spacebtw":20,
        "initial":0
    }
    #update default settings
    for setting in default_setting:
        if setting in settings:
            default_setting[setting]=settings[setting]


    obj,objdic=list(obj_list[0].items())[0]
    height=objdic["height"]
    row=int(re.findall('\d+',obj)[0])- default_setting["initial"]
    objdic["y"] = row*(height+default_setting["spacebtw"])
    return objdic,state


def distribute_grid_around_point(obj_list, settings, state, remove):
    """The function return the x location of object based on the number in object name, Node1-2,etc.
    Args:
        obj_list(Array): Array of objects dictionary
        settings(dictionary): a dictionary for settings
        state(dictionary): state of the world
        remove(Boolean): whether remove the object from the state
    Returns:
        updated attribute dictionary and state

    """


    #default function settings
    default_setting={
        "rowindex":0,
        "colindex":1,
        "margin":100
    }
    #update default settings
    for setting in default_setting:
        if setting in settings:
            default_setting[setting]=settings[setting]

    #object name
    obj,objdic=list(obj_list[0].items())[0]
    row=int(re.findall('\d+',obj)[default_setting["rowindex"]])
    col= int(re.findall('\d+', obj)[default_setting["colindex"]])
    objdic["x"]= row * default_setting["margin"]
    objdic["y"] = col * default_setting["margin"]
    return objdic, state


def draw_line(x1,y1,x2,y2,name):
    """The function return an line object with initial location and rotation angle
    Args:
        x1,y1: point1
        x2,y2: point2
        name: name of the line
    Returns:
        Integer: y postion of obj

    """
    vec1=np.array([1,0])
    vec2=np.array([x2-x1,y2-y1])
    Lvec1=np.sqrt(vec1.dot(vec1))
    Lvec2=np.sqrt(vec2.dot(vec2))
    middle=[(x1+x2)/2,(y1+y2)/2]
    lx1=middle[0]-Lvec2/2
    ly1=middle[1]
    cross=np.cross(vec1,vec2)
    cos_angle=vec1.dot(vec2)/(Lvec1*Lvec2)
    radius=np.arccos(cos_angle)
    
    angle=radius*360/2/np.pi
    
    if cross <= 0:
        fangle = angle
    elif cross>0:
        fangle= 360 - angle
        
    line={}
    line["width"]=Lvec2
    line["rotate"]=fangle
    line["x"]=lx1
    line["y"]=ly1
    line["showName"]=False
    line["prefabImage"]="line"
    line["color"]={"r":0,"g":0,"b":0,"a":1}
    line["height"]=5
    line["name"]=name
    line["depth"]=0
    return line

def distribute_within_objects_vertical(obj_list, settings, state, remove):
    """The function return an x/y location of obj based on the location of node
    Args:
        obj_list(Array): Array of objects dictionary
        settings(dictionary): a dictionary for settings
        state(dictionary): state of the world
        remove(Boolean): whether remove the object from the state
    Returns:
        updated attribute dictionary and state

    """

    #default function settings
    default_setting={
        "padding":5,
        "row_count":4
    }
    #update default settings
    for setting in default_setting:
        if setting in settings:
            default_setting[setting]=settings[setting]

    if len(obj_list) !=2:
        return False
    #object name
    obj,objdic=list(obj_list[0].items())[0]
    parent,parentdic = list(obj_list[1].items())[0]

    #initalise state for parent
    if parent not in state:
        state[parent]=[0]

    row_count=default_setting["row_count"]
    padding=default_setting["padding"]

    if obj in state[parent]:
        objindex = state[parent].index(obj)
        objdic["x"]= parentdic["x"] + int(objindex / row_count) * objdic["width"] + padding
        objdic["y"]= parentdic["y"] + (objindex % row_count) * objdic["height"] + padding
        return objdic, state
    else:
        for num, value in enumerate(state[parent]):
            if num == value:
                state[parent][num] = obj
                state[parent].append(num + 1)
                # print(obj_dic[parent]["x"]+int(num/row_count)*obj["width"]+padding)
                objdic["x"]= parentdic["x"] + int(num / row_count) * objdic["width"] + padding
                objdic["y"]= parentdic["y"] + (num % row_count) * objdic["height"] + padding
                return objdic, state

def distribute_within_objects_horizontal(obj_list, settings, state, remove):
    """The function return x location of obj based on the location of parent
    Args:
        obj_list(Array): Array of objects dictionary
        settings(dictionary): a dictionary for settings
        state(dictionary): state of the world
        remove(Boolean): whether remove the object from the state
    Returns:
        updated attribute dictionary and state

    """

    #default function settings
    default_setting={
        "padding":40,
        "col_count":4
    }
    #update default settings
    for setting in default_setting:
        if setting in settings:
            default_setting[setting]=settings[setting]

    if len(obj_list) !=2:
        return False
    #object name

    obj,objdic=list(obj_list[0].items())[0]
    parent,parentdic = list(obj_list[1].items())[0]

    #initalise state for parent
    if parent not in state:
        state[parent]=[0]

    col_count=default_setting["col_count"]
    padding=default_setting["padding"]

    if obj in state[parent]:
        objindex = state[parent].index(obj)
        objdic["x"]=parentdic["x"]+objindex*(objdic["width"]+padding)
        return objdic,state
    else:
        for num, value in enumerate(state[parent]):
            if num == value:
                state[parent][num] = obj
                state[parent].append(num+1)
                objdic["x"] = parentdic["x"]+num*(objdic["width"]+padding)
                return objdic,state

def apply_smaller(obj_list, settings, state, remove):
    """The function return width of object, it remember how big the object are by integer.Used for hanoi domain
    Args:
        obj_list(Array): Array of objects dictionary
        settings(dictionary): a dictionary for settings
        state(dictionary): state of the world
        remove(Boolean): whether remove the object from the state
    Returns:
        updated attribute dictionary and state

    """
    #default function settings
    default_setting={
        "increase_width":10,
    }
    #update default settings
    for setting in default_setting:
        if setting in settings:
            default_setting[setting]=settings[setting]

    if len(obj_list) !=2:
        return False
    #object name
    obj1,obj1dic=list(obj_list[0].items())[0]
    obj2,obj2dic = list(obj_list[1].items())[0]
    #remove the digital char
    obj1type=''.join(filter(lambda x: x.isalpha(), obj1))
    obj2type=''.join(filter(lambda x: x.isalpha(), obj2))
    
    if obj1type==obj2type and obj1!=obj2:

        if obj1 not in state:
            state[obj1]=1
        else:
            state[obj1]=state[obj1]+1
        obj1dic["width"]=obj1dic["width"] +default_setting["increase_width"]
        return obj1dic,state
    else:

        return obj1dic,state


def calculate_label(obj_list, settings, state, remove):
    """The function return the label of the objects, e.g showing how many packages in the trunks
        Args:
            obj_list(Array): Array of objects dictionary
            settings(dictionary): a dictionary for settings
            state(dictionary): state of the world
            remove(Boolean): whether remove the object from the state
        Returns:
            updated attribute dictionary and state

        """
    # object name
    obj2, obj2dic = list(obj_list[1].items())[0]
    if obj2 not in state:
        state[obj2] = 1
        obj2dic["showLabel"] = True
    else:
        state[obj2] = state[obj2] +1
        obj2dic["showLabel"] = True

    obj2dic["label"] = state[obj2]
    return obj2dic,state

def align_middle(obj_list, settings, state, remove):
    """The function return updated x position of obj1 based on obj2, it will make sure the middle of two object are
    Args:
        obj_list(Array): Array of objects dictionary
        settings(dictionary): a dictionary for settings
        state(dictionary): state of the world
        remove(Boolean): whether remove the object from the state
    Returns:
        updated attribute dictionary and state
    """

    if len(obj_list) !=2:
        return False

    #object name
    obj1,obj1dic=list(obj_list[0].items())[0]
    obj2, obj2dic = list(obj_list[1].items())[0]

    #remove the digital char
    # obj1type=''.join(filter(lambda x: x.isalpha(), obj1name))
    # obj2type=''.join(filter(lambda x: x.isalpha(), obj2name))
    obj1dic["x"]=obj2dic["x"]+(obj2dic["width"]-obj1dic["width"])/2
    return obj1dic,state