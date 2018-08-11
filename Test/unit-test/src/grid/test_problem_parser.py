import unittest
import sys
sys.path.append('../../../../server/PddLparser/visualiserFile/')
import pparser.plan_generator as step1
import pparser.problem_parser as step2
import pparser.predicates_generator as step3
import generator.visualisation_generator as step4
import pparser.domain_parser as dom_par

class MyTestCase(unittest.TestCase):
    #  Test get_problem_json to see if it can generate an output correctly
    # Input: a standard grid domain pddl file and a problem pddl file
    # Output: a non-empty problem json  (without any special character)
    def test_get_problem_json(self):
        # the amount of stages generated
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()
        predicates_list = dom_par.get_domain_json(domain_file)
        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file, predicates_list)

        self.assertTrue(problem_json)


if __name__ == '__main__':
    unittest.main()
