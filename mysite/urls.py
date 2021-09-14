
from django.contrib import admin
from django.urls import include, path
# urlpatterns のリストに include() を挿入
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
