from rest_framework import serializers

from base.accounting.models import *


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'


class DepositAccountSerializer(serializers.ModelSerializer):
    type_display = serializers.SerializerMethodField()
    bank_display = serializers.SerializerMethodField()

    class Meta:
        model = DepositAccount
        fields = '__all__'

    def get_type_display(self, obj):
        return obj.get_type_display()

    def get_bank_display(self, obj):
        return str(obj.bank)
