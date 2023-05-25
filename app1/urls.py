from django.urls import path


from app1.views import *

app_name='nothing'

urlpatterns=[
        path('virat/',virat, name='virat'),
        path('maxwell/', maxwell,name='maxwell'),

]