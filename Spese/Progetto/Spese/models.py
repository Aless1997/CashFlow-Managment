from django.db import models

class Tipologia(models.Model):
    n_tipologia = models.CharField(max_length=15, null=False)
    data_creazione = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Tipologia'
        verbose_name_plural = 'Tipologie'
    
    def __str__(self):
        return f"{self.n_tipologia}"

class Destinazione(models.Model):
    nome = models.CharField(max_length=25, null=False)
    data_creazione = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Destinazione'
        verbose_name_plural = 'Destinazioni'
    
    def __str__(self):
        return f"{self.nome}"

class Movimento(models.Model):
    tipologia = models.ForeignKey(Tipologia, on_delete=models.CASCADE, related_name='MTipologia')
    valore = models.DecimalField(max_digits=12, decimal_places=2)
    destinazione = models.ForeignKey(Destinazione, on_delete=models.CASCADE, related_name='MDestinazione')
    data_movimento = models.DateField(auto_now=True)
    descrizione = models.TextField(max_length=150, null=False)
    file = models.FileField(upload_to='documenti/', blank=True)

    class Meta:
        verbose_name = 'Movimento'
        verbose_name_plural = 'Movimenti'

    def __str__(self):
        return f"{self.tipologia} {self.valore} €"