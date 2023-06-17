from rest_framework import serializers

from loans.models import Loan


class LoanSerializer(serializers.ModelSerializer):
    return_at = serializers.DateField(read_only=True)

    class Meta:
        model = Loan
        fields = ['id', 'return_at', 'created_at', 'user', 'book']