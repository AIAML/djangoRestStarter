from django.urls import include, path

from .views import RegisterView,UserProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [path("register/", RegisterView.as_view(),name='user-register'),
               path('profile/', UserProfileView.as_view(),name='user-profile'),
               path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
               path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
               ]