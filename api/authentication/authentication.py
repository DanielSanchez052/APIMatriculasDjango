from rest_framework_simplejwt.views import TokenObtainPairView, TokenViewBase 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from api.authentication.serializers.authenticationSerializer import ObtainTokenSerializer

#Custom Obtain Token 
class ObtainTokenView(TokenObtainPairView):
    serializer_class = ObtainTokenSerializer

#Logout 
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        if self.request.data.get('all'):
            token: OutstandingToken
            for token in OutstandingToken.objects.filter(user=request.user):
                _, _ = BlacklistedToken.objects.get_or_create(token=token)
            return Response({"message": "all refresh tokens blacklisted"},status=status.HTTP_200_OK)
        refresh_token = self.request.data.get('refresh')
        token = RefreshToken(token=refresh_token)
        token.blacklist()
        return Response({"message": "token blacklisted"},status=status.HTTP_200_OK)
