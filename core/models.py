from django.db import models

class Atirgul(models.Model):
    turi = models.CharField(max_length=31)
    rangi= models.CharField(max_length=31)
    vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.turi


class Moshina(models.Model):
    turi = models.CharField(max_length=31)
    rangi = models.CharField(max_length=31)
    vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rangi



class Odam(models.Model):
    ism = models.CharField(max_length=31)
    yosh = models.IntegerField(default=18)
    vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ism



class Uy(models.Model):
    manzil = models.CharField(max_length=31)
    maydon = models.IntegerField(default=2)
    vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.manzil



class Telefon(models.Model):
    malumot = models.TextField(max_length=31)
    narx = models.IntegerField(default=100)
    vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.malumot



class Meva(models.Model):
    tur = models.CharField(max_length=31)
    narx = models.IntegerField(default=31)
    vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tur



class Davlat(models.Model):
    nom = models.CharField(max_length=31)
    maydon = models.IntegerField(default=2)
    vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom



class Qoshiq(models.Model):
    til = models.CharField(max_length=31)
    mazmun = models.TextField()
    vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.til



class Yegulik(models.Model):
    nomii = models.CharField(max_length=31)
    narxii=models.IntegerField(default=10)
    vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nomii



class Rasm(models.Model):
    turii = models.CharField(max_length=31)
    soni = models.IntegerField(default=2)
    vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.turii



class Moshinaa(models.Model):
    turr = models.CharField(max_length=31)
    rangg = models.CharField(max_length=31)
    yil = models.IntegerField(default=2004)
    narx = models.IntegerField(default=70)
    rasm = models.CharField(max_length=256)

    def __str__(self):
        return self.turr