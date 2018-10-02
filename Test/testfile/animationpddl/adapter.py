
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
            if (v.isdigit()):
                dict1[k] = float(v)
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
            rgba = {"r": str(int(c[0])),
                    "g": str(int(c[1])),
                    "b": str(int(c[2])),
                    "a": str(1)
                    }
            result[k]["color"] = rgba
    return result


