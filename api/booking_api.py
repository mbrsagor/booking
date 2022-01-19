from rest_framework import views, serializers, status, permissions
from rest_framework.response import Response

from rent.models import Booking
from rent.utils.responses import prepare_success_response, prepare_error_response, prepare_create_success_response


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'id', 'customer', 'rent_name', 'address', 'status', 'phone_number', 'transaction_id',
            'booking_purpose', 'payment_type', 'booking_date', 'checkout_date', 'created_at', 'updated_at'
        )


class BookingAPIListCreateView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        location = Booking.objects.all()
        serializer = BookingSerializer(location, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(customer=request.user)
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)


class BookingUpdateDetailAPI(views.APIView):
    permission_classes = [permissions.IsAdminUser, ]

    def get_object(self, pk):
        try:
            return Booking.objects.get(id=pk).first()
        except Booking.DoesNotExist:
            return None

    def put(self, request, pk):
        booking = self.get_object(pk)
        if booking is not None:
            serializer = BookingSerializer(booking, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(prepare_create_success_response(serializer.data), status=status.HTTP_201_CREATED)
            return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(prepare_error_response("No data found for this ID"), status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        booking = self.get_object(pk)
        serializer = BookingSerializer(booking)
        if serializer is not None:
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        return Response(prepare_error_response("Content Not found"), status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        booking = self.get_object(pk)
        if booking is not None:
            booking.delete()
            return Response(prepare_success_response("Data deleted successfully"), status=status.HTTP_200_OK)
        else:
            return Response(prepare_error_response("Content Not found"), status=status.HTTP_400_BAD_REQUEST)
