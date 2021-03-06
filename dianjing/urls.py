from django.conf.urls import include, url
from django.contrib import admin

import apps.config.views
import apps.gift_code.views

import views.admin
import views.purchase
import views.statistics

urlpatterns = [
    # Examples:
    # url(r'^$', 'dianjing.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^game/', include('views.urls')),
    url(r'^api/', include('views_api.urls')),

    url(r'^system/config/$', apps.config.views.get_config),
    url(r'^system/bulletin/$', apps.config.views.get_bulletins),

    url(r'^flushcache/$', views.admin.flushcache),
    url(r'^relogin/$', views.admin.relogin),
    url(r'^callback/1sdk/$', views.purchase.callback_1sdk),
    url(r'^callback/stars_cloud/$', views.purchase.callback_stars_cloud),

    url(r'^statistics/$', views.statistics.index),
    url(r'^statistics/purchase/$', views.statistics.purchase_info),
    url(r'^statistics/purchase/download/$', views.statistics.purchase_info_download),
    url(r'^statistics/retained/$', views.statistics.retained_info),
    url(r'^statistics/retained/download/$', views.statistics.retained_info_download),
    url(r'^statistics/char/$', views.statistics.char_info),
    url(r'^statistics/union/$', views.statistics.union_info),
    url(r'^statistics/arena/$', views.statistics.arena_info),
    url(r'^statistics/gold/$', views.statistics.gold_info),
    url(r'^statistics/gold/download/$', views.statistics.gold_info_download),
    url(r'^statistics/diamond/$', views.statistics.diamond_info),
    url(r'^statistics/diamond/download/$', views.statistics.diamond_info_download),

    url(r'^gift_code/download/$', apps.gift_code.views.download_gift_code),
]
