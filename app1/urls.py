from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path('zwn/',views.zwn,name="zwn"),
    path('lyj/', views.lyj, name="lyj"),
    path('xcp/', views.xcp, name="xcp"),
    path('zyl/',views.zyl,name="zyl"),
]