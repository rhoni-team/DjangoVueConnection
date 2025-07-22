"""urls for dj_vue_project Django project"""

from django.contrib import admin
from django.urls import path, re_path # add import re_path
from index_view.views import IndexView # add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^.*', IndexView.as_view()), #add this line
]
