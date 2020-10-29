from django.core.management.base import BaseCommand

from deeppavlov.download import deep_download
from homepage.views import MODEL_CONFIG


class Command(BaseCommand):
    help = 'Warms up deep pavlov models'

    def handle(self, *args, **options):
        self.stdout.write('Downloading deep pavlov models')
        deep_download(MODEL_CONFIG)
        self.stdout.write(self.style.SUCCESS('Deep pavlov models are loaded'))
