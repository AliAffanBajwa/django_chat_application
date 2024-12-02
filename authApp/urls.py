from django.urls import path
from .views import RegisterView, LoginUserView, LogoutUserView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),   
]
