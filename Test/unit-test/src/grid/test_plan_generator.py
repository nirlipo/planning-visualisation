import unittest
import server.PddLparser.visualiserFile.parser.plan_generator as step1
import re

class MyTestCase(unittest.TestCase):

    # Test if the returning value from the API is not empty
    def test_integration_api_result(self):
        plan = step1.get_plan("../../input/domain_grid.pddl", "../../input/gw01.pddl")
        text = ''.join(str(e) for e in plan)
        self.assertTrue(text)

    # Test if the returning value from the API is correct
    def test_integration_api_result(self):
        plan = step1.get_plan("../../input/domain_grid.pddl", "../../input/gw01.pddl")
        result = False
        if "ok" in plan["status"]:
            result = True
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
