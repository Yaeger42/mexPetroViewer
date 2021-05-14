CREATE  PROCEDURE week4.UpdateTables()
language sql
BEGIN
    DROP TABLE IF EXISTS week4.MethanePetrochemicals;
    DROP TABLE IF EXISTS week4.GasolinePrices;
    DROP TABLE IF EXISTS week4.Actives;
    DROP TABLE IF EXISTS week4.GasolineType;
    DROP TABLE IF EXISTS week4.ProductTypes;
    DROP TABLE IF EXISTS week4.Region;
    DROP TABLE IF EXISTS week4.ActiveCode;
    DROP TABLE IF EXISTS week4.Types;

    CREATE TABLE week4.Types(
        Id SERIAL PRIMARY KEY,
        Name varchar(100) NOT NULL
    );

    CREATE TABLE week4.ProductTypes(
        Id SERIAL PRIMARY KEY,
        Name varchar(100) NOT NULL
    );

    CREATE TABLE week4.GasolineType(
        Id SERIAL PRIMARY KEY,
        Name varchar(100) NOT NULL
    );


    CREATE TABLE week4.Region (
        Id SERIAL PRIMARY KEY,
        Name varchar(100) NOT NULL
    );

    CREATE TABLE week4.ActiveCode (
        Id SERIAL PRIMARY KEY,
        Name varchar(200) NOT NULL
    );

    CREATE TABLE week4.MethanePetrochemicals (
        Id SERIAL PRIMARY KEY,
        Price BIGINT,
        TypeId INT references Types(Id),
        ProductTypeId INT references ProductTypes (Id),
        CreationDate date
    );
    CREATE TABLE week4.GasolinePrices(
        Id  SERIAL PRIMARY KEY,
        GasolineTypeId INT REFERENCES GasolineType(Id),
        Price DECIMAL,
        CreationDate DATE
    );

    CREATE TABLE week4.Actives(
        Id SERIAL PRIMARY KEY,
        RegionId INT REFERENCES Region(Id),
        ActiveCodeId INT REFERENCES ActiveCode(Id),
        Price DECIMAL,
        CreationDate Date
    );

    INSERT INTO week4.Types VALUES(1, 'Derivados del metano');
    INSERT INTO week4.Types VALUES(2, 'Derivados del etano');
    INSERT INTO week4.Types VALUES(3, 'Aromaticos y derivados');
    INSERT INTO week4.Types VALUES(4, 'Propileno y derivados');
    INSERT INTO week4.Types VALUES(5, 'Otros');
    INSERT INTO week4.Types VALUES(6, 'Residuo largo ligero');

        INSERT INTO week4.ProductTypes VALUES(1, 'Anh. Carbonico');
    INSERT INTO week4.ProductTypes VALUES(2, 'Amoniaco');
    INSERT INTO week4.ProductTypes VALUES(3, 'Metanol');
    INSERT INTO week4.ProductTypes VALUES(4, 'Etileno');
    INSERT INTO week4.ProductTypes VALUES(5, 'Dicloroetano');
    INSERT INTO week4.ProductTypes VALUES(6, 'Oxido de Etileno');
    INSERT INTO week4.ProductTypes VALUES(7, 'Polietileno B.D.');
    INSERT INTO week4.ProductTypes VALUES(8, 'Polietileno Lineal B.D.');
    INSERT INTO week4.ProductTypes VALUES(9, 'Acetaldehido');
    INSERT INTO week4.ProductTypes VALUES(10, 'Cloruro de Vinilo');
    INSERT INTO week4.ProductTypes VALUES(11, 'Polietileno A.D.');
    INSERT INTO week4.ProductTypes VALUES(12, 'Glicoles');
    INSERT INTO week4.ProductTypes VALUES(13, 'Percloroetileno');
    INSERT INTO week4.ProductTypes VALUES(14, 'Xilenos');
    INSERT INTO week4.ProductTypes VALUES(15, 'Tolueno');
    INSERT INTO week4.ProductTypes VALUES(16, 'Paraxileno');
    INSERT INTO week4.ProductTypes VALUES(17, 'Etilbenceno');
    INSERT INTO week4.ProductTypes VALUES(18, 'Estireno');
    INSERT INTO week4.ProductTypes VALUES(19, 'Aromina 100');
    INSERT INTO week4.ProductTypes VALUES(20, 'Hidrocarburo de Alto Octano');
    INSERT INTO week4.ProductTypes VALUES(21, 'Benceno');
    INSERT INTO week4.ProductTypes VALUES(22, 'Aromaticos Pesados');
    INSERT INTO week4.ProductTypes VALUES(23, 'Ortoxileno');
    INSERT INTO week4.ProductTypes VALUES(24, 'Fluxoil');
    INSERT INTO week4.ProductTypes VALUES(25, 'Cumeno');
    INSERT INTO week4.ProductTypes VALUES(26, 'Gasolina Amorfa');
    INSERT INTO week4.ProductTypes VALUES(27, 'Gasolina Base Octano');
    INSERT INTO week4.ProductTypes VALUES(28, 'Propileno');
    INSERT INTO week4.ProductTypes VALUES(29, 'Acrilonitrilo');
    INSERT INTO week4.ProductTypes VALUES(30, 'Polipropileno');
    INSERT INTO week4.ProductTypes VALUES(31, 'Ac. Cianhidrico');
    INSERT INTO week4.ProductTypes VALUES(32, 'Acetonitrilo');
    INSERT INTO week4.ProductTypes VALUES(33, 'Isopropanol');
    INSERT INTO week4.ProductTypes VALUES(34, 'Others');
    INSERT INTO week4.ProductTypes VALUES(35, 'Residuo largo ligero');


    INSERT INTO week4.GasolineType VALUES(1, 'Pemex Magna');
    INSERT INTO week4.GasolineType VALUES(2, 'Pemex Premium');
    INSERT INTO week4.GasolineType VALUES(3, 'Pemex Diesel');
    INSERT INTO week4.GasolineType VALUES(4, 'Combustoleo pesado');
    INSERT INTO week4.GasolineType VALUES(5, 'Diesel Marino Nacional');

    INSERT INTO week4.Region VALUES(1, 'Region Marina Noreste');
    INSERT INTO week4.Region VALUES(2, 'Region Marina Suroeste');
    INSERT INTO week4.Region VALUES(3, 'Region Sur');
    INSERT INTO week4.Region VALUES(4, 'Region Norte');

    INSERT INTO week4.ActiveCode VALUES (1, 'Activo de Producción Cantarell');
    INSERT INTO week4.ActiveCode VALUES (2, 'Activo de Producción Ku-Maloob-Zaap');
    INSERT INTO week4.ActiveCode VALUES (3, 'Activo de Producción Abkatún-Pol Chuc');
    INSERT INTO week4.ActiveCode VALUES (4, 'Activo de Producción Litoral de Tabasco');
    INSERT INTO week4.ActiveCode VALUES (5, 'Activo de Producción Cinco Presidentes');
    INSERT INTO week4.ActiveCode VALUES (6, 'Activo de Producción Bellota-Jujo');
    INSERT INTO week4.ActiveCode VALUES (7, 'Activo de Producción Macuspana-Muspac');
    INSERT INTO week4.ActiveCode VALUES (8, 'Activo de Producción Samaria-Luna');
    INSERT INTO week4.ActiveCode VALUES (9, 'Activo Integral Burgos');
    INSERT INTO week4.ActiveCode VALUES (10, 'Activo de Produccioón Poza Rica-Altamira');
    INSERT INTO week4.ActiveCode VALUES (11, 'Activo Integral Aceite Terciario del Golfo');
    INSERT INTO week4.ActiveCode VALUES (12, 'Activo Integral Veracruz');
END