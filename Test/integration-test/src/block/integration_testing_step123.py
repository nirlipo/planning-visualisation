import unittest
import sys
sys.path.append('../../../../server/PddLparser/visualiserFile/')
import pparser.plan_generator as step1
import pparser.problem_parser as step2
import pparser.predicates_generator as step3
import pparser.domain_parser as dom_par
import copy

class test_integration_step123(unittest.TestCase):
    # Test if the output is not empty
    def test_integration_predicate_each_stage_step123(self):
        domain_file = open("../../input/domain_blocks.pddl", 'r').read()
        problem_file = open("../../input/bw08.pddl", 'r').read()
        predicates_list = dom_par.get_domain_json(open("../../input/domain_blocks.pddl", 'r').read())
        plan = step1.get_plan(domain_file, problem_file, "")
        problem_json = step2.get_problem_json(problem_file,predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        self.assertTrue(stages)

    # Test if the output contains an object list
    def test_integration_predicates_object_list_step123(self):
        domain_file = open("../../input/domain_blocks.pddl", 'r').read()
        problem_file = open("../../input/bw08.pddl", 'r').read()
        predicates_list = dom_par.get_domain_json(open("../../input/domain_blocks.pddl", 'r').read())
        plan = step1.get_plan(domain_file, problem_file, "")
        problem_json = step2.get_problem_json(problem_file,predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        objectList = copy.deepcopy(stages["objects"])
        self.assertTrue(len(objectList) > 1)

    # Test if the output stages should contain at least the init and goal stage
    def test_integration_predicates_stages_step123(self):
        domain_file = open("../../input/domain_blocks.pddl", 'r').read()
        problem_file = open("../../input/bw08.pddl", 'r').read()
        predicates_list = dom_par.get_domain_json(open("../../input/domain_blocks.pddl", 'r').read())
        plan = step1.get_plan(domain_file, problem_file, "")
        problem_json = step2.get_problem_json(problem_file,predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        stages = copy.deepcopy(stages["stages"])
        self.assertTrue(len(stages) > 2)

    # Test if each stage has an adequate amount of objects
    def test_integration_predicates_stage_size_step123(self):
        domain_file = open("../../input/domain_blocks.pddl", 'r').read()
        problem_file = open("../../input/bw08.pddl", 'r').read()
        predicates_list = dom_par.get_domain_json(open("../../input/domain_blocks.pddl", 'r').read())
        plan = step1.get_plan(domain_file, problem_file, "")
        problem_json = step2.get_problem_json(problem_file,predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        objectList = copy.deepcopy(stages["objects"])
        stages = copy.deepcopy(stages["stages"])
        register = 0
        for counter in range(0, len(stages)):
            if len(stages[counter]) > 1:
                register += 1
        self.assertTrue(register > 2)

    # Test if each stage has an adequate amount of add actions
    def test_integration_predicates_add1_step123(self):
        domain_file = open("../../input/domain_blocks.pddl", 'r').read()
        problem_file = open("../../input/bw08.pddl", 'r').read()
        predicates_list = dom_par.get_domain_json(open("../../input/domain_blocks.pddl", 'r').read())
        plan = step1.get_plan(domain_file, problem_file, "")
        problem_json = step2.get_problem_json(problem_file,predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        objectList = copy.deepcopy(stages["objects"])
        stages = copy.deepcopy(stages["stages"])
        register = 0
        for counter in range(0, len(stages)):
            if("add" in stages[counter].keys()):
                register += 1
        self.assertEqual(register,len(stages))

    # Test if each stage has an adequate amount of remove actions
    def test_integration_predicates_add2_step123(self):
        domain_file = open("../../input/domain_blocks.pddl", 'r').read()
        problem_file = open("../../input/bw08.pddl", 'r').read()
        predicates_list = dom_par.get_domain_json(open("../../input/domain_blocks.pddl", 'r').read())
        plan = step1.get_plan(domain_file, problem_file, "")
        problem_json = step2.get_problem_json(problem_file,predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        objectList = copy.deepcopy(stages["objects"])
        stages = copy.deepcopy(stages["stages"])
        register = 0
        for counter in range(0, len(stages)):
            if("remove" in stages[counter].keys()):
                register += 1
        self.assertEqual(register,len(stages))

if __name__ == '__main__':
    unittest.main()
