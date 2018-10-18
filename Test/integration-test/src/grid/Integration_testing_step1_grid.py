import unittest
import sys
sys.path.append('../../../../server/app/vfg/')
import pparser.plan_generator as step1

# Test Plan_generator.py
class integration_testing_step1(unittest.TestCase):

    # test if the inputs are all correct, then the api can return
    # correct solution with status "ok"
    def test_correct_inputs(self):
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()
        plan = step1.get_plan(domain_file, problem_file, "")
        if "status" in plan:
            st = plan["status"]
        print(st)
        self.assertTrue(st == "ok")

    # test if problem file is empty,
    # api will return result with "error" status
    def test_empty_problem_file(self):
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/empty.pddl", 'r').read()
        plan = step1.get_plan(domain_file, problem_file, "")
        if "status" in plan:
            st = plan["status"]
        self.assertTrue(st == "error")

    # test if domain file is empty,
    # api will return result with "error" status
    def test_empty_domain_file(self):
        domain_file = open("../../input/empty.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()
        plan = step1.get_plan(domain_file, problem_file, "")
        if "status" in plan:
            st = plan["status"]
        self.assertTrue(st == "error")

    # test if domain file is wrong,
    # api will return result with "error" status
    def test_wrong_domain_file(self):
        domain_file = open("../../input/domain_grid_wrong.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()
        plan = step1.get_plan(domain_file, problem_file, "")
        if "status" in plan:
            st = plan["status"]
        self.assertTrue(st == "error")

    # test if problem file is wrong,
    # api will return result with "error" status
    def test_wrong_problem_file(self):
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01_wrong.pddl", 'r').read()
        plan = step1.get_plan(domain_file, problem_file, "")
        if "status" in plan:
            st = plan["status"]
        self.assertTrue(st == "error")

if __name__ == '__main__':
    unittest.main()
