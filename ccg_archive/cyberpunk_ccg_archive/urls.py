"""cyberpunk_ccg_archive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from ccg_archive.cyberpunk_ccg_archive import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="homepage"),
    path('sponsor/', views.SubmitSponsorView.as_view(), name='sponsor'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user'),
    path('card/submit/', views.SubmitSponsorView.as_view(), name='createcard'),
    path('cards/', views.CardListView.as_view(), name='cardlist'),
    path('card/<int:pk>', views.CardDetailView.as_view(), name='card'),
    path('card/<int:pk>/edit', views.CardUpdateView.as_view(), name='editcard'),
    path('staff/', views.CardApprovalView.as_view(), name="approve"),
    path('deck/submit/', views.SubmitDeckView.as_view(), name='createdeck'),
    path('decks/', views.DeckListView.as_view(), name='decklist'),
    path('deck/<int:pk>/', views.DeckDetailView.as_view(), name='deck')
]
