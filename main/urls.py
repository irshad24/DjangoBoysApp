from django.urls import path
from . import views
from django.views.generic.base import RedirectView
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
app_name="main"

urlpatterns=[
      path("",views.homepage,name="homepage"),
      re_path(r'^favicon\.ico$', favicon_view),
]