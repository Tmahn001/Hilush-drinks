from django.urls import path, include
from rest_framework import routers
from api.views import CategoryView, ItemView
from . import views
from django.conf import settings
from django.conf.urls.static import static

'''router = routers.DefaultRouter()
router.register(r'category', CategoryView)
router.register(r'item', ItemView)
router.register(r'', views.homeView)'''

urlpatterns = [
    path('', views.homeView, name="home"),
    path('test', views.home_test),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('update-item', views.updateItem),
    path('process-order', views.processOrder, name='process-order'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
