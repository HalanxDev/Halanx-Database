
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^batch/', include('BatchBase.urls')),
    url(r'^carts/', include('Carts.urls')),
    url(r'^itemslist/', include('ItemsList.urls')),
    url(r'^orders/', include('OrderBase.urls')),
    url(r'^products/', include('Products.urls')),
    url(r'^shoppers/', include('ShopperBase.urls')),
    url(r'^stores/', include('StoreBase.urls')),
    url(r'^users/', include('UserBase.urls')),

]


urlpatterns = format_suffix_patterns(urlpatterns)


