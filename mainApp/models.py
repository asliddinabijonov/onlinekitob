from django.db import models


class Bolim(models.Model):
    nomi = models.CharField(max_length=255, null=True, blank=True)
    haqida = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nomi


class Muallif(models.Model):
    ism = models.CharField(max_length=255)
    tirik = models.BooleanField(default=False)
    mamlakat = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.ism



class Kitob(models.Model):
    nomi = models.CharField(max_length=255)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    yili = models.DateField(null=True, blank=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
