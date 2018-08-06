import re
import string


#######################################################
# Input File: domain file
# Output : predicates for INIT stage and GOAL stage
#######################################################
def get_domain_json(file_name):
    patternPare = re.compile(r'\((.*?)\)')
    fileop = open(file_name)
    strfile = fileop.read()
    strPre = strfile[strfile.index("predicates") + len("predicates"):strfile.index("action")]

    namePare = patternPare.findall(strPre)
    PredicateList = {}
    for name in namePare:
        if (name.find("?") != -1):
            indexQue = name.find("?")
            namePre = name[0:indexQue - 1]
            #PredicateList.append(namePre)
            PredicateList[namePre] = name.count("?")
            #print(name, name.count("?"))
        else:
            #PredicateList.append(name)
            PredicateList[name] = name.count("?")

    return PredicateList