from rest_framework import views, serializers, status, permissions
from rest_framework.response import Response

from rent.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'id', 'name', 'parent', 'is_active', 'created_at', 'updated_at'
        )


class LocationAPIListCreateView(views.APIView):
    permission_classes = [permissions.IsAdminUser, ]

    def get(self, request):
        location = Location.objects.all()
        serializer = LocationSerializer(location, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
