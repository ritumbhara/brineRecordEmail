from django.urls import path
from .views import EmailItemViews

urlpatterns = [
    path('email-items/', EmailItemViews.as_view())
]