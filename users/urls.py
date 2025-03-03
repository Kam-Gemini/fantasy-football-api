from django.urls import path
from .views import RegisteredView, LoginView, UserProfileView

urlpatterns = [
    path('register/', RegisteredView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('login/', LoginView.as_view())
]