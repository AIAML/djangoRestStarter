from django.urls import include, path

from .views import RegisterView,UserProfileView

urlpatterns = [path("register/", RegisterView.as_view(),name='user-register'),
               path('profile/', UserProfileView.as_view(),name='user-profile'),
               ]