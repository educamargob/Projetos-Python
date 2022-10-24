from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.utils import timezone
from django_apscheduler.models import DjangoJobExecution
import sys
from fcm_django.models import FCMDevice
from usuarios.models import Mensagens
from firebase_admin.messaging import Message, Notification, WebpushNotification, WebpushConfig

# This is the function you want to schedule - add as many as you want and then register them in the start() function below
def deactivate_expired_accounts():
    today = timezone.now()
    ...
    # get accounts, expire them, etc.
    ...


def teste():
    mensagens = Mensagens.objects.order_by('-data_criacao').filter(habilitada=True)
    x = 0
    device = FCMDevice.objects.all().first()
    # device.send_message(Message(notification=Notification(title='comida', body='comida', image='https://blog.consumer.com.br/wp-content/uploads/2020/11/culin%C3%A1ria-regional-brasileira.jpg')))
    # device.send_message(Message(webpush=WebpushConfig(notification=WebpushNotification(title='comida', body='comida', image='https://blog.consumer.com.br/wp-content/uploads/2020/11/culin%C3%A1ria-regional-brasileira.jpg', icon='https://universo.adami.com.br/static/user/assets/images/logo_universo.png'))))
    for mensagem in mensagens:
        icone = ''
        if mensagem.icon:
            icone = mensagem.icon.url
        else:
            icone = 'https://universo.adami.com.br/static/user/assets/images/logo_universo.png'
        device.send_message(Message(webpush=WebpushConfig(notification=WebpushNotification(title=mensagem.titulo, body=mensagem.corpo_mensagem, image=mensagem.icon.url, icon=icone))))
         

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    # run this job every 24 hours
    scheduler.add_job(teste, 'interval', minutes=1, name='clean_accounts', jobstore='default')
    register_events(scheduler)
    scheduler.start()
    print("Scheduler started...", file=sys.stdout)