from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Card(models.Model):
    FACTIONS = [('G', 'Government'), ('C', 'Corporate'), ('S', 'Street'), ('N', 'None')]

    name = models.CharField(max_length=50)
    faction = models.CharField(
        choices=FACTIONS,
        max_length=50)
    cost = models.IntegerField(default=0, blank=True, null=True)
    abilities = models.CharField(max_length=150)
    flavor = models.TextField(max_length=500, blank=True, null=True)
    date_submitted = models.DateTimeField(auto_now_add=True, blank=True)
    approved = models.BooleanField(default=False, blank=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def faction_verbose(self):
        return dict(Card.FACTIONS)[self.faction]

    def __str__(self):
        return self.name


class Sponsor(Card):
    production = models.IntegerField(default=0)
    victory = models.CharField(max_length=150)


class Location(Card):
    manual_security = models.IntegerField(default=0)
    electronic_security = models.IntegerField(default=0)
    production = models.IntegerField(default=0)
    ops_points = models.IntegerField(default=0)
    attributes = models.CharField(max_length=150)


class Image(models.Model):
    image = models.ImageField(upload_to='./cards')
    approved = models.BooleanField(default=True, blank=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return self.card.name


class Deck(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    cards = models.ManyToManyField(Card, limit_choices_to={'approved': True}, blank=True)
    date_submitted = models.DateTimeField(auto_now_add=True, blank=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} by {self.submitted_by}'
