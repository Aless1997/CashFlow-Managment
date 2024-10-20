from django.forms import ModelForm
from Spese.models import Tipologia, Movimento, Destinazione

class AddTipologia(ModelForm):
    class Meta():
        model = Tipologia
        fields = '__all__'    

class AddMovimento(ModelForm):
    class Meta():
        model = Movimento
        fields = '__all__'

class AddDestinazione(ModelForm):
    class Meta():
        model = Destinazione
        fields = '__all__'