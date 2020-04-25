from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView

from ccg_archive.cyberpunk_ccg_archive.forms import SponsorCardForm
from ccg_archive.cyberpunk_ccg_archive.models import Sponsor, Image


class IndexView(TemplateView):
    """
    Template view of the homepage
    """

    template_name = "index.html"


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
        return HttpResponseRedirect(reverse_lazy('admin'))
