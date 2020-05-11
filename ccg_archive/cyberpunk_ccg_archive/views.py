from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView

from ccg_archive.cyberpunk_ccg_archive.forms import SponsorCardForm, DeckForm
from ccg_archive.cyberpunk_ccg_archive.models import Sponsor, Image, Card, Deck


class IndexView(TemplateView):
    """
    Template view of the homepage
    """

    template_name = "index.html"


def handler404(request, error):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '404.html', status=500)


class UserDetailView(DetailView):
    template_name = 'userdetails.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_list'] = Card.objects.filter(submitted_by=context['user'], approved=True)
        context['deck_list'] = Deck.objects.filter(submitted_by=context['user'])
        return context


@method_decorator(login_required, name='dispatch')
class SubmitSponsorView(CreateView):
    template_name = 'generic-form.html'
    form_class = SponsorCardForm
    success_url = '/'

    def form_valid(self, form):
        data = form.cleaned_data

        card = Sponsor.objects.create(
            name=data['name'],
            faction=data['faction'],
            cost=data['cost'],
            abilities=data['abilities'],
            flavor=data['flavor'],
            submitted_by=self.request.user,
            production=data['production'],
            victory=data['victory']
        )
        card.save()
        image = Image.objects.create(
            image=data['image'],
            submitted_by=self.request.user,
            card=card
        )

        image.save()
        return HttpResponseRedirect(reverse_lazy('homepage'))


class CardListView(ListView):
    template_name = 'cardlist.html'
    model = Card
    queryset = Card.objects.filter(approved=True)
    ordering = ['name']
    paginate_by = 10


class CardDetailView(DetailView):
    template_name = 'carddetail.html'
    model = Card

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_images'] = Image.objects.filter(card=context['object'].id)
        return context


@method_decorator(staff_member_required, name='dispatch')
class CardUpdateView(UpdateView):
    template_name = 'generic-form.html'
    success_url = reverse_lazy('homepage')
    model = Card
    fields = ['name',
              'faction',
              'cost',
              'abilities',
              'flavor',
              'approved']


@method_decorator(staff_member_required, name='dispatch')
class CardApprovalView(ListView):
    template_name = 'cardapprovallist.html'
    model = Card
    queryset = Card.objects.filter(approved=False)
    ordering = ['date_submitted']
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class SubmitDeckView(CreateView):
    template_name = 'generic-form.html'
    form_class = DeckForm
    success_url = '/'

    def form_valid(self, form):
        data = form.cleaned_data

        deck = Deck.objects.create(
            name=data['name'],
            description=data['description'],
            submitted_by=self.request.user
        )
        for card in data['cards']:
            deck.cards.add(card)
        deck.save()
        return HttpResponseRedirect(reverse_lazy('homepage'))


class DeckListView(ListView):
    template_name = 'decklist.html'
    model = Deck
    queryset = Deck.objects.all()
    ordering = ['name']
    paginate_by = 25


class DeckDetailView(DetailView):
    template_name = 'deckdetail.html'
    model = Deck

