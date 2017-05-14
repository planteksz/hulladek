from django.conf.urls import url
from . import views



urlpatterns = [
    # /users/signup:url to take the input from the user
    url(r'^signup/$', views.signup, name='signup'),
    #/users/showdata:url to display the list of users stored on the database
    url(r'^showdata/$', views.showdata, name='showdata'),
]