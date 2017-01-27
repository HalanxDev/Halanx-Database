from django.conf.urls import url
from ShopperBase import views


urlpatterns = [
    url(r'^$', views.shopper_list),
    url(r'^(?P<pk>[0-9]+)', views.shopper_id),
    url(r'^$', views.slot_list),
]



