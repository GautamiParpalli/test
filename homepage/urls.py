
from django.urls import path,include
from .views import index,detail,banner
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path ('',index),
    path('<int:pk>',detail),
    path('Slider',banner)

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)