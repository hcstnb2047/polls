from django.urls import path

from . import views
# ビューを呼ぶために URL を対応付け。URLパターンをインクルードするときはいつでも include() を使うべき
urlpatterns=[
    path('', views.index, name='index'),
]