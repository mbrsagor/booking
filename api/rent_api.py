from rest_framework import views, serializers, status, permissions
from rest_framework.response import Response

from rent.models import Rent
from rent.utils.responses import prepare_success_response, prepare_error_response


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = (
            'id', 'name', 'bed_room', 'bath_room', 'price', 'rent_location', 'types', 'is_available', 'descriptions',
            'image', 'gallery_image', 'gallery_image2', 'gallery_image3', 'created_at', 'updated_at'
        )


class RentAPIListCreateView(views.APIView):
    permission_classes = [permissions.IsAdminUser, ]

    def get(self, request):
        location = Rent.objects.all()
        serializer = RentSerializer(location, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RentUpdateDetailDeleteAPIView(views.APIView):
    permission_classes = [permissions.IsAdminUser, ]

    def get_object(self, pk):
        try:
            return Rent.objects.get(id=pk)
        except Rent.DoesNotExist:
            return None

    def get(self, request, pk):
        rent = self.get_object(pk)
        serializer = RentSerializer(rent)
        if serializer is not None:
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        return Response(prepare_error_response("Content Not found"), status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        rent = self.get_object(pk)
        if rent is not None:
            return Response(prepare_success_response("Data deleted successfully"), status=status.HTTP_200_OK)
        else:
            return Response(prepare_error_response("Content Not found"), status=status.HTTP_400_BAD_REQUEST)
