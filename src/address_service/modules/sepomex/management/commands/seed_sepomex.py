import os, sys

from django.core.management.base import BaseCommand
from django.utils import timezone

from address_service.modules.sepomex.models import Sepomex

class Command(BaseCommand):
    help = 'Fill sepomex table from txt file'

    def handle(self, *args, **kwargs):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file = '{}/CPdescarga.txt'.format(BASE_DIR)
        with open(file, encoding="ISO-8859-1") as fp:
            counter = 0
            for line in fp:
                counter = counter + 1
                if(counter > 2):
                    row_list = line.split("|")   
                    sepomex = Sepomex.objects.create(
                        d_codigo = row_list[0],
                        d_asenta = row_list[1],
                        d_tipo_asenta = row_list[2],
                        D_mnpio = row_list[3],
                        d_estado = row_list[4],
                        d_ciudad = row_list[5],
                        d_CP = row_list[6],
                        c_estado = row_list[7],
                        c_oficina = row_list[8],
                        c_CP = row_list[9],
                        c_tipo_asenta = row_list[10],
                        c_mnpio = row_list[11],
                        id_asenta_cpcons = row_list[12],
                        d_zona = row_list[13],
                        c_cve_ciudad = row_list[14]
                    )