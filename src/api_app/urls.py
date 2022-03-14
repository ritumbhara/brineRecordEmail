from django.urls import path
from .views import EmailItemViews

urlpatterns = [
    path('email/', EmailItemViews.as_view())
]