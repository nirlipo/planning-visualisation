from django.shortcuts import render
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' +"vfg/parser"))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' +"vfg/adapter"))
import plan_generator  # Step1: get plan from planning domain api
import problem_parser  # Step2: parse problem pddl, to get the inital and goal stage
import predicates_generator  # Step3: manipulate the predicate for each step/stage
import transfer  # Step4. use the animation profile and stages from step3 to get the visualisation file
import animation_parser
import domain_parser
import json
import io
import re
# Create your views here.
from app.models import PDDL
from app.serializers import PDDLSerializer

from rest_framework import viewsets
from rest_framework.parsers import BaseParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.
class PDDLViewSet(viewsets.ModelViewSet):
    queryset = PDDL.objects.all()
    serializer_class = PDDLSerializer
    
class PlainTextParser(BaseParser):
    """
    Plain text parser.
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
        try:
            domain_file = request.data['domain']
            problem_file = request.data['problem']
            animation_file = request.data['animation']

            # add url
            if "url" in request.data:
                url_link = request.data['url']
            else:
                url_link = "http://solver.planning.domains/solve"

            animation_profile = json.loads(animation_parser.get_animation_profile(animation_file))
            print(animation_profile["predicates_rules"])
            print ("!!!!!!",type(animation_profile))
            print(animation_profile)
            predicates_list = domain_parser.get_domain_json(domain_file)
            plan = plan_generator.get_plan(domain_file, problem_file, url_link)
            problem_json = problem_parser.get_problem_json(problem_file,predicates_list)

            stages = predicates_generator.get_stages(plan, problem_json, problem_file,predicates_list)
            # A file called visualistaion.json will be generated in the folder if successful
            final = transfer.get_visualisation_json(stages,animation_profile,plan['result']['plan'],problem_json)
        except Exception as e:
            message = repr(e)
            final = {"visualStages": [], "subgoalPool": {}, "subgoalMap": {}, "transferType": 0, "imageTable": {},
                     "message": str(message)}

        return Response(final)

    
class UserGuide(APIView):
    renderer_classes=[TemplateHTMLRenderer]
    template_name = 'UserGuide.html'
    
    def get(self,request):
        return Response({'':""})