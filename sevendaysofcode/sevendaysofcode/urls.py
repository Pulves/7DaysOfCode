import thirdday
from django.contrib import admin
from django.urls import path, include

import thirdday.third_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(thirdday.third_urls)),
]
