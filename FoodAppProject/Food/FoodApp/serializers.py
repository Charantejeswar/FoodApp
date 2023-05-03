from rest_framework.serializers import ModelSerializer
from .models import *

class Ser(ModelSerializer):
    class Meta:
        model = User
        fields = "__ALL__"