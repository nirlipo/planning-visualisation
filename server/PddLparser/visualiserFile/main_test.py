"""This module intergrate all the other module, it takes the domain PDDL, problem PDDL, and 
animation profile, and it write the visualisation file to visualsation.json.
"""
#-----------------------------Authorship-----------------------------------------
#-- Authors  : Sai
#-- Group    : Planning Visualisation
#-- Date     : 13/August/2018
#-- Version  : 1.0
#--------------------------------------------------------------------------------
#-----------------------------Reviewer-------------------------------------------
#-- Authors  : Sharukh
#-- Group    : Planning Visualisation
#-- Date     : 27/August/2018
#-- Version  : 1.0
#--------------------------------------------------------------------------------
import sys
import pparser.plan_generator  # Step1: get plan from planning domain api
import pparser.problem_parser  # Step2: parse problem pddl, to get the inital and goal stage
import pparser.predicates_generator  # Step3: manipulate the predicate for each step/stage
import adapter.transfer  # Step4. use the animation profile and stages from step3 to get the visualisation file
import pparser.domain_parser  # Step3: extract all the available predicates from problem.pddl
import json

def get_visualisation_file():
    # # This function will call the other modules to generate the visualisaiton file.
    # if len(sys.argv) < 4:
    # 	print("some file is missing, please follow the command below to run the program")
    # 	print("python main.py [dommainfile] [problemfile] [animationprofile]")
    # 	sys.exit()

    domain_file = "domain.pddl"
    problem_file = "pfile8.pddl"
    animation_file = "animation_hanoi_parsed.json"
    # animation_file = "grid_animation_profile_v3.json"

    url_link = ""

    # read animation profile from json
    file = open(animation_file)
    content = file.read()
    animation_profile = json.loads(content)

    plan = pparser.plan_generator.get_plan(open(domain_file, 'r').read(), 
                                           open(problem_file, 'r').read(),
                                           url_link)

    # print(json.dumps(plan))
    predicates_list = pparser.domain_parser.get_domain_json(open(domain_file, 'r').read())
    # print(json.dumps(predicates_list))
    problem_json = pparser.problem_parser.get_problem_json(open(problem_file, 'r').read(), predicates_list)
    # print(json.dumps(problem_json))
    stages = pparser.predicates_generator.get_stages(plan, problem_json, open(problem_file, 'r').read(), predicates_list)

    print(json.dumps(adapter.transfer.get_visualisation_json(stages, animation_profile,plan['result']['plan'],problem_json)))
if __name__ == "__main__":
    get_visualisation_file()
