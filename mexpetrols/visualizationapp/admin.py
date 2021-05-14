from django.contrib import admin
from .models import Activecode, Actives, Gasolineprices, Gasolinetype, Methanepetrochemicals, Producttypes, Region, Types
# Register your models here.
@admin.register(Activecode)
class ActiveCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
    list_filter = ['name']

@admin.register(Actives)
class ActivesAdmin(admin.ModelAdmin):
    list_display = ('id', 'regionid', 'activecodeid', 'price', 'creationdate')
    search_fields = ('activecodeid', 'creationdate')
    list_filter = ['regionid', 'activecodeid']

@admin.register(Gasolineprices)
class GasolinepricesAdmin(admin.ModelAdmin):
    list_display =  ('id', 'gasolinetypeid', 'price', 'creationdate')
    search_fields = ('gasolinetypeid', 'price')
    list_filter = ('id', 'gasolinetypeid', 'price')

@admin.register(Gasolinetype)
class GasolinetypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
    list_filter = ['name']

@admin.register(Methanepetrochemicals)
class MethanepetrochemicalsAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'typeid', 'producttypeid', 'creationdate')
    search_fields = ('id', 'price', 'typeid', 'producttypeid', 'creationdate')
    list_filter = ('price', 'typeid', 'producttypeid', 'creationdate')

@admin.register(Producttypes)
class ProducttypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
    list_filter = ['name']

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
    list_filter = ['name']

@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['name']
    list_filter = ['name']