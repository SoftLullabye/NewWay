from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import Articles
from .forms import ArticlesForm


from django.shortcuts import get_object_or_404, redirect, render


def news(request):
    new = Articles.objects.order_by('-date')
    return render(request, 'news/news.html', {'new': new})


def newsfeed(request):
    new = Articles.objects.order_by('-date')
    return render(request, 'news/newsfeed.html', {'new': new})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Неверная форма'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)


def detail(request):
    return render(request, 'news/create.html')


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'

def post_detail(request):
    return render(request, 'news/create.html')



