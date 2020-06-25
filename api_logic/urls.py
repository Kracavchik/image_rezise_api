from django.urls import path
from .views import ImageView

app_name = 'api_logic'

urlpatterns = [
    path('image/<int:pk>/', ImageView.as_view()),
    path('image/<int:pk>_<int:height>_<int:width>/', ImageView.as_view()),
]
