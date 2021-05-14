from datetime import date
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import pandas
import numpy as np 
from sqlalchemy import create_engine, Table, Column, String, Integer, Float, ForeignKey, Date, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey

"""
PWD='123123123'
USR='test_user';
SQLALCHEMY_DATABASE_URI = 'mysql://{}:{}@localhost:3306/test_db'.format(USR, PWD)
"""
db_string = 'mysql+pymysql://root:samplepassword@localhost:3306/week4'
db = create_engine(db_string)
metadata = MetaData(db)
base = declarative_base(metadata=metadata)
if db:
    print("yeih")

update_tables = db.execute('CALL UpdateTables();')

   
""" EXTRACT """

def extract():
    urls_list = ['https://datos.gob.mx/busca/dataset/elaboracion-de-productos-petroquimicos-derivados-del-metano',
        'https://datos.gob.mx/busca/dataset/precio-publico-ponderado-de-productos-petroliferos-seleccionados',
        'https://datos.gob.mx/busca/dataset/produccion-de-petroleo-crudo-por-activos-y-region-estructura-a-partir-del-2004',]

    file_names_list = []

    for i in urls_list:
        openUrl = urlopen(i)

        try:
            html = openUrl.read().decode('latin-1')
        finally:
            openUrl.close()

        soup = BeautifulSoup(html, "html.parser")

        for link in soup.select('#datasets-list div:nth-of-type(1) div:nth-of-type(3) ul:nth-of-type(1) div:nth-of-type(1) a'):
            href = link.get('href')
            if not any(href.endswith(x) for x in ['csv']):
                continue

            filename = href.rsplit('/', 1)[-1]
            file_names_list.append(filename)
            urlretrieve(href, filename)

    return file_names_list

file_names_list = extract()

# print(file_names_list)

def generate_dates(header_dates):
    years_dict = {}
    heads = list(header_dates)
    heads.pop(0) # Removing NaN
    for i in heads:
        years_dict[i] = ''
    year = 2005
    month = 1
    for key in years_dict.keys():
        if month > 9:
            years_dict[key] = f'{year}-{month}-01'
        else:
            years_dict[key] = f'{year}-0{month}-01'
        if month >= 12:
            year += 1
            month = 1
            continue
        month +=1 
    
    return years_dict

""" TRANSFORM """
id = 1
def generate_list(subset:dict, productTypeId: int, typeId: int, elementLocation: int, heads):
    dates = generate_dates(heads)
    global id
    if dates.keys():
        product = []
        for column, element in subset.items():
            if element[elementLocation] == 'N/D' or element[elementLocation] =='0':
                continue
            if column in dates.keys():
                product.append({
                    'ID': id,
                    'ProductTypeID': productTypeId,
                    'TypeID': typeId,
                    'Price': element[elementLocation],
                    'Date': f"'{dates[column]}'"
                })
                id +=1
        if product != []: 
            return product
        return "Empty subset"

""" Petrochemicals START"""
data = pandas.read_csv(file_names_list[0], sep=',', header=None, skiprows=6, nrows=1)
data.convert_dtypes().dtypes

heads_petro = data.to_numpy()[0]
heads_petro[0] = 'Products'
dataSet = pandas.read_csv(file_names_list[0], sep=',', names=heads_petro, skiprows=10, header=None)
df_list = np.split(dataSet, dataSet[dataSet.isnull().all(1)].index)


methane_derivatives = df_list[0].dropna()
ethylene_derivatives = df_list[1].dropna()
aromatics_derivatives = df_list[2].dropna()
propylene_derivatives = df_list[3].dropna()
otros = df_list[4].dropna()
residuoLargoLigero = df_list[7].dropna()

# Methane derivates
anh_carbon = generate_list(methane_derivatives, 1, 1, 1, heads_petro)
for i in anh_carbon:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

ammonia = generate_list(methane_derivatives, 2, 1, 2, heads_petro)
for i in ammonia:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")


methanol = generate_list(methane_derivatives, 3, 1, 3, heads_petro)
for i in methanol:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

# Ethylene derivatives
ethylene = generate_list(ethylene_derivatives, 4, 2, 6, heads_petro)
for i in ethylene:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

dichloroethane = generate_list(ethylene_derivatives, 5, 2, 7, heads_petro)
print(dichloroethane)
for i in dichloroethane:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

ethylene_oxide = generate_list(ethylene_derivatives, 6, 2, 8, heads_petro)
for i in ethylene_oxide:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

polyethylenebd = generate_list(ethylene_derivatives, 7, 2, 9, heads_petro)
for i in polyethylenebd:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

linealpolyethylenebd = generate_list(ethylene_derivatives, 8, 2, 10, heads_petro)
for i in linealpolyethylenebd:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")
# acethaldehyde = generate_list(ethylene_derivatives, 9, 2, 11, heads_petro) # No records

vinyl_chloride = generate_list(ethylene_derivatives, 10, 2, 12, heads_petro)
for i in vinyl_chloride:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

polyethylene_ad = generate_list(ethylene_derivatives, 11, 2, 13, heads_petro)
for i in polyethylene_ad:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

glycols = generate_list(ethylene_derivatives, 12, 2, 14, heads_petro)
for i in glycols:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

#perchlorethylene = generate_list(ethylene_derivatives, 13, 2, 15, heads_petro) # No records

# Aromatics derivatives
xylenes = generate_list(aromatics_derivatives, 14, 3, 18, heads_petro)
for i in xylenes:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

toluene = generate_list(aromatics_derivatives, 15, 3, 19, heads_petro)
for i in toluene:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

paraxylene = generate_list(aromatics_derivatives, 16, 3, 20, heads_petro)
for i in paraxylene:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

ethylbenzene = generate_list(aromatics_derivatives, 17, 3, 21, heads_petro)
for i in ethylbenzene:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

styrene = generate_list(aromatics_derivatives, 18, 3, 22, heads_petro)
for i in styrene:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

aromine = generate_list(aromatics_derivatives, 19, 3, 23, heads_petro)
for i in aromine:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

high_octane_carbon = generate_list(aromatics_derivatives, 20, 3, 24, heads_petro)
for i in high_octane_carbon:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

benzene = generate_list(aromatics_derivatives, 21, 3, 25, heads_petro)
for i in benzene:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

heavy_aromatics = generate_list(aromatics_derivatives, 22, 3, 26, heads_petro)
for i in heavy_aromatics:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

orthoxylene = generate_list(aromatics_derivatives, 23, 3, 27, heads_petro)
for i in orthoxylene:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

fluxoil = generate_list(aromatics_derivatives, 24, 3, 28, heads_petro)
for i in fluxoil:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")
# cumene = generate_list(aromatics_derivatives, 25, 3, 29, heads_petro) # No records

amorphous_gasoline = generate_list(aromatics_derivatives, 26, 3, 30, heads_petro)
for i in amorphous_gasoline:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")


octane_base_gasoline = generate_list(aromatics_derivatives, 27, 3, 31, heads_petro)
for i in octane_base_gasoline:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")
# Propylene derivatives
propylene = generate_list(propylene_derivatives, 28, 4, 34, heads_petro)
for i in propylene:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

acrylonitrile = generate_list(propylene_derivatives, 29, 4, 35, heads_petro)
for i in acrylonitrile:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

# polypropylene = generate_list(propylene_derivatives, 30, 4, 36, heads_petro)
# print(polypropylene)
# for i in polypropylene: """ EMPTY """
#     db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

ac_hydrocyanic = generate_list(propylene_derivatives, 31, 4, 37, heads_petro)
for i in ac_hydrocyanic:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

acetonitrile = generate_list(propylene_derivatives, 32, 4, 38, heads_petro)
for i in acetonitrile:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

isopropanol = generate_list(propylene_derivatives, 33, 4, 39, heads_petro)
for i in isopropanol:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

# Others
others = generate_list(otros, 34, 5, 41, heads_petro)
for i in others:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")

#Light large residue
llr = generate_list(residuoLargoLigero, 35, 6, 47, heads_petro) 
for i in llr:
    db.execute(f"INSERT INTO MethanePetrochemicals VALUES({i['ID']}, {i['Price']}, {i['TypeID']}, {i['ProductTypeID']}, {i['Date']})")
""" Petrochemicals END"""

""" Public price START"""

gasolineIdSql = 1
def generate_gasoline_list(subset:dict, gasolineId: int,  elementLocation: int, heads):
    global gasolineIdSql
    dates = generate_dates(heads)
    if dates.keys():
        product = []
        for column, element in subset.items():
            if element[elementLocation] == 'N/D' or element[elementLocation] =='0':
                continue
            if column in dates.keys():
                product.append({
                    'ID': gasolineIdSql,
                    'GasolineId': gasolineId,
                    'Price': element[elementLocation],
                    'Date': f"'{dates[column]}'"
                })
                gasolineIdSql +=1
        if product != []:
            return product
        return "empty subset"

public_price = pandas.read_csv(file_names_list[1], sep=',', header=None, skiprows=7, nrows=1)
public_price.convert_dtypes().dtypes
heads_prices = public_price.to_numpy()[0]
heads_prices[0] = 'Products'

dataSet_prices = pandas.read_csv(file_names_list[1], sep=',', names=heads_prices, skiprows=9, header=None)

df_prices_list = np.split(dataSet_prices, dataSet_prices[dataSet_prices.notnull().all(1)].index)

pemex_magna = df_prices_list[1].dropna()
pemex_premium = df_prices_list[2].dropna()
pemex_diesel = df_prices_list[3].dropna()
heavy_gasoline = df_prices_list[4].dropna()
national_marine_diesel = df_prices_list[5].dropna()

pm = generate_gasoline_list(pemex_magna, 1, 0, heads_prices)
for i in pm:
    db.execute(f"INSERT INTO GasolinePrices VALUES({i['ID']}, {i['GasolineId']}, {i['Price']}, {i['Date']})")

pp = generate_gasoline_list(pemex_premium, 2, 1, heads_prices)
for i in pp:
    db.execute(f"INSERT INTO GasolinePrices VALUES({i['ID']}, {i['GasolineId']}, {i['Price']}, {i['Date']})")

pd = generate_gasoline_list(pemex_diesel, 3, 2, heads_prices)
for i in pd:
    db.execute(f"INSERT INTO GasolinePrices VALUES({i['ID']}, {i['GasolineId']}, {i['Price']}, {i['Date']})")

hg = generate_gasoline_list(heavy_gasoline, 4, 3, heads_prices)
for i in hg:
    db.execute(f"INSERT INTO GasolinePrices VALUES({i['ID']}, {i['GasolineId']}, {i['Price']}, {i['Date']})")

nmd = generate_gasoline_list(national_marine_diesel, 5, 4, heads_prices)
for i in nmd:
    db.execute(f"INSERT INTO GasolinePrices VALUES({i['ID']}, {i['GasolineId']}, {i['Price']}, {i['Date']})")
""" Public price END"""


"""Actives per region START"""
data = pandas.read_csv('SENER_05_ProduccionPetroleoCrudoPorActivosRegion-PMXB1C05.csv', sep=',', header=None, skiprows=6, nrows=1)
data.convert_dtypes().dtypes

heads = data.to_numpy()[0]

heads[0] = 'Products'
dataSet = pandas.read_csv(file_names_list[2], sep=',', names=heads, skiprows=10, header=None)
df_list = np.split(dataSet, dataSet[dataSet.isnull().all(1)].index)

activesId = 1
def generate_actives_list(subset: dict, regionId: int, activeCodeId: int, elementLocation: int, heads):
    dates = generate_dates(heads)
    global activesId 
    active = []
    for column, element in subset.items():
        if element[elementLocation] == 'N/D' or element[elementLocation] == '0':
            continue
        if column in dates.keys():
            active.append({
                'ID': activesId,
                'RegionId': regionId,
                'ActiveCodeId': activeCodeId,
                'Price': element[elementLocation],
                'Date': f"'{dates[column]}'"
            })
            activesId += 1
    return active

north_marine_region = df_list[0].dropna()
north_marine_total = generate_actives_list(north_marine_region, 1, None, 0, heads)
cantarell = generate_actives_list(north_marine_region, 2, 1, 1, heads)
for i in cantarell:
    db.execute(f"INSERT INTO Actives VALUES({i['ID']}, {i['RegionId']}, {i['ActiveCodeId']}, {i['Price']}, {i['Date']})")

ku_maloob = generate_actives_list(north_marine_region, 3, 1, 2, heads)
for i in ku_maloob:
    db.execute(f"INSERT INTO Actives VALUES({i['ID']}, {i['RegionId']}, {i['ActiveCodeId']}, {i['Price']}, {i['Date']})")

southwest = df_list[1].dropna()
southwest_total = generate_actives_list(southwest, 2, None, 4, heads)
abkatun = generate_actives_list(southwest, 2, 3, 5, heads)
for i in abkatun:
    db.execute(f"INSERT INTO Actives VALUES({i['ID']}, {i['RegionId']}, {i['ActiveCodeId']}, {i['Price']}, {i['Date']})")

tabasco = generate_actives_list(southwest, 2, 4, 6, heads)
for i in tabasco:
    db.execute(f"INSERT INTO Actives VALUES({i['ID']}, {i['RegionId']}, {i['ActiveCodeId']}, {i['Price']}, {i['Date']})")

south = df_list[2].dropna()
south_total = generate_actives_list(south, 3, None, 8, heads)
cinco_presidentes = generate_actives_list(south, 3, 5, 9, heads)
for i in cinco_presidentes:
    db.execute(f"INSERT INTO Actives VALUES({i['ID']}, {i['RegionId']}, {i['ActiveCodeId']}, {i['Price']}, {i['Date']})")

bellota = generate_actives_list(south, 3, 6, 10, heads)
for i in bellota:
    db.execute(f"INSERT INTO Actives VALUES({i['ID']}, {i['RegionId']}, {i['ActiveCodeId']}, {i['Price']}, {i['Date']})")

macuspana = generate_actives_list(south, 3, 7, 11, heads)
for i in macuspana:
    db.execute(f"INSERT INTO Actives VALUES({i['ID']}, {i['RegionId']}, {i['ActiveCodeId']}, {i['Price']}, {i['Date']})")

samaria_luna = generate_actives_list(south, 3, 8, 12, heads)
for i in samaria_luna:
    db.execute(f"INSERT INTO Actives VALUES({i['ID']}, {i['RegionId']}, {i['ActiveCodeId']}, {i['Price']}, {i['Date']})")


north = df_list[3].dropna()
north_total = generate_actives_list(north, 4, None, 14, heads)
burgos = generate_actives_list(north, 4, 9, 15, heads)
for i in burgos:
    db.execute(f"INSERT INTO Actives VALUES({i['ID']}, {i['RegionId']}, {i['ActiveCodeId']}, {i['Price']}, {i['Date']})")

poza_rica = generate_actives_list(north, 4, 10, 16, heads)
for i in poza_rica:
    db.execute(f"INSERT INTO Actives VALUES({i['ID']}, {i['RegionId']}, {i['ActiveCodeId']}, {i['Price']}, {i['Date']})")

aceite_golfo = generate_actives_list(north, 4, 11, 17, heads)
for i in aceite_golfo:
    db.execute(f"INSERT INTO Actives VALUES({i['ID']}, {i['RegionId']}, {i['ActiveCodeId']}, {i['Price']}, {i['Date']})")

veracruz = generate_actives_list(north, 4, 12, 18, heads)
for i in veracruz:
    db.execute(f"INSERT INTO Actives VALUES({i['ID']}, {i['RegionId']}, {i['ActiveCodeId']}, {i['Price']}, {i['Date']})")
"""Actives per region END"""
