from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from api.authentication.authentication import ObtainTokenView,LogoutView

urlpatterns = [
    path('login/', ObtainTokenView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
