from rest_framework import views, generics, status
from rest_framework.response import Response
from django.db import transaction


from metrobus.models import UpdateInformation, MetrobusUnitInformation
from metrobus.serializaers import InformationSerializer, UnitSerializer, \
    DisponiblesSerializer, InfoUnitSerializer, AlcaldiaSerializer, AlcaldiaUnitSerializer
from Arkon.paginator import Paginator


import json as js
from datetime import datetime
import pytz
import requests

from geopy.geocoders import Nominatim

utc=pytz.UTC

class GetRemoteInfo(generics.GenericAPIView):

    def get(self, request):

        url = "https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=prueba_fetchdata_metrobus&q=&rows=1"

        payload = {}
        headers = {
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        if response.status_code == 200:
            incoming_event = js.loads(response.text)
            try:

                last_transactions = UpdateInformation.objects.filter().order_by('-information_date')[:1][0].information_date
                incoming_event_timestamp = datetime.strptime(incoming_event['records'][0]['fields']['date_updated'], "%Y-%m-%d %H:%M:%S")
                if incoming_event_timestamp.replace(tzinfo=pytz.utc) > last_transactions.replace(tzinfo=pytz.utc):
                    all_elements = self.complete_request(limit=str(incoming_event['nhits']))
                else:
                    return Response(status=status.HTTP_412_PRECONDITION_FAILED)

            except Exception as e:
                all_elements = self.complete_request(limit=str(incoming_event['nhits']))

            with transaction.atomic():

                data = {
                    "information_date": incoming_event_timestamp.replace(tzinfo=pytz.utc)
                }
                serializer = InformationSerializer(data=data)

                serializer.is_valid(raise_exception=True)
                serializer.save()

                geolocator = Nominatim(user_agent="arkon_herver")
                i = 1
                for element in all_elements['records']:
                    print("{} de {}".format(i, len(all_elements['records'])))

                    location = geolocator.reverse("{}, {}".format(element['fields']['position_latitude'], element['fields']['position_longitude']))

                    try:
                        data={
                            "information_date": serializer.data['id'],
                            "vehicle_id": element['fields']['vehicle_id'],
                            "position_longitude": element['fields']['position_longitude'],
                            "position_latitude": element['fields']['position_latitude'],
                            "alcaldia": location.raw['address']['county']
                            if 'county' in location.raw['address']['county'] else ""

                        }

                        unit_serializer = UnitSerializer(data=data)

                        unit_serializer.is_valid(raise_exception=True)
                        unit_serializer.save()
                    except:
                        print(location.address, )
                    i += 1

                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_202_ACCEPTED)

    def complete_request(self, limit="1"):
        url = "https://datos.cdmx.gob.mx/api/records/1.0/search/?dataset=prueba_fetchdata_metrobus&q=&rows={}".format(limit)

        payload = {}
        headers = {
        }

        return js.loads((requests.request("GET", url, headers=headers, data=payload)).text)



class MetrobusDisponibles(generics.ListAPIView):
    serializer_class = DisponiblesSerializer
    pagination_class = Paginator
    queryset = MetrobusUnitInformation.objects.all().values('vehicle_id').distinct().order_by('vehicle_id')


class InfoUnit(generics.ListAPIView):
    serializer_class = InfoUnitSerializer
    pagination_class = Paginator

    def get_queryset(self):
        queryset = MetrobusUnitInformation.objects.filter(vehicle_id=self.kwargs['unit_id'])\
            .order_by('-information_date__information_date')
        return queryset


class Alcaldias(generics.ListAPIView):
    serializer_class = AlcaldiaSerializer
    pagination_class = Paginator

    def get_queryset(self):
        queryset = MetrobusUnitInformation.objects.all().values('alcaldia').distinct().order_by("-alcaldia")
        return queryset


class AlcaldiasUnit(generics.ListAPIView):
    serializer_class = AlcaldiaUnitSerializer
    pagination_class = Paginator

    def get_queryset(self):
        queryset = MetrobusUnitInformation.objects.filter(alcaldia=self.kwargs['alcaldia_id'])\
            .order_by('-information_date__information_date')
        return queryset
