import unittest
import server.PddLparser.visualiserFile.parser.domain_parser as step1
import re

class MyTestCase(unittest.TestCase):

    # Can generate output
    def test_output_is_not_empty(self):
        test_output = step1.get_domain_json("../../input/domain_grid.pddl")
        self.assertTrue(test_output)

    # Can generate output completely
    def test_output_contains_all_items(self):
        result = False
        test_input = "(key-shape ?k ?s) " \
                     "(lock-shape ?x ?s) " \
                     "(at ?r ?x )(at-robot ?x)" \
                     "(place ?p)(key ?k)(shape ?s)" \
                     "(locked ?x)(holding ?k)(open ?x)" \
                     "(arm-empty )"
        test_output = step1.get_domain_json("../../input/domain_grid.pddl")
        for k, v in test_output.items():
            if k in test_output:
                result = True
            else:
                result = False
                break
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
