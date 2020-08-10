from rest_framework import serializers
from demo.models import Funds,Investment
class FundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funds
        fields = '__all__'

class InvestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = '__all__'

