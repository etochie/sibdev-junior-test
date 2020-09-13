from django.contrib import admin
from django.urls import path

from apps.core.views import DealView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('deal/', DealView.as_view())
]
