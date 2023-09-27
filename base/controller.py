import threading
from django.core.mail import send_mail
from rest_framework.response import Response
from send_email.settings import EMAIL_HOST_USER


class EmailController:
    def send(self, request):
        try:
            subject = "Auto Generated Email"
            message = f"""
                Hi this is an auto generated email from django server
                """
            receiver_email = "hamzakhalil@joyn.com.pk"
            recipient_list = [receiver_email]
            t = threading.Thread(target=send_mail, args=(subject, message, EMAIL_HOST_USER, recipient_list))
            t.start()
            return Response('Email Successfully Sent', 200)

        except Exception as e:
            return Response('Unsuccessful', 500)