import unittest
import json
import re
import sys
sys.path.append('../../../../server/PddLparser/visualiserFile/')
import pparser.plan_generator as step1
import pparser.problem_parser as step2
import pparser.predicates_generator as step3
import adapter.transfer as step4
import pparser.domain_parser as dom_par
import copy


class integration_testing_step123(unittest.TestCase):
    # Test if the total amount of stages is still the same
    def test_integration_number_of_stages_step1234(self):
        # the amount of stages generated
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()

        predicates_list = dom_par.get_domain_json(domain_file)
        plan = step1.get_plan(domain_file, problem_file, "")
        problem_json = step2.get_problem_json(problem_file, predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        objectList = copy.deepcopy(stages["objects"])
        stages = copy.deepcopy(stages["stages"])
        register = 0
        for counter in range(0, len(stages)):
            if ("add" in stages[counter].keys()):
                register += 1

        self.assertTrue(register - 1 == plan['result']['length'])


if __name__ == '__main__':
    unittest.main()
