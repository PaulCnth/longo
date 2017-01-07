from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from models import Article, HashTag
from forms import ArticleForm, SearchForm
from api import Spider

# Create your views here.


class Index(View):
    def get(self, request):
        articles = Article.objects.order_by("-pub_date")
        return render(request, 'profile.html', {'articles': articles})

    def post(self, request):
        return HttpResponse('Hi, <b>kalimodo</b>, welcome you here!!!')


class AddArticle(View):
    """
    Tweet Post form available on page /add/ URL
    """

    def post(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():

            # get web abstract
            spid = Spider()
            data = spid.get_content(form.cleaned_data['url'])

            # save into  article
            art = Article(url=form.cleaned_data['url'], title=data['title'], context=data['tips'])
            art.save()

            # save into hashtag
            words = form.cleaned_data['tag'].split(",")
            for word in words:
                # at least one keyword
                if len(word) >= 1:
                    hashtag, created = HashTag.objects.get_or_create(name=word[1:])
                    hashtag.article.add(art)
            return HttpResponseRedirect('/index/')


class HashTagCloud(View):
    """
    Hash Tag page reachable from /hashtag/<hashtag> URL
    """

    def get(self, request, hashtag):
        params = dict()
        hashtag = HashTag.objects.get(name=hashtag)
        params["tweets"] = hashtag.tweet
        return render(request, 'hashtag.html', params)
