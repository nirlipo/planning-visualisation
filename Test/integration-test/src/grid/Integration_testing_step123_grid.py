import datetime
import time
import unittest
import json
import re
import sys
sys.path.append('../../../../server/PddLparser/visualiserFile/')
import pparser.plan_generator as step1
import pparser.problem_parser as step2
import pparser.predicates_generator as step3
import generator.visualisation_generator as step4
import pparser.domain_parser as dom_par
import copy

class MyTestCase(unittest.TestCase):
    # Test if the output the PDDL parser component is not empyt
    # Input: an empty grid domain pddl file and a problem pddl.
    # Output: an empty parsed stages json.
    def test_integration_predicate_each_stage_step123(self):
        # Read input
        domain_file = ""
        problem_file = ""
        predicates_list = dom_par.get_domain_json(domain_file)
        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file, predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        self.assertRaises(Exception,lambda:predicates_list)

    # Test if the output the PDDL parser component is not empyt
    # Input: an empty grid domain pddl file and a problem pddl.
    # Output: an empty parsed stages json.
    def test_integration_predicate_each_stage_step123(self):
        # Read input
        domain_file = ""
        problem_file = ""
        predicates_list = dom_par.get_domain_json(domain_file)
        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file, predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        self.assertRaises(Exception,lambda:problem_json)

    # Test if the output the PDDL parser component is not empyt
    # Input: an empty grid domain pddl file and a problem pddl.
    # Output: The entire parsing process can be finished within 5 sec
    def test_correct_inputs_stages(self):
        started_at = time.time()
        # Read input
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()
        predicates_list = dom_par.get_domain_json(domain_file)
        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file, predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        elapsed = time.time() - started_at

        self.assertTrue(elapsed < 5)

    # Test if the output the PDDL parser component is not empyt
    # Input: a standard grid domain pddl file and a problem pddl.
    # Output: a non-empty parsed stages json.
    def test_integration_predicate_each_stage_step123(self):
        # Read input
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()

        predicates_list = dom_par.get_domain_json(domain_file)
        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file, predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        self.assertTrue(stages)

    # Test if each stage has an adequate amount of add actions
    # Input: a standard grid domain pddl file and a problem pddl.
    # Output: the number of "add" action should be same as the number of stages in the plan
    def test_integration_predicates_add1_step123(self):
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()
        predicates_list = dom_par.get_domain_json(domain_file)

        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file, predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file, predicates_list)
        objectList = copy.deepcopy(stages["objects"])
        stages = copy.deepcopy(stages["stages"])
        register = 0
        for counter in range(0, len(stages)):
            if ("add" in stages[counter].keys()):
                register += 1
        self.assertEqual(register, len(stages))

    # Test if each stage has an adequate amount of remove actions
    # Input: a standard grid domain pddl file and a problem pddl.
    # Output: the number of "remove" action should be same as the number of stages in the plan
    def test_integration_predicates_add2_step123(self):
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()
        predicates_list = dom_par.get_domain_json(domain_file)

        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file, predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file, predicates_list)
        objectList = copy.deepcopy(stages["objects"])
        stages = copy.deepcopy(stages["stages"])
        register = 0
        for counter in range(0, len(stages)):
            if ("remove" in stages[counter].keys()):
                register += 1
        self.assertEqual(register, len(stages))


if __name__ == '__main__':
    unittest.main()
