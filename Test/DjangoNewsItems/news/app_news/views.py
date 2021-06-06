from pprint import pprint

from django.shortcuts import render,reverse
from django.utils import timezone
from django.views import View, generic
from django.http import HttpResponseRedirect
from .models import NewsItem, Comment
from .forms import NewsItemCreateForm, NewsCommentCreateForm


class NewsItemList(generic.ListView):
    model = NewsItem
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    queryset = NewsItem.objects.all()


class NewsItemDetail(View):

    @staticmethod
    def check_login(check_list):
        for comment in check_list:
            if comment.user is None:
                comment.name_author = f'{comment.name_author}(аноним)'
            else:
                comment.name_author = comment.user
        return check_list

    def get(self, request, news_id):
        news_item = NewsItem.objects.get(id=news_id)
        comment_list = Comment.objects.filter(news_id=news_id)[::-1]
        comment_form = NewsCommentCreateForm()

        comment_list = self.check_login(check_list=comment_list)

        return render(request, 'news/detail.html', {'news_item': news_item,
                                                    'comment_list': comment_list,
                                                    'comment_form': comment_form,
                                                    'news_id': news_id})

    def post(self, request, news_id):
        new_comment = NewsCommentCreateForm(request.POST)
        if new_comment.is_valid():
            Comment.objects.create(**new_comment.cleaned_data, news_id=news_id)

        elif request.user.is_authenticated:
            new_comment.cleaned_data['name_author'] = request.user.username
            Comment.objects.create(**new_comment.cleaned_data, news_id=news_id, user_id=request.user.id)

        return HttpResponseRedirect(f'/news_list/{news_id}')


class NewsItemCreateView(View):

    def get(self, request):
        item_form = NewsItemCreateForm()
        return render(request, 'news/create.html', {'item_form': item_form})

    def post(self, request):
        item_form = NewsItemCreateForm(request.POST)
        if item_form.is_valid():
            NewsItem.objects.create(**item_form.cleaned_data)
            return HttpResponseRedirect(reverse('news-list'))
        return render(request, 'news/create.html', {'item_form': item_form})


class NewsItemEditView(View):

    def get(self, request, news_id):
        news_item = NewsItem.objects.get(id=news_id)
        news_item_form = NewsItemCreateForm(instance=news_item)
        return render(request, 'news/edit.html', context={'news_item': news_item,
                                                          'news_item_form': news_item_form,
                                                          'news_id': news_id})

    def post(self, request, news_id):
        news_item = NewsItem.objects.get(id=news_id)
        news_item_form = NewsItemCreateForm(request.POST, instance=news_item)
        if news_item_form.is_valid():
            news_item.edit_date = timezone.now()
            news_item.save()
        return HttpResponseRedirect(reverse('news-list'))
