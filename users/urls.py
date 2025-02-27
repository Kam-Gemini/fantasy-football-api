from django.urls import path
from .views import RegisteredView, LoginView

urlpatterns = [
    path('register/', RegisteredView.as_view()),
    path('login/', LoginView.as_view())
]