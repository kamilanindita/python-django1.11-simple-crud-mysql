from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = [
    url(r'^buku/',include('buku.urls',namespace='buku')),
    url(r'^$', RedirectView.as_view(url='buku', permanent=False)),
    url(r'^admin/', admin.site.urls),
]
