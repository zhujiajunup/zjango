from .views import sso_complete
from django.conf.urls import url

app_name = 'sso'
urlpatterns = [
    url(r'^complete/$', sso_complete, name='sso_complete')
]
