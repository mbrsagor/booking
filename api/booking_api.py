from rest_framework import views, serializers, status, permissions
from rest_framework.response import Response

from rent.models import Booking
from rent.utils.responses import prepare_success_response, prepare_error_response
from rent.utils.validate_service import validate_booking_service


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            'id', 'customer', 'rent_name', 'address', 'status', 'phone_number', 'transaction_id',
            'booking_purpose', 'payment_type', 'booking_date', 'checkout_date', 'created_at', 'updated_at'
        )


class BookingAPIListCreateView(views.APIView):
    # permission_classes = [permissions.IsAdminUser, ]

    def get(self, request):
        location = Booking.objects.all()
        serializer = BookingSerializer(location, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        validate_error = validate_booking_service(request.data)
        if validate_error is not None:
            return Response(prepare_error_response(validate_error), status=status.HTTP_400_BAD_REQUEST)
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(prepare_success_response(serializer.data), status=status.HTTP_200_OK)
        return Response(prepare_error_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
