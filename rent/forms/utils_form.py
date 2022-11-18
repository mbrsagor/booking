from rest_framework import views, status, serializers
from rest_framework.response import Response

from rent.models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class CategoryUtilsAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        pass


