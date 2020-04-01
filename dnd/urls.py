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
from char_app.views import ViewCharacterSheet, NewCharacterSheet
from landing_page.views import HomePage
from dice_roller.views import DiceRollView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # My urls

    # char_app specifically
    path('view_character/<int:id>', ViewCharacterSheet.as_view()),

    # landing_page links
    path('', HomePage.as_view()),  # main site
    path('new_character', NewCharacterSheet.as_view()),
    # TODO path('view_campaigns', .as_view()),
    # TODO path('view_characters', .as_view()),
    # dice_roller
    path('roll_dice', DiceRollView.as_view()),
] + static(settings.STATIC_URL,
           document_root=settings.STATIC_ROOT)


