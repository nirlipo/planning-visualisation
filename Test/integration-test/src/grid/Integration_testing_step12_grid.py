import unittest
import sys
sys.path.append('../../../../server/app/vfg/')
import pparser.plan_generator as step1
import pparser.domain_parser as step2
import os
import shutil
import hashlib
# Test Plan_generator.py
#      Domain_parser.py
class integration_testing_step12(unittest.TestCase):

    # check that none of the two components can change the content of domain file
    def test_file_modify(self):
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()
        # md value of the domain file before calling the function
        f1 = domain_file
        step1.get_plan(domain_file, problem_file, "")
        step2.get_domain_json(domain_file)
        # md value of the domain file after calling the function
        f2 = domain_file
        md_before = hashlib.md5(f1.encode('utf-8')).hexdigest()
        md_after = hashlib.md5(f2.encode('utf-8')).hexdigest()
        self.assertEqual(md_after,md_before)

    #The input is grid domain PDDL file,
    # check that the amount of predicates is correct
    def test_predicates_amount(self):
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()
        predicates_list = step2.get_domain_json(domain_file)
        count = 0
        for predicate in predicates_list:
            count += 1;
        # Given the grid domain file, there are 12 predicates.
        Num = 12
        self.assertEqual(count, Num)

    # Check that the number of object for predicate "conn" is 2
    def test_predicates_conn_correct(self):
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()
        predicates_list = step2.get_domain_json(domain_file)
        print(predicates_list)
        value = 0
        if "conn" in predicates_list:
            value = predicates_list['conn']
        self.assertEqual(value, 2)

    # Check that the number of object for predicate "holding" is 1
    def test_predicates_holding_correct(self):
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()
        predicates_list = step2.get_domain_json(domain_file)
        value = 0
        if "holding" in predicates_list:
            value = predicates_list['holding']
        self.assertEqual(value, 1)

    # Check that the number of object for predicate "arm-empty" is 0
    def test_predicates_holding_correct(self):
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        problem_file = open("../../input/gw01.pddl", 'r').read()
        predicates_list = step2.get_domain_json(domain_file)
        value = 0
        if "arm-empty" in predicates_list:
            value = predicates_list['arm-empty']
        self.assertEqual(value, 0)


if __name__ == '__main__':
    unittest.main()
