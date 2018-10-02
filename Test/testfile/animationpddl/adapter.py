
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
                # print(dict1[k])
            elif (v == "FALSE"):
                dict1[k] = False
                # print(dict1[k])
            elif (v == "Null"):
                dict1[k] = False
                # print(dict1[k])
            elif (check_color(v)):
                print(v)
                dict1[k]=transfer_Color(v)



        else:
            if type(v) is dict:
                dictget(v)
    return dict1

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