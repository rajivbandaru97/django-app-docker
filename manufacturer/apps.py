from django.apps import AppConfig


class ManufacturerConfig(AppConfig):
    name = 'manufacturer'

def ready(self):
	import users.signals