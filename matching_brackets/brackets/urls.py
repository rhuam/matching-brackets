from django.conf.urls import url
from brackets.views import home

urlpatterns = [
    url(r'^$', home),
    url(r'^(?P<get>.*)/$', home),
    ]