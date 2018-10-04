"""This module is responsible to get the planning result from other planning solver"""
#-----------------------------Authorship-----------------------------------------
#-- Authors  : Sai
#-- Group    : Planning Visualisation
#-- Date     : 13/August/2018
#-- Version  : 1.0
#--------------------------------------------------------------------------------
#-----------------------------Reviewer-------------------------------------------
#-- Authors  : Gang chen
#-- Group    : Planning Visualisation
#-- Date     : 23/August/2018
#-- Version  : 1.0
#--------------------------------------------------------------------------------
#-----------------------------Authorship-----------------------------------------
#-- Authors  : Sai
#-- Group    : Planning Visualisation
#-- Date     : 17/Septemeber/2018
#-- Version  : 2.0
#--------------------------------------------------------------------------------
#-----------------------------Reviewer-------------------------------------------
#-- Authors  : 
#-- Group    : Planning Visualisation
#-- Date     : 
#-- Version  : 2.0
#--------------------------------------------------------------------------------
import urllib.request
import json

#######################################################
# Input File: A domain file
# Input File: A problem file
# Output : A valid plan will be returned from the planning.domain website
#######################################################

def get_plan(domain_file, problem_file,url):
    """This function will send the domain and problem pddl to the planning.domains
    API to get the plan.
    Args:
            domain_file(String): file name of domain pddl.
            problem_file(String): file name of problem pddl.
    Returns:
            plan(Dictionary): plan return by the planning.domain API.
    """
    data = {'domain': domain_file,
            'problem': problem_file}

    if url == '':
        url = 'http://solver.planning.domains/solve'
        req = urllib.request.Request(url)
    else:
        req = urllib.request.Request(url)
        
    req.add_header('Content-Type', 'application/json')
    json_data = json.dumps(data)
    json_data_as_bytes = json_data.encode('utf-8')
    req.add_header('Content-Length', len(json_data_as_bytes))
    response = urllib.request.urlopen(req, json_data_as_bytes)
    str_response = response.read().decode('utf-8')
    plan = json.loads(str_response)
    return plan
