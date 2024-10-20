from django.urls import path, include
from Spese.views import home, lista_destinazione, lista_tipologia, lista_movimenti, dettaglio_movimento, add_destinazione, add_movimento, add_tipologia
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('lista_destinazione/', lista_destinazione, name='lista_destinazione'),
    path('lista_tipologia/', lista_tipologia, name='lista_tipologia'),
    path('litsa_movimenti/', lista_movimenti, name='lista_movimenti'),
    path('add_destinazione/', add_destinazione, name='add_destinazione'),
    path('add_movimento/', add_movimento, name='add_movimento'),
    path('add_tipologia/', add_tipologia, name='add_tipologia'),
    path('movimento/<int:movimento_id>/', views.dettaglio_movimento, name='dettaglio_movimento'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)