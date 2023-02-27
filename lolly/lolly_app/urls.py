from django.urls import path
from lolly_app import views

urlpatterns = [
    path('',views.index, name='home'),
    path('check_duplicate',views.checkDuplication, name="duplication"),
    path('commas',views.commas, name="commas"),
    path('upload',views.upload,name="upload")
]