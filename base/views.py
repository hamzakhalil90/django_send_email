from rest_framework.viewsets import ModelViewSet
from .controller import EmailController


email_controller = EmailController()

class EmailAPIView(ModelViewSet):
    def send(self, request):
        return email_controller.send(request)