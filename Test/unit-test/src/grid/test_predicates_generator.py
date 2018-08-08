import unittest
import sys
sys.path.append('../../../../server/PddLparser/visualiserFile/')
import pparser.plan_generator as step1
import pparser.problem_parser as step2
import pparser.predicates_generator as step3
import generator.visualisation_generator as step4
import pparser.domain_parser as dom_par

class MyTestCase(unittest.TestCase):
    # Test remove_unused_char
    def test_remove_unused_char(self):
        input = [{"action": "abc effect:bca"}]
        output = step3.remove_unused_char(input)
        result = True
        if "effect" in output:
            result = False
        self.assertTrue(result)

    #  Test get_stages to see if it can generate an output
    def test_get_stages_1(self):
        domain_file = "../../input/domain_grid.pddl"
        problem_file = "../../input/gw01.pddl"
        predicates_list = dom_par.get_domain_json("../../input/domain_grid.pddl")
        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file,predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        self.assertTrue(stages)

    #  Test get_stages to see if it can generate an output (length is correct)
    def test_get_stages_2(self):
        # the amount of stages generated
        domain_file = "../../input/domain_grid.pddl"
        problem_file = "../../input/gw01.pddl"
        predicates_list = dom_par.get_domain_json("../../input/domain_grid.pddl")
        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file, predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file, predicates_list)
        result = len(stages["stages"]) - 1 # minus initial stage

        # the amount of stages expected
        expect = plan['result']['length']
        self.assertTrue(result is expect)

    #  Test get_stages to see if it can generate an output correctly (without any special characters)
    def test_get_stages_3(self):
        # the amount of stages generated
        domain_file = "../../input/domain_grid.pddl"
        problem_file = "../../input/gw01.pddl"
        predicates_list = dom_par.get_domain_json("../../input/domain_grid.pddl")
        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file, predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file, predicates_list)
        result = True
        for counter1 in range(0, len(stages)):
            temp = stages["stages"][counter1]["items"]
            for counter2 in range(0, len(temp)):
                if " " in temp[counter2]["name"]:
                    result = False
                    break
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
