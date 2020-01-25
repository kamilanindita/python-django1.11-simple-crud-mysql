from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
	url(r'^update/(?P<update_id>[0-9]+)$', views.update, name='update'),
    url(r'^add/$',views.add, name='add'),
	url(r'^$',views.buku, name='buku'),
]