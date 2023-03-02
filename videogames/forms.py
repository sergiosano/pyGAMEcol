from django import forms
from .models import Videogame, Platform, Format


class VideogameCreateForm(forms.Form):
    title = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'title'}))
    platform = forms.ModelChoiceField(queryset=Platform.objects.all().order_by('name'), widget=forms.Select(attrs={'class': 'form-control form-control-lg', 'id': 'platform'}))
    formato = forms.ModelChoiceField(queryset=Format.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-lg', 'id': 'formato'}))
    release_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control form-control-lg text-center', 'id': 'release_date', 'type': 'date'})) 
    front_cover = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control form-control-lg', 'id': 'front_cover'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control form-control-lg', 'id': 'formato', 'rows': 4}))

class VideogameUpdateForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'title'}))
    platform = forms.ModelChoiceField(queryset=Platform.objects.all().order_by('name'), widget=forms.Select(attrs={'class': 'form-control form-control-lg', 'id': 'platform'}))
    formato = forms.ModelChoiceField(queryset=Format.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-lg', 'id': 'formato'}))
    release_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control form-control-lg text-center', 'id': 'release_date', 'type': 'date'}, format='%Y-%m-%d'))
    front_cover = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control form-control-lg', 'id': 'front_cover'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control form-control-lg', 'id': 'formato', 'rows': 4}))

    class Meta:
        model = Videogame
        fields = ['title', 'platform', 'formato', 'release_date', 'front_cover', 'description']