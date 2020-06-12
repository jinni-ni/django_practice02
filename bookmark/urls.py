from django.urls import path
from bookmark.views import BookmarkDV, BookmarkLV

app_name='bookmark'

urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('',BookmarkDV.as_view(), name='detail'),
]
