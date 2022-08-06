from django.apps import AppConfig


class RetailerConfig(AppConfig):
    name = 'retailer'

def ready(self):
	import users.signals