

from django.urls import path
from app import views


urlpatterns = [
    #path('admin/', admin.site.urls),

    #path('', views.sample_function, name="index"),
    path('events', views.events, name="events"),
    path('test-events', views.test_events, name="events"),

]
