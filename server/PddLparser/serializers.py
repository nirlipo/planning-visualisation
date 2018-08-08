from rest_framework import serializers
from PddLparser.models import PDDL


class PDDLSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDDL
        # fields = '__all__'
        fields = ('id', 'name', 'filetype','file')
