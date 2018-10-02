
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
    transfer_Color(result["visual"])
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
                dict1[k] = v.lower()
                print(dict1[k])
            elif (v == "FALSE"):
                dict1[k] = v.lower()
                print(dict1[k])
            elif (v == "Null"):
                dict1[k] = "false"
                print(dict1[k])


        else:
            if type(v) is dict:
                dictget(v)
    return dict1

def transfer_Color(result):
    """
    This function transfer color name into rgba
    """

    for k in result:
        if result[k]["color"] != "RANDOMCOLOR":
            color = (result[k]["color"])
            c = Color(color).get_rgb()
            rgba = {"r": str(float(c[0])),
                    "g": str(float(c[1])),
                    "b": str(float(c[2])),
                    "a": str(1.0)
                    }
            result[k]["color"] = rgba
    return result


