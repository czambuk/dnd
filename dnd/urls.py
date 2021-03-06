"""dnd URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# From Apps
from char_app.views import ViewCharacterSheet, NewCharacterSheet, AllHeroesListView, HeroDetailView
from landing_page.views import HomePage, LoginPageView, LogoutPageView, UserCreateView, ContactPage
from dice_roller.views import DiceRollView
from campaigns_diary.views import (CampaignCreateView,
                                   CampaignViewAllView,
                                   CampaignDetailView,
                                   CampaignEntryCreateView,
                                   CampaignDeleteView,
                                   CampaignUpdateView,
                                   )
from quests.views import (AllQuestsView,
                          QuestCreateView,
                          )

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # My urls
                  # main site
                  path('', HomePage.as_view()),
                  # landing_page main views
                  path('new_character', NewCharacterSheet.as_view()),
                  path('view_campaigns', CampaignViewAllView.as_view()),
                  path('view_characters', AllHeroesListView.as_view()),
                  path('roll_dice', DiceRollView.as_view()),
                  path('contact', ContactPage.as_view()),
                  # login/logout/register
                  path('login', LoginPageView.as_view()),
                  path('logout', LogoutPageView.as_view()),
                  path('register', UserCreateView.as_view()),
                  # char_app
                  path('view_character/<int:id>', HeroDetailView.as_view()),
                  # campaigns_diary
                  path('add_campaign', CampaignCreateView.as_view()),
                  path('view_campaigns/<int:camp_id>', CampaignDetailView.as_view()),
                  path('add_entry/<int:id>', CampaignEntryCreateView.as_view()),
                  path('delete_campaign/<int:campaign_id>', CampaignDeleteView.as_view()),
                  path('update_campaign/<int:campaign_id>', CampaignUpdateView.as_view()),
                  path('view_quests', AllQuestsView.as_view()),
                  path('create_quests', QuestCreateView.as_view()),

              ] + static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
