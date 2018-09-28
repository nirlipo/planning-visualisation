from django.shortcuts import render
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' +"visualiserFile/pparser"))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' +"visualiserFile/adapter"))
import plan_generator  # Step1: get plan from planning domain api
import problem_parser  # Step2: parse problem pddl, to get the inital and goal stage
import predicates_generator  # Step3: manipulate the predicate for each step/stage
import transfer  # Step4. use the animation profile and stages from step3 to get the visualisation file
import domain_parser
import json
import io
import re
# Create your views here.
from PddLparser.models import PDDL
from PddLparser.serializers import PDDLSerializer

from rest_framework import viewsets
from rest_framework.parsers import BaseParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class PDDLViewSet(viewsets.ModelViewSet):
    queryset = PDDL.objects.all()
    serializer_class = PDDLSerializer
    
class PlainTextParser(BaseParser):
    """
    Plain text pparser.
    """
    media_type = 'text/plain'

    def parse(self, stream, media_type="text/plain", parser_context=None):
        """
        Simply return a string representing the body of the request.
        """
        return stream.read()
    
class LinkUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, filename, format=None):
        domain_file = request.data['domain']
        problem_file = request.data['problem']
        animation_file = json.loads(request.data['animation'])

        # add url
        if "url" in request.data:
            url_link = request.data['url']
        else:
            url_link = "http://solver.planning.domains/solve"



        predicates_list = domain_parser.get_domain_json(domain_file)
        plan = plan_generator.get_plan(domain_file, problem_file, url_link)
        problem_json = problem_parser.get_problem_json(problem_file,predicates_list)

        stages = predicates_generator.get_stages(plan, problem_json, problem_file,predicates_list)
        # A file called visualistaion.json will be generated in the folder if successful
        final = transfer.get_visualisation_json(stages,animation_file,plan['result']['plan'],problem_json)

        return Response(final)

