"""This module is designed to help with getting a valid plan for the given problem/domain"""
#-----------------------------Authorship-----------------------------------------
#-- Authors  : Sai
#-- Group    : Planning Visualisation
#-- Date     : 13/August/2018
#-- Version  : 1.0
#--------------------------------------------------------------------------------
#-----------------------------Reviewer-------------------------------------------
#-- Authors  : Sharukh, Gang chen
#-- Group    : Planning Visualisation
#-- Date     : 23/August/2018
#-- Version  : 1.0
#--------------------------------------------------------------------------------
import re
import sys

#######################################################
# Input File: A domain file
# Output : All the predicates in the given domain.pddl file
#######################################################

def get_domain_json(file_name):
    PredicateList = ""
    try:
        patternPare = re.compile(r'\((.*?)\)')
        strPre = file_name[file_name.index("predicates") + len("predicates"):file_name.index("action")]

        namePare = patternPare.findall(strPre)
        PredicateList = {}
        for name in namePare:
            if (name.find("?") != -1):
                indexQue = name.find("?")
                namePre = name[0:indexQue - 1]
                PredicateList[namePre] = name.count("?")
            else:
                PredicateList[name] = name.count("?")
    except:
        raise ValueError("Empty string found")
    return PredicateList
if __name__ == "__main__":
    get_domain_json(open("domain_blocks.pddl", 'r').read())