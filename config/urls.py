
from django.contrib import admin
from django.urls import path, include

from config.schema import swagger_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('knn-diabetes/', include('apps.knn.urls'))
]
urlpatterns += swagger_urlpatterns
