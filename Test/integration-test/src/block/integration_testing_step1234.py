
import unittest
import json
import re
import sys
sys.path.append('../../../../server/PddLparser/visualiserFile/')
import PredicateParser.plan_generator as step1
import PredicateParser.problem_parser as step2
import PredicateParser.predicates_generator as step3
import generator.visualisation_generator as step4
import PredicateParser.domain_parser as dom_par
import copy


class integration_testing_step1234(unittest.TestCase):
    # Test if the total amount of stages is still the same
    def test_integration_number_of_stages_step1234(self):
        # amount of stages from step 123
        domain_file = "../../input/domain_blocks.pddl"
        problem_file = "../../input/bw08.pddl"
        predicates_list = dom_par.get_domain_json("../../input/domain_blocks.pddl")
        plan = step1.get_plan(domain_file, problem_file)
        problem_json = step2.get_problem_json(problem_file,predicates_list)
        stages = step3.get_stages(plan, problem_json, problem_file,predicates_list)
        objectList = copy.deepcopy(stages["objects"])
        stages = copy.deepcopy(stages["stages"])
        register = 1
        for counter in range(0, len(stages)):
            if ("add" in stages[counter].keys()):
                register += 1

        # amount of stages from step 4
        fileop = open("../../input/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]
        self.assertTrue(len(st) == register)

    # Test if the each stage has prefab definition
    def test_integration_number_of_prefabs_step1234(self):
        # amount of stages from step 4
        fileop = open("../../input/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]

        register = 0
        for counter in range(0, len(st)):
            blockexist = st[counter]['visualSprites'][0]['prefab']
            register += 1
        self.assertTrue(len(st) == register)

    # Test if the each stage has showName definition
    def test_integration_number_of_shownames_step1234(self):
        # amount of stages from step 4
        fileop = open("../../input/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]

        register = 0
        for counter in range(0, len(st)):
            showname = st[counter]['visualSprites'][0]['showName']
            if len(str(showname)) > 0:
                register += 1
        self.assertTrue(len(st) == register)

    # Test if the each stage has x definition
    def test_integration_number_of_xs_step1234(self):
        # amount of stages from step 4
        fileop = open("../../input/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]

        register = 0
        num_format = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
        for counter in range(0, len(st)):
            xvalue = st[counter]['visualSprites'][0]['x']
            if isinstance(xvalue, int) :
                register += 1
        self.assertTrue(len(st) == register)

    # Test if the each stage has y definition
    def test_integration_number_of_ys_step1234(self):
        # amount of stages from step 4
        fileop = open("../../input/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]

        register = 0
        num_format = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
        for counter in range(0, len(st)):
            yvalue = st[counter]['visualSprites'][0]['y']
            if isinstance(yvalue, int):
                register += 1
        self.assertTrue(len(st) == register)

    # Test if the each stage has width definition
    def test_integration_number_of_widths_step1234(self):
        # amount of stages from step 4
        fileop = open("../../input/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]

        register = 0
        num_format = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
        for counter in range(0, len(st)):
            widthvalue = st[counter]['visualSprites'][0]['width']
            if isinstance(widthvalue, int):
                register += 1
        self.assertTrue(len(st) == register)

    # Test if the each stage has height definition
    def test_integration_number_of_heights_step1234(self):
        # amount of stages from step 4
        fileop = open("../../input/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]

        register = 0
        num_format = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
        for counter in range(0, len(st)):
            heightvalue = st[counter]['visualSprites'][0]['height']
            if isinstance(heightvalue, int):
                register += 1
        self.assertTrue(len(st) == register)

    # Test if the each stage has panel definition
    def test_integration_bounday_limit_step1234(self):
        # amount of stages from step 4
        fileop = open("../../input/visualisation.json")
        strfile = fileop.read()
        st = json.loads(strfile)["visualStages"]

        register = 0
        num_format = re.compile("^[\-]?[1-9][0-9]*\.?[0-9]+$")
        for counter in range(0, len(st)):
            minX = st[counter]['visualSprites'][0]['minX']
            maxX = st[counter]['visualSprites'][0]['maxX']
            minY = st[counter]['visualSprites'][0]['minY']
            maxY = st[counter]['visualSprites'][0]['maxY']

            if isinstance(minX, float) and isinstance(maxX, float)and \
                    isinstance(minY, float) and isinstance(maxY, float):
                register += 1
        self.assertTrue(len(st) == register)


if __name__ == '__main__':
    unittest.main()
