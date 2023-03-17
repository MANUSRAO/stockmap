from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('heatmap/',views.heatmap,name="Nifty"),
    path('sensexHeatmap/',views.sensexHeatmap,name="Sensex")
]