import re


#######################################################
# Input File: domain file
# Output : all predicates in the domain
#######################################################
import sys


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