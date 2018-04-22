from django.conf.urls import url
from brackets.views import home

#####
# URLs: Parametros vazios ou com valor, ambas enviam para a view home
#####

urlpatterns = [
    url(r'^$', home),
    url(r'^(?P<get>.*)/$', home),
    ]