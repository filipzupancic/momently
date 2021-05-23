

from django.urls import path
from app import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #path('admin/', admin.site.urls),

    #path('', views.sample_function, name="index"),
    path('events', views.events, name="events"),
    path('test-events', views.test_events, name="events"),
    path('ping', views.ping, name="ping"),
    path('graph-points', views.graph_points, name="graph_points")

]