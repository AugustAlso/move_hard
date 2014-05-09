from django.conf.urls import patterns, url
from moves import views

urlpatterns = patterns('',
    url(r'^$', views.MoveView.as_view(), name="index"),
)