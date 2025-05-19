from django.urls import path
from . import views


urlpatterns = [
    path("",views.index),  #/challenges/
    path("<int:month>",views.monthly_challenges_by_number),
    path("<str:month>",views.monthly_challenges_by_text,name="monthly_challenges_by_me")
]