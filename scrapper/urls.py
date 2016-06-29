
from django.conf.urls import include, url
from django.contrib import admin
from data import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.ScrappList.as_view(), name='home' ),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.ScrappDetail.as_view(), name='detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
