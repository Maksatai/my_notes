from django.urls import path
from signup.views import SignupView

urlpatterns = [
    path('signup/', SignupView.as_view(), name="signup"),
]