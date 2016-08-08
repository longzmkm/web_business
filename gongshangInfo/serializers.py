from rest_framework import serializers
from .models import company


class companySerializers(serializers.ModelSerializer):
    class Meta:
        model=company
        fields=['company_name','person_name','position_name','regNO']
