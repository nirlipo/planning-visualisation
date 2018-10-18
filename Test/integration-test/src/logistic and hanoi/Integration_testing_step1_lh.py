import unittest
import sys

sys.path.append('../../../../server/PddLparser/visualiserFile/')
import pparser.plan_generator as step1


# Test plan_generator.py
class integration_testing_step1(unittest.TestCase):

    # test if the inputs are all correct, then the api can return
    # correct solution with status "ok"
    def test_correct_inputs(self):
        domain_file = open("../../../testfile/hanoi/domain.pddl", 'r').read()
        problem_file = open("../../../testfile/hanoi/pfile8.pddl", 'r').read()
        url = 'http://bfws-preference.herokuapp.com/solve'
        plan = step1.get_plan(domain_file, problem_file, url)
        if "status" in plan:
            st = plan["status"]
        print(st)
        self.assertTrue(st == "ok")

    # test if the inputs are all correct, then the api can return
    # correct solution with status "ok"
    def test_correct_inputs1(self):
        domain_file = open("../../../testfile/hanoi/domain.pddl", 'r').read()
        problem_file = open("../../../testfile/hanoi/pfile8.pddl", 'r').read()
        url = ''
        plan = step1.get_plan(domain_file, problem_file, url)
        if "status" in plan:
            st = plan["status"]
        self.assertTrue(st == "ok")

    # api will return result with "error"
    # test if problem file is empty, status
    def test_empty_problem_file(self):
        domain_file = open("../../../testfile/hanoi/domain.pddl", 'r').read()
        problem_file = open("../../input/empty.pddl", 'r').read()
        url = 'http://bfws-preference.herokuapp.com/solve'
        plan = step1.get_plan(domain_file, problem_file, url)
        if "status" in plan:
            st = plan["status"]
        self.assertTrue(st == "error")

    # test if domain file is empty,
    # api will return result with "error" status
    def test_empty_domain_file(self):
        domain_file = open("../../input/empty.pddl", 'r').read()
        problem_file = open("../../../testfile/hanoi/pfile8.pddl", 'r').read()
        url = 'http://bfws-preference.herokuapp.com/solve'
        plan = step1.get_plan(domain_file, problem_file, url)
        if "status" in plan:
            st = plan["status"]
        self.assertTrue(st == "error")

    # test if domain file is wrong,
    # api will return result with "error" status
    def test_wrong_domain_file(self):
        domain_file = open("../../input/domain_grid_wrong.pddl", 'r').read()
        problem_file = open("../../../testfile/hanoi/pfile8.pddl", 'r').read()
        url = 'http://bfws-preference.herokuapp.com/solve'
        plan = step1.get_plan(domain_file, problem_file, url)
        if "status" in plan:
            st = plan["status"]
        self.assertTrue(st == "error")

    # test if problem file is wrong,
    # api will return result with "error" status
    def test_wrong_problem_file(self):
        domain_file = open("../../../testfile/hanoi/domain.pddl", 'r').read()
        problem_file = open("../../input/gw01_wrong.pddl", 'r').read()
        url = 'http://bfws-preference.herokuapp.com/solve'
        plan = step1.get_plan(domain_file, problem_file, url)
        if "status" in plan:
            st = plan["status"]
        self.assertTrue(st == "error")


if __name__ == '__main__':
    unittest.main()
