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


class InfoUnitSerializer(serializers.ModelSerializer):

    date = serializers.DateTimeField(source="information_date.information_date")

    class Meta:

        model = MetrobusUnitInformation

        fields = ('date', 'position_longitude', 'position_latitude', 'alcaldia')


class AlcaldiaSerializer(serializers.ModelSerializer):

    class Meta:

        model = MetrobusUnitInformation

        fields = ('alcaldia',)


class AlcaldiaUnitSerializer(serializers.ModelSerializer):

    date = serializers.DateTimeField(source="information_date.information_date")

    class Meta:

        model = MetrobusUnitInformation

        fields = ('vehicle_id', 'date', 'position_longitude', 'position_latitude',)
