from django import forms
from ccg_archive.cyberpunk_ccg_archive import models


class SponsorCardForm(forms.ModelForm):
    class Meta:
        model = models.Sponsor
        fields = [
            'name',
            'faction',
            'cost',
            'abilities',
            'flavor',
            'production',
            'victory'
        ]
    image = forms.ImageField()


class LocationCardForm(forms.ModelForm):
    class Meta:
        model = models.Location
        fields = [
            'name',
            'faction',
            'cost',
            'abilities',
            'flavor',
            'manual_security',
            'electronic_security',
            'production',
            'ops_points',
            'attributes'
        ]
