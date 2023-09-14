from django.dispatch import receiver
from django.db.models.signals import post_save
from realtys.models import Bill
from django.core.mail import send_mail


@receiver(post_save, sender=Bill)
def mail_sender(sender, instance, created, **kwargs):
    if created:
        name = instance.name
        email = instance.email
        subject = instance.subject
        message = instance.message
        from_email = 'plotnikov-d@bk.ru'
        email_manager = instance.email_manager
        recepient = ['plotnikov_da@npcses.ru', email, email_manager]
        send_mail(subject, message, from_email, recepient)


