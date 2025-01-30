from . import views

from django.urls import path

urlpatterns = [
    path('', views.index, name='emailer-index'),
    path('send-bcc-email/', views.send_bcc_email, name='send-bcc-email'),
]
