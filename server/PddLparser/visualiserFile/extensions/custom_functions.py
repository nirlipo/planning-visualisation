import re
import numpy as np
"""This module contain all the customer funtion we designed to help position the objects"""


__all__ = ['init_space', 'distributex','distribute_grid_around_pointx']


def init_space(size):
    """The funtion initialise an space for distributex function
    Args:
        size(int): the max number of item in space
    Returns:
        space: an array of integer
    """
    space = []
    for i in range(size):
        space.append(i)
    return space


def distributex(obj, gspace, spacebtw, width, remove):
    """The function return the x location of object of an given space"""
    space=gspace["distributex"]
    if not remove:
        if obj in space:
            objindex = space.index(obj)
            return objindex * (width + spacebtw)
        else:
            for num, value in enumerate(space):
                if num == value:
                    space[num] = obj
                    return num * (width + spacebtw)
    else:
        if obj in space:
            objindex = space.index(obj)
            space[objindex] = objindex
            return True
    return False

def distribute_grid_around_pointx(obj,rowindex,margin):
    row=int(re.findall('\d+',obj)[rowindex])
    return row*margin

def distribute_grid_around_pointy(obj,colindex,margin):
    col=int(re.findall('\d+',obj)[colindex])
    return col*margin

def draw_line(x1,y1,x2,y2,name):
    
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