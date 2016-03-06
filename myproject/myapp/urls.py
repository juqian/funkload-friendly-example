from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.top_page),
    url(r'^secret_page$', views.secret_page),
    url(r'^calculate/add/$', views.AddView.as_view()),
]
