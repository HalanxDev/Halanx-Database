from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.itemslist_list),
    url(r'^(?P<pk>[0-9]+)', views.itemslist_id),

]





