from rest_framework import serializers
from Blog.models import *


class PostSeri(serializers.ModelSerializer):
     class Meta:
        model= Posts
        fields='__all__'


