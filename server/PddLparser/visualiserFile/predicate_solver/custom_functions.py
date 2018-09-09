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

__all__ = ['init_space', 'distributex','distribute_grid_around_pointx']


def distributex(obj, gspace, spacebtw, width, remove):
    """The function return the x location of object of an given space"""
    space=gspace["distributex"]
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
    """The function return the x location of object of an given space"""
    objname=obj["name"]
    height=obj["height"]
    row=int(re.findall('\d+',objname)[0])

    return row*(height+spacebtw)


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
def distribute_horizontal(obj,parent,gspace,padding=40):
    
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
    obj1name=obj1["name"]
    obj2name=obj2["name"]
    #remove the digital char
    obj1type=''.join(filter(lambda x: x.isalpha(), obj1name))
    obj2type=''.join(filter(lambda x: x.isalpha(), obj2name))
    # space=gspace["apply_smaller"]
    
    # if obj1type==obj2type:
    #     return obj2["x"]+(obj2["width"]-obj1["width"])/2
    # else:
    return obj2["x"]+(obj2["width"]-obj1["width"])/2