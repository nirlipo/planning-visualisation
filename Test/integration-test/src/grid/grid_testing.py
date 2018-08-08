import unittest
import json
import re
import sys
import server.PddLparser.visualiserFile.pparser.plan_generator as step1
import server.PddLparser.visualiserFile.pparser.problem_parser as step2
import server.PddLparser.visualiserFile.pparser.predicates_generator as step3
import server.PddLparser.visualiserFile.generator.visualisation_generator as step4
import server.PddLparser.visualiserFile.pparser.domain_parser as dom_par
import copy


class integration_testing_step123(unittest.TestCase):
    # Test if the total amount of stages is still the same
    def test_integration_number_of_stages_step1234(self):
        # the amount of stages generated
        domain_file = "../../input/domain_grid.pddl"
        problem_file = "../../input/gw01.pddl"
        predicates_list = dom_par.get_domain_json("../../input/domain_grid.pddl")
        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file, predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        objectList = copy.deepcopy(stages["objects"])
        stages = copy.deepcopy(stages["stages"])
        register = 1
        for counter in range(0, len(stages)):
            if ("add" in stages[counter].keys()):
                register += 1

        self.assertTrue(register - 1 == plan['result']['length'])


if __name__ == '__main__':
    unittest.main()
