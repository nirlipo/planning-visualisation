import re


#######################################################
# Input File: domain file
# Output : all predicates in the domain
#######################################################
def get_domain_json(file_name):
    patternPare = re.compile(r'\((.*?)\)')
    fileop = open(file_name)
    strfile = fileop.read()
    strPre = strfile[strfile.index("predicates") + len("predicates"):strfile.index("action")]
    # find all the predicates in the domain
    namePare = patternPare.findall(strPre)
    PredicateList = {}
    for name in namePare:
        # predicates with "?"
        if (name.find("?") != -1):
            indexQue = name.find("?")
            namePre = name[0:indexQue - 1]
            #PredicateList.append(namePre)
            PredicateList[namePre] = name.count("?")

        # predicates without "?"
        else:
            #PredicateList.append(name)
            PredicateList[name] = name.count("?")

    return PredicateList