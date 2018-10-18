import unittest
import sys
sys.path.append('../../../../server/PddLparser/visualiserFile/')
import pparser.plan_generator as step1
import pparser.domain_parser as step2
import hashlib
# Test plan_generator.py
#      domain_parser.py
class integration_testing_step12(unittest.TestCase):

    # check that none of the two components can change the content of domain file
    def test_file_modify(self):
        domain_file = open("../../../testfile/hanoi/domain.pddl", 'r').read()
        problem_file = open("../../../testfile/hanoi/pfile8.pddl", 'r').read()
        url = 'http://bfws-preference.herokuapp.com/solve'
        # md value of the domain file before calling the function
        f1 = domain_file
        step1.get_plan(domain_file, problem_file, url)
        step2.get_domain_json(domain_file)
        # md value of the domain file after calling the function
        f2 = domain_file
        md_before = hashlib.md5(f1.encode('utf-8')).hexdigest()
        md_after = hashlib.md5(f2.encode('utf-8')).hexdigest()
        self.assertEqual(md_after,md_before)

    #The input is hanoi domain PDDL file,
    # check that the amount of predicates is correct
    def test_predicates_amount(self):
        domain_file = open("../../../testfile/hanoi/domain.pddl", 'r').read()
        predicates_list = step2.get_domain_json(domain_file)
        count = 0
        for predicate in predicates_list:
            count += 1
        # Given the hanoi domain file, there are 3 predicates.
        Num = 3
        self.assertEqual(count, Num)

    # Check that the number of object for predicate "on" is 2
    def test_predicates_conn_correct(self):
        domain_file = open("../../../testfile/hanoi/domain.pddl", 'r').read()
        predicates_list = step2.get_domain_json(domain_file)
        print(predicates_list)
        value = 0
        if "on" in predicates_list:
            value = predicates_list['on']
        self.assertEqual(value, 2)

    # Check that the number of object for predicate "smaller" is 2
    def test_predicates_holding_correct(self):
        domain_file = open("../../../testfile/hanoi/domain.pddl", 'r').read()
        predicates_list = step2.get_domain_json(domain_file)
        value = 0
        if "smaller" in predicates_list:
            value = predicates_list['smaller']
        self.assertEqual(value, 2)

    # Check that the number of object for predicate "clear" is 1
    def test_predicates_holding_correct(self):
        domain_file = open("../../../testfile/hanoi/domain.pddl", 'r').read()
        predicates_list = step2.get_domain_json(domain_file)
        value = 0
        if "clear" in predicates_list:
            value = predicates_list['clear']
        self.assertEqual(value, 1)


if __name__ == '__main__':
    unittest.main()
