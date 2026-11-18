from rest_framework import serializers
from .models import ContactForm

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['name','phone','email','address','message','created_at']
        read_only_fields = ('created_at',)

        #read_only_fields = ['created_at']