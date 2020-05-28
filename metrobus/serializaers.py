from rest_framework import serializers

from metrobus.models import UpdateInformation, MetrobusUnitInformation


class InformationSerializer(serializers.ModelSerializer):

    class Meta:

        model = UpdateInformation

        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):

    class Meta:

        model = MetrobusUnitInformation

        fields = '__all__'


class DisponiblesSerializer(serializers.ModelSerializer):

    class Meta:

        model = MetrobusUnitInformation

        fields = ('vehicle_id', )
