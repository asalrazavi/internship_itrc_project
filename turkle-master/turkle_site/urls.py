from django.contrib import admin
from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns

from turkle.utils import get_site_name

admin.autodiscover()
admin.site.site_header = 'Administration'
admin.site.site_title = get_site_name()

urlpatterns = i18n_patterns(
    # backward compatibility - remove with Turkle 3.0 release
    path('turkle/', include('turkle.urls')),

    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('turkle.urls')),
)
