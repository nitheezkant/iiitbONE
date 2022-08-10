from django.contrib import admin
from django.urls import URLPattern, path,include
from django.views import View
from . import views

urlpatterns=[
    path('',views.landing,name="landing"),
    path('upload/',views.upload,name="upload"),
    path('clist/',views.clist,name="clist"),
    path('tlist/<str:pk>/', views.tlist, name="tlist"),
    path('lisst/<str:pk>/<str:pkk>', views.lisst, name="lisst"),
    path('info/<str:pk>/', views.info, name="info"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.loginn,name="login"),
    path('semc/<str:pk>/',views.semc,name="semc"),
    path('logout/', views.logoutuser, name='logout'),
]