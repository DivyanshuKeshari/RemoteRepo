
from django.conf.urls import url
from django.contrib import admin
from Durgasoftapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/',views.home_view),
    url(r'^services/',views.services_view),
    url(r'^enquiry/',views.enquiry_view),
    url(r'^gallery/',views.gallery_view),
    url(r'^feedback/',views.feedback_view),
    url(r'$',views.home_view)
]
