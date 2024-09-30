from django.db import models

class Aziende(models.Model):    
    id_azienda = models.AutoField(primary_key=True)
    azienda = models.CharField(max_length=100)
    descrizione = models.TextField()
    password = models.CharField(max_length=50)
    mail = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    url_logo = models.CharField(max_length=100)
    url_img_1 = models.CharField(max_length=100)
    url_img_2 = models.CharField(max_length=100)
    url_img_3 = models.CharField(max_length=100)
    def __str__(self):        
        return self.azienda
    
class Competenze(models.Model):
    id_competenza = models.AutoField(primary_key=True)    
    competenza = models.CharField(max_length=50)
    link = models.CharField(max_length=100)
    def __str__(self):        
        return self.competenza
    
class Offerte(models.Model):
    id_offerta = models.AutoField(primary_key=True)    
    id_azienda = models.IntegerField()
    titolo = models.CharField(max_length=50)  
    descrizione_breve = models.TextField()
    descrizione = models.TextField()
    luogo = models.CharField(max_length=100)  
    def __str__(self):        
        return self.titolo
    
class Offerte_competenze(models.Model):
    id_offerta = models.ForeignKey(Offerte, on_delete=models.CASCADE)  
    id_competenza = models.ForeignKey(Competenze, on_delete=models.CASCADE)