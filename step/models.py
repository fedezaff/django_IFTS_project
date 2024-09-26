from django.db import models

class Aziende(models.Model):    
    id_azienda = models.AutoField(primary_key=True)
    azienda = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    def __str__(self):        
        return self.azienda
    
class Competenze(models.Model):
    id_competenza = models.AutoField(primary_key=True)    
    competenza = models.CharField(max_length=50)
    link = models.CharField(max_length=1000)
    def __str__(self):        
        return self.competenza
    
class Offerte(models.Model):
    id_offerta = models.AutoField(primary_key=True)    
    id_azienda = models.IntegerField()
    titolo = models.CharField(max_length=50)    
    descrizione = models.TextField()
    def __str__(self):        
        return self.titolo
    
class Offerte_competenze(models.Model):
    id_offerta = models.ForeignKey(Offerte, on_delete=models.CASCADE)  
    id_competenza = models.ForeignKey(Competenze, on_delete=models.CASCADE)