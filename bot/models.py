from django.db import models


class Valk(models.Model):
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=10)
    image = models.CharField(max_length=255,default=None,null=True)
    color_hex = models.IntegerField(max_length=8,default=0xEB459F)
    def __str__(self):
        return self.name

class SignetCategory(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    

class Signet(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(SignetCategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Build(models.Model):
    name = models.CharField(max_length=200)
    valk = models.ForeignKey(Valk, on_delete=models.CASCADE)
    signets = models.ManyToManyField(Signet)
    def __str__(self):
        return self.name
    
    