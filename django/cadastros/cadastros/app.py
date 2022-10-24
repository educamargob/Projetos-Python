from django.apps import AppConfig

class CadastrosConfig(AppConfig):
    name = 'cadastros'
    def ready(self):
        from apps.scheduler import scheduler
        scheduler.start()
