"""This module is designed to help with getting a set of coordinates for Solver"""
#-----------------------------Authorship-----------------------------------------
#-- Authors  : Sai
#-- Group    : Planning Visualisation
#-- Date     : 13/August/2018
#-- Version  : 1.0
#--------------------------------------------------------------------------------
#-----------------------------Reviewer-------------------------------------------
#-- Authors  : Sharukh
#-- Group    : Planning Visualisation
#-- Date     : 27/August/2018
#-- Version  : 1.0
#--------------------------------------------------------------------------------
import re
import numpy as np
"""This module contain all the customer funtion we designed to help position the objects"""
#######################################################
# Output : A set of coordinates that satisfying the requirements of Solver
#######################################################

__all__ = ['distributex','distributey','distribute_grid_around_pointx']


def distributex(obj, gspace, spacebtw, width, remove):
    """This funtion will return the x position of an object.used for block domain
    Args:
        obj(String): objectect name
        gspace(dictionary): a dictionary of all space information about the custom function.
        spacebtw(Integer): Space between two object
        width(Integer):width of the obj
        remove(Boolean): whether remove the object from the space
    Returns:
        Returns:
            1. Interger if remove is false
            2. Boolean if an object is removed from the space

    """
    space=gspace["distributex"]

    #intialise the space to an integer array
    if not space:
        gspace["distributex"]=[0]
        space=gspace["distributex"]

    if not remove:
        if obj in space:
            objindex = space.index(obj)
            return objindex * (width + spacebtw)
        else:
            for num, value in enumerate(space):
                if num == value:
                    space[num] = obj
                    space.append(num+1)
                    return num * (width + spacebtw)
    else:
        if obj in space:
            objindex = space.index(obj)
            space[objindex] = objindex
            return True
    return False

def distributey(obj,spacebtw):
    """The function return the y location of object based on the number in object name
    Args:
        obj(String): objectect name
        spacebtw(Integer): Space between two object
    Returns:
        Integer: y postion of obj

    """
    objname=obj["name"]
    height=obj["height"]
    row=int(re.findall('\d+',objname)[0])
    return row*(height+spacebtw)


def distribute_grid_around_pointx(obj,rowindex,margin):
    """The function return the x location of object based on the number in object name, Node1-2,etc.
    Args:
        obj(String): objectect name
        rowindex(Integer): indicate which number is for row
        margin: space between objects
    Returns:
        Integer: x postion of obj

    """
    row=int(re.findall('\d+',obj)[rowindex])
    return row*margin

def distribute_grid_around_pointy(obj,colindex,margin):
    """The function return the y location of object based on the number in object name, Node1-2,etc.
    Args:
        obj(String): objectect name
        colindex(Integer): indicate which number is for col
        margin: space between objects
    Returns:
        Integer: y postion of obj

    """
    col=int(re.findall('\d+',obj)[colindex])
    return col*margin

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

def distribute_vertical(obj,node,colcount,axis,gspace,padding=5):
    """The function return an x/y location of obj based on the location of node
    Args:
        obj: object table of the unsolved object
        node: object table of the parent object
        colcount: maximum number of objects for each column
        axis: axis can be x or y
        gspace(dictionary): a dictionary of all space information about the custom function.
        padding: default 5
    Returns:
        Integer: x/y postion of obj

    """
    objname=obj["name"]
    nodename=node["name"]
    space=gspace["distribute_vertical"]
    if nodename not in space:
        space[nodename]=[0]
    if axis =="x":#x axis
        if objname in space[nodename]:
            objindex = space[nodename].index(objname)
            return node["x"]+int(objindex/colcount)*obj["width"]+padding
        else:
            for num, value in enumerate(space[nodename]):
                if num == value:
                    space[nodename][num] = objname
                    space[nodename].append(num+1)
                    return node["x"]+int(num/colcount)*obj["width"]+padding
    else: #y axis
        if objname in space[nodename]:
            objindex = space[nodename].index(objname)
            return node["y"]+(objindex%colcount)*obj["height"]+padding
        else:
            for num, value in enumerate(space[nodename]):
                if num == value:
                    space[nodename][num] = objname
                    space[nodename].append(num+1)
                    return node["y"]+(num%colcount)*obj["height"]+padding

def distribute_horizontal(obj,parent,gspace,padding=40):
    """The function return x location of obj based on the location of parent
    Args:
        obj: object table of the unsolved object
        parent: object table of the parent object
        gspace(dictionary): a dictionary of all space information about the custom function.
        padding: default 40
    Returns:
        Integer: x postion of obj

    """
    objname=obj["name"]
    parentname=parent["name"]
    space=gspace["distribute_horizontal"]
    if parentname not in space:
        space[parentname]=[0]
    if objname in space[parentname]:
        objindex = space[parentname].index(objname)
        return parent["x"]+objindex*(obj["width"]+padding)
    else:
        for num, value in enumerate(space[parentname]):
            if num == value:
                space[parentname][num] = objname
                space[parentname].append(num+1)
                return parent["x"]+num*(obj["width"]+padding)

def apply_smaller(obj1,obj2,increase_width,gspace):
    """The function return width of object, it remember how big the object are by integer.Used for hanoi domain
    Args:
        obj1: object1 table of the unsolved object
        obj2: object2 table of the parent object
        increase_width: the difference of width between two objects
        gspace(dictionary): a dictionary of all space information about the custom function.
    Returns:
        Integer: width of obj1

    """
    obj1name=obj1["name"]
    obj2name=obj2["name"]
    #remove the digital char
    obj1type=''.join(filter(lambda x: x.isalpha(), obj1name))
    obj2type=''.join(filter(lambda x: x.isalpha(), obj2name))
    space=gspace["apply_smaller"]
    
    if obj1type==obj2type:
        if obj1name not in space:
            space[obj1name]=1
        else:
            space[obj1name]=space[obj1name]+1
        return obj1["width"]+space[obj1name]*increase_width
    else:
        return obj1["width"]
        
def shiftx(obj1,obj2):
    """The function return updated x position of obj1 based on obj2, it will make sure the middle of two object are
    aligned.
    Args:
        obj1: object1 table of the unsolved object
        obj2: object2 table of the parent object
    Returns:
        Integer: x position of obj1

    """

    obj1name=obj1["name"]
    obj2name=obj2["name"]
    #remove the digital char
    # obj1type=''.join(filter(lambda x: x.isalpha(), obj1name))
    # obj2type=''.join(filter(lambda x: x.isalpha(), obj2name))

    return obj2["x"]+(obj2["width"]-obj1["width"])/2