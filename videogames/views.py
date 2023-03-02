from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from .models import Videogame
from .forms import VideogameCreateForm, VideogameUpdateForm


class VideogameListView(ListView):
    template_name = 'collection/collection.html'

    def get_queryset(self):
        return Videogame.objects.filter(owner_id=self.request.user.id).order_by('title')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index')

        return super().dispatch(request, *args, **kwargs)

class VideogameDetailView(DetailView):
    model = Videogame
    template_name = 'videogames/videogame_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user != Videogame.objects.get(slug=kwargs['slug']).owner:
            return redirect('index')

        return super().dispatch(request, *args, **kwargs)

def videogame_create(request):
    if not request.user.is_authenticated:
        return redirect('index')

    form = VideogameCreateForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        title = form.cleaned_data.get('title')
        platform = form.cleaned_data.get('platform')
        formato = form.cleaned_data.get('formato')
        release_date = form.cleaned_data.get('release_date')
        front_cover = form.cleaned_data.get('front_cover')
        if not front_cover:
            front_cover = 'videogames/front_covers/default_front_cover.png'
        description = form.cleaned_data.get('description')
        videogame = Videogame.objects.create(owner=request.user, title=title, platform=platform, formato=formato, release_date=release_date, front_cover=front_cover, description=description)

        if videogame:
            return redirect('collection')

    return render(request, 'videogames/videogame_create.html', {'form': form})

def videogame_update(request, slug):
    if not request.user.is_authenticated or request.user != Videogame.objects.get(slug=slug).owner:
        return redirect('index')
    
    videogame = Videogame.objects.get(slug=slug)

    if request.method == 'POST':
        form = VideogameUpdateForm(request.POST or None, request.FILES or None, instance=videogame)
        if form.is_valid():
            form.save()
            return redirect('videogame_view', videogame.slug)
    else:
        form = VideogameUpdateForm(instance=videogame)

    return render(request, 'videogames/videogame_update.html', {'form': form, 'videogame': videogame})

class VideogameDeleteView(DeleteView):
    model = Videogame
    success_url = reverse_lazy("collection")
    template_name = "videogames/videogame_delete.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or request.user != Videogame.objects.get(slug=kwargs['slug']).owner:
            return redirect('index')

        return super().dispatch(request, *args, **kwargs)