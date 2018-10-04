
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
import animation_parser

def transfer(result):
    """The function return the animation file in correct format
        Args:
            Dict: animation file json object
        Returns:
            Dict: correct animation profile
        """
    dictget(result)

    return result

def dictget(input):
    """The function transfers all the digital number string into number
     """
    if type(input) is str:
        print(input)
        return transfer_str(input)

    if type(input) is dict:
        for k, v in input.items():
            if type(v) is dict:
                input[k]=dictget(v)
            elif type(v) is list:
                input[k]=dictget(v)
            else:
                input[k]=transfer_str(v)
    elif type(input) is list:
        for i,item in enumerate(input):
            input[i]=dictget(item)

    return input
def transfer_str(v):
    value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')

    result = value.match(v)

    if (result):
        return float(v)
    elif (v.isdigit()):
        return int(v)
    elif (v == "TRUE"):
        return True
    elif (v == "FALSE"):
        return False
        # print(dict1[k])
    elif (v.lower() == "null"):
        return False
        # print(dict1[k])
    elif (check_color(v)):
        # print(v)
        return transfer_Color(v)
    else:
        return v

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