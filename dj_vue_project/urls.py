"""urls for dj_vue_project Django project"""

from django.contrib import admin
from django.urls import path, re_path, include # add include import
from index_view.views import IndexView

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/', include('backend.urls')), # Include the backend URLs before the catch-all route
   re_path(r'^.*', IndexView.as_view()), # Catch-all route for the frontend
]
