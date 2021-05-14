from django.db import models

# Create your models here.
class Activecode(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ActiveCode'


class Actives(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    regionid = models.IntegerField(db_column='RegionId', blank=True, null=True)  # Field name made lowercase.
    activecodeid = models.IntegerField(db_column='ActiveCodeId', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        verbose_name = 'Actives'
        managed = False
        db_table = 'Actives'


class Gasolineprices(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    gasolinetypeid = models.IntegerField(db_column='GasolineTypeId', blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GasolinePrices'


class Gasolinetype(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GasolineType'


class Methanepetrochemicals(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    price = models.BigIntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    typeid = models.IntegerField(db_column='TypeId', blank=True, null=True)  # Field name made lowercase.
    producttypeid = models.IntegerField(db_column='ProductTypeId', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MethanePetrochemicals'


class Producttypes(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductTypes'


class Region(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Region'


class Types(models.Model):
    id = models.BigAutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Types'
