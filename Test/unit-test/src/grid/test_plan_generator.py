import unittest
import sys
sys.path.append('../../../../server/app/vfg/')
import pparser.plan_generator as step1
import re

class MyTestCase(unittest.TestCase):
    # Test if the returning value from the API is not empty
    # Input: a standard grid domain pddl file and a problem pddl file
    # Output: a non-empty plan json file.
    def test_integration_api_result(self):
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()
        plan = step1.get_plan(domain_file, problem_file)

        text = ''.join(str(e) for e in plan)
        self.assertTrue(text)

    # Test if the returning value from the API is correct
    # This is the most important guard.
    # If this test case can pass, then it means the input domain/problem are correct
    # Input: a standard grid domain pddl file and a problem pddl file
    # Output: "ok" should be the status code in the returned plan
    def test_integration_api_result(self):
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()
        plan = step1.get_plan(domain_file, problem_file, "")
        result = False
        if "ok" in plan["status"]:
            result = True
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
