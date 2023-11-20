from django import forms
from .models import CD, GENRE_CHOICES


class ExchangeForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    title = forms.CharField(max_length=100)
    artist = forms.CharField(max_length=40)
    genre = forms.ChoiceField(choices=GENRE_CHOICES)
    price = forms.DecimalField(required=False)
    comment = forms.CharField(widget=forms.Textarea, required=False)

    def clean_artist(self):
        artist = self.cleaned_data['artist']
        valid_artist = CD.objects.filter(artist__contains=artist).count()
        if valid_artist == 0:
            raise forms.ValidationError('Такого Артиста нету')
        return artist
