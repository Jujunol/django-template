from rest_framework import serializers
from .models import Record


class RecordSerializer(serializers.ModelSerializer):

    # Necessary to override the owner field with it's username value 
    # as type 'User' is not serializable
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Record
        fields = (
            'id',
            'name',
            'owner',
        )
        read_only_fields = (
        )
