from django.urls import path
from hello import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("log/", views.log_message, name="log"),
    path("messages/", views.MessageListView.as_view(), name='messages')
]
