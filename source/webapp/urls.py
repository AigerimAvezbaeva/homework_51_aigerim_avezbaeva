from django.urls import path

from webapp.views.cat_stats import cat_stats
from webapp.views.base import index_view

urlpatterns = [
    path('', index_view),
    path('cat_stats', cat_stats)
]
