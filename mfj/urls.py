from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('intro.urls')),
    path('',include('explore.urls')),
    path('authentication/',include('authentication.urls')),
    path('',include('payment.urls')),
    path('',include('review.urls')),
    path('',include('filter.urls')),
    path('',include('contactus.urls')),
    path('',include('admins.urls')),
    path('',include('appointments.urls')),
    path('',include('appointments.urls')),
    path('',include('bill.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)