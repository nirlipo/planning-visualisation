
"""This module is designed to help with transfer the animation profile into correct JSON format"""
# -----------------------------Authorship-----------------------------------------
# -- Authors  : Ella
# -- Group    : Planning Visualisation
# -- Date     : 2/Oct/2018
# -- Version  : 1.0
# --------------------------------------------------------------------------------
# -----------------------------Reviewer-------------------------------------------
# -- Authors  :
# -- Group    :
# -- Date     :
# -- Version  :
# --------------------------------------------------------------------------------
import re
import sys
import json
import copy

#######################################################
# Input File: A json object contains animation file
# Output : A complete animation profile in JSON format
#######################################################

import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from colour import Color
import animationparser

def transfer(result):
    """The function return the animation file in correct format
        Args:
            Dict: animation file json object
        Returns:
            Dict: correct animation profile
        """
    dictget(result)

    return result


def dictget(dict1):
    """The function transfers all the digital number string into number
     """
    # if(type(dict1) == dict):

    for k, v in dict1.items():

        if type(v) is not dict and type(v) is not list:
            value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')

            result = value.match(v)
            if (result):
                dict1[k] = float(v)
            elif (v.isdigit()):
                dict1[k] = int(v)
            elif (v == "TRUE"):
                dict1[k] = True

            elif (v == "FALSE"):
                dict1[k] = False
            elif (v == "Null"):
                dict1[k] = False
            elif (check_color(v)):
                print(v)
                dict1[k]=transfer_Color(v)

        else:
            if type(v) is dict:
                dictget(v)
            elif type(v) is list:
                # print("list us")
                transfer_list(v)


    # elif (type(dict1) == list):
    #     print(list)
    #     for a in dict1:
    #         if type(a) is not dict and type(v) is not list:
    #             value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
    #             result = value.match(a)
    #             if (result):
    #                 print(result)
    #                 dict[list.index(a)] = float(a)


    return dict1

def transfer_list(list):
    for a in list:
        if type(a) is not dict and type(a) is not list:
            print(a)
            value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')

            result = value.match(a)
            if (result):
                print(result)
                list[list.index(a)] = float(a)
            elif (a.isdigit()):
                list[list.index(a)] = int(a)
        else:
            if type(a) is dict:
                dictget(a)
            elif type(a) is list:
                transfer_list(a)
    return list
def transfer_Color(color):
    """
    This function transfer color name into rgba
    """


    c = Color(color).get_rgb()
    rgba = {"r": round(c[0],4),
            "g": round(c[1],4),
            "b": round(c[2],4),
            "a": 1.0
            }

    return rgba


def check_color(color):
    try:
        # Converting 'deep sky blue' to 'deepskyblue'
        color = color.replace(" ", "")
        Color(color)
        # if everything goes fine then return True
        return True
    except ValueError: # The color code was not found
        return False