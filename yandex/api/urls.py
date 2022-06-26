from django.urls import path
from . import views

urlpatterns = [
    path('imports', views.ApiView.as_view()),
    path('delete/<str:uid>', views.ApiView.as_view()),
    path('nodes/<str:uid>', views.ApiView.as_view()),
    path('sales', views.OptionalApiView.as_view())
]