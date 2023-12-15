from django.urls import path,include
from. import views
urlpatterns = [
    path('',views.home,name='home'),
    path('forms/',views.form,name='forms'),
    path('model/',views.model,name='model'),
]
