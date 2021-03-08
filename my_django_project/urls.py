from django.contrib import admin
from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('fbv_demo/', include('fbv_demo.urls')),
    path('cbv_demo/', include('cbv_demo.urls')),
    path('misc/', include('misc.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns