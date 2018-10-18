import unittest
import sys
sys.path.append('../../../../server/app/vfg/')
import pparser.domain_parser as step1
import re

class MyTestCase(unittest.TestCase):
    # To check if the function can be parsed
    # Input: a standard grid domain pddl file.
    # Output: a non-empty parsed json file.
    def test_output_is_not_empty(self):
        domain_file = open("../../input/domain_grid.pddl", 'r').read()

        test_output = step1.get_domain_json(domain_file)
        self.assertTrue(test_output)

    # To check if the function can be parsed completely
    # Input: a list of standard grid predicates
    # Output: each predicate should present in the final output.
    def test_output_contains_all_items(self):
        domain_file = open("../../input/domain_grid.pddl", 'r').read()
        result = False
        test_input = "(key-shape ?k ?s) " \
                     "(lock-shape ?x ?s) " \
                     "(at ?r ?x )(at-robot ?x)" \
                     "(place ?p)(key ?k)(shape ?s)" \
                     "(locked ?x)(holding ?k)(open ?x)" \
                     "(arm-empty )"
        test_output = step1.get_domain_json(domain_file)
        for k, v in test_output.items():
            if k in test_output:
                result = True
            else:
                result = False
                break
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
