CREATE TABLE Types(
    Id SERIAL PRIMARY KEY,
    Name varchar(100) NOT NULL
);


CREATE TABLE ProductTypes(
    Id SERIAL PRIMARY KEY,
    Name varchar(100) NOT NULL
);

CREATE TABLE MethanePetrochemicals (
    Id SERIAL PRIMARY KEY,
    Price DECIMAL,
    TypeId INT references Types(Id),
    ProductTypeId INT references ProductTypes (Id),
    CreationDate date
);




CREATE TABLE GasolineType(
    Id SERIAL PRIMARY KEY,
    Name varchar(100) NOT NULL
);

CREATE TABLE GasolinePrices(
    Id INT SERIAL PRIMARY KEY,
    GasolineTypeId INT REFERENCES GasolineType(Id),
    CreationDate DATE,
    Price DECIMAL
)



CREATE TABLE Region (
    Id SERIAL PRIMARY KEY,
    Name varchar(100) NOT NULL
)

CREATE TABLE ActiveCode (
    Id, SERIAL PRIMARY KEY,
    Name varchar(200) NOT NULL
)

CREATE TABLE Actives(
    Id SERIAL PRIMARY KEY,
    RegionId INT REFERENCES Region(Id),
    ActiveCodeId INT REFERENCES ActiveCode(Id),
    Price DECIMAL
    CreationDate Date,
)