from django.conf.urls import url
from django.urls import path

from .views import ProfileRetrieveAPIView

app_name = 'profiles'
urlpatterns = [
    url(r'^profiles/<str:email>', ProfileRetrieveAPIView.as_view()),
]