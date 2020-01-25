from __future__ import unicode_literals

from django.db import models

class Buku(models.Model):
    id          = models.AutoField(primary_key=True)
    penulis     = models.CharField(max_length=100)
    judul       = models.CharField(max_length=100)
    kota        = models.CharField(max_length=100)
    penerbit    = models.CharField(max_length=100)
    tahun       = models.IntegerField()
    
    def __str__(self):
        return "{}.{}".format(self.id,self.penulis)
    