from django.urls import path
from .views import NewsItemList, NewsItemDetail, NewsItemCreateView, NewsItemEditView

urlpatterns = [
    path('news_list/', NewsItemList.as_view(), name='news-list'),
    path('news_list/<int:news_id>', NewsItemDetail.as_view(), name='news-detail'),
    path('news_list/create/', NewsItemCreateView.as_view(), name='news-create'),
    path('news_list/<int:news_id>/edit', NewsItemEditView.as_view(), name='news-edit'),
]
