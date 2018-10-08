import unittest
import sys
import json
sys.path.append('../../../../server/PddLparser/visualiserFile/')
import pparser.plan_generator as step1
import pparser.problem_parser as step2
import pparser.predicates_generator as step3
import pparser.domain_parser as dom_par
import pparser.animation_parser as ap
import copy


class integration_testing_step123(unittest.TestCase):
    # Test if the total amount of stages is still the same
    def test_integration_number_of_stages_step1234(self):
        # the amount of stages generated
        domain_file = open("../../../testfile/hanoi/domain.pddl", 'r').read()
        problem_file = open("../../../testfile/hanoi/pfile8.pddl", 'r').read()
        url = 'http://bfws-preference.herokuapp.com/solve'
        predicates_list = dom_par.get_domain_json(domain_file)
        plan = step1.get_plan(domain_file, problem_file, url)
        problem_json = step2.get_problem_json(problem_file, predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        objectList = copy.deepcopy(stages["objects"])
        stages = copy.deepcopy(stages["stages"])
        register = 0
        re = 0
        for counter in range(0, len(stages)):
            if ("add" in stages[counter].keys()):
                register += 1
        fileop = open("../../input/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]
        self.assertTrue(register - 1 == plan['result']['length'])

    # Test if the final output is correct
    def test_integration_number_of_object_step1234(self):
        # the amount of info generated
        domain_file = open("../../../testfile/hanoi/domain.pddl", 'r').read()
        problem_file = open("../../../testfile/hanoi/pfile8.pddl", 'r').read()
        url = 'http://bfws-preference.herokuapp.com/solve'
        predicates_list = dom_par.get_domain_json(domain_file)
        plan = step1.get_plan(domain_file, problem_file, url)
        problem_json = step2.get_problem_json(problem_file, predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)

        fileop = open("../../../testfile/animationpddl/hanoi.pddl", 'r').read()
        testjson1 = ap.get_animation_profile(fileop)
        testjson = open("../../../integration-test/input/testjson.json",'r').read()
        self.assertEquals(testjson,testjson1)

if __name__ == '__main__':
    unittest.main()
