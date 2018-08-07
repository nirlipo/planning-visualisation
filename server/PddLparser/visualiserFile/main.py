"""This module intergrate all the other module, it takes the domain PDDL, problem PDDL, and 
animation profile, and it write the visualisation file to visualsation.json.
"""
import sys
import parser.plan_generator  # Step1: get plan from planning domain api
import parser.problem_parser  # Step2: parse problem pddl, to get the inital and goal stage
import parser.predicates_generator  # Step3: manipulate the predicate for each step/stage
import generator.visualisation_generator  # Step4. use the animation profile and stages from step3 to get the visualisation file
import json

def get_visualisation_file():
	"""This function will call the other modules to generate the visualisaiton file.
	"""
	if len(sys.argv) < 4:
	    print("some file is missing, please follow the command below to run the program")
	    print("python main.py [dommainfile] [problemfile] [animationprofile]")
	    sys.exit()

	domain_file = sys.argv[1]
	problem_file = sys.argv[2]
	animation_file = sys.argv[3]

	# read animation profile from json
	file = open(animation_file)
	content = file.read()
	animation_profile = json.loads(content)


	plan = parser.plan_generator.get_plan(domain_file, problem_file)
	problem_json = parser.problem_parser.get_problem_json(problem_file)
	stages = parser.predicates_generator.get_stages(plan, problem_json, problem_file)
	# A file called visualistaion.json will be generated in the folder if successful
	generator.visualisation_generator.get_visualisation_json(stages,animation_profile)
if __name__ == "__main__":
    get_visualisation_file()