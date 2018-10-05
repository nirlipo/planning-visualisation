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
import parser.Plan_generator  # Step1: get plan from planning domain api
import parser.Animation_parser  # Step1: get plan from planning domain api
import parser.Problem_parser  # Step2: parse problem pddl, to get the inital and goal stage
import parser.Predicates_generator  # Step3: manipulate the predicate for each step/stage
import adapter.visualiser_adapter.Transfer # Step4. use the animation profile and stages from step3 to get the visualisation file
import parser.Domain_parser # Step3: extract all the available predicates from problem.pddl
import json

def get_visualisation_file():
    # # This function will call the other modules to generate the visualisaiton file.
    # if len(sys.argv) < 4:
    # 	print("some file is missing, please follow the command below to run the program")
    # 	print("python main.py [dommainfile] [problemfile] [animationprofile]")
    # 	sys.exit()
    try:
        domain_file = "example/block/domain_blocks.pddl"
        problem_file = "example/block/bw01.pddl"
        animation_file = "example/block/blockanimation.pddl"
        url_link = "http://solver.planning.domains/solve"

        # read animation profile from json
        file = open(animation_file)
        content = file.read()
        animation_profile = json.loads(parser.Animation_parser.get_animation_profile(content))
        # print(parser.animation_parser.compare_String("Asdd","asdd"))
        # print(parser.animation_parser.get_animation_profile(content))

        plan = parser.Plan_generator.get_plan(open(domain_file, 'r').read(),
                                               open(problem_file, 'r').read(),
                                               url_link)

        # print(json.dumps(plan))
        predicates_list = parser.Domain_parser.get_domain_json(open(domain_file, 'r').read())
        # print(json.dumps(predicates_list))
        problem_json = parser.Problem_parser.get_problem_json(open(problem_file, 'r').read(), predicates_list)
        # print(json.dumps(problem_json))
        stages = parser.Predicates_generator.get_stages(plan, problem_json, open(problem_file, 'r').read(), predicates_list)

        print(json.dumps(adapter.visualiser_adapter.Transfer.get_visualisation_json(stages, animation_profile,plan['result']['plan'],problem_json)))
    except Exception as e:
        message = repr(e)
        final = {"visualStages": [],"subgoalPool":{},"subgoalMap":{},"transferType":0,"imageTable": {}, "message": str(message)}
        print(final)
if __name__ == "__main__":
    get_visualisation_file()
