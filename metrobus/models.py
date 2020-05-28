from django.db import models

import uuid


class UpdateInformation(models.Model):

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          unique=True,
                          )

    creation_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name="Fecha de Creacion")


    information_date = models.DateTimeField(null=False,
                                            blank=False,
                                            verbose_name="Fecha de la Informacion")


    def __srt__(self):
        return self.information_date


class MetrobusUnitInformation(models.Model):

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False,
                          unique=True,
                          )

    information_date = models.ForeignKey('metrobus.UpdateInformation',
                                         on_delete=models.CASCADE)

    vehicle_id = models.CharField(blank=False,
                                  null=False,
                                  max_length=10)

    position_longitude = models.FloatField(max_length=25,
                                           blank=False,
                                           null=False,
                                           )

    position_latitude = models.FloatField(max_length=25,
                                          blank=False,
                                          null=False,
                                          )

    alcaldia = models.CharField(max_length=25,
                                blank=False,
                                null=False,
                                )
