from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.order_list),
    url(r'^(?P<pk>[0-9]+)', views.order_id),
]



