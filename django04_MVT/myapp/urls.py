from django.urls import path
from myapp import views

urlpatterns = [
    path('index/',views.index),
    path('<request1_id>/<request2_id>',views.userRequest)
]