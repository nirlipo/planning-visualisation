import sys
sys.path.append('../../../../server/PddLparser/visualiserFile/pparser')
import unittest
import plan_generator as step1

class integration_testing_step1(unittest.TestCase):
    # Test if the domain file is not empty
    def test_integration__input_domain_step_1(self):
        with open("../../input/domain_blocks.pddl", "r") as f1:
            domaintext = f1.read()
        self.assertTrue(domaintext)
        f1.close()

    # Test if the problem file is not empty
    def test_integration__input_problem_step_1(self):
        with open("../../input/bw08.pddl", "r") as f2:
            problemtext = f2.read()
        self.assertTrue(problemtext)
        f2.close()

    # Test if the returning value from the API is not empty
    def test_integration_api_result(self):
        with open("../../input/domain_blocks.pddl", "r") as f1:
            domaintext = f1.read()
        with open("../../input/bw08.pddl", "r") as f2:
            problemtext = f2.read()
        self.assertTrue(step1.get_plan(domaintext, problemtext, ""))

if __name__ == "__main__":
    unittest.main()
