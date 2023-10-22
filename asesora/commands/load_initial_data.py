from django.core.management.base import BaseCommand
from asesora.models import Comuna, Region

import json

class Command(BaseCommand):
    help = 'Carga datos iniciales desde un archivo JSON'

    def handle(self, *args, **options):
        with open('region-comuna.json', 'r') as json_file:
            data = json.load(json_file)
            for region_data in data['regiones']:
                region = Region.objects.create(region=region_data['region'])
                for comuna_name in region_data['comunas']:
                    Comuna.objects.create(region=region, descripcion=comuna_name)
        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente'))