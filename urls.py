from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="name1"),
    path('<int:price>', views.calculate_total, name="name2"),
    path('taxRate', views.index4, name="name3"),
    #path('<str:name>', views.greet, name="name5"),
    #path('<str:name>', views.flexable, name="Azzam"),
    # Add more URL patterns here
]