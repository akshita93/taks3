from rest_framework.generics import ListCreateAPIView
from .serializers import registerUser

# Create your views here.

class UserRegisterAPI(ListCreateAPIView):
    serializer_class = registerUser