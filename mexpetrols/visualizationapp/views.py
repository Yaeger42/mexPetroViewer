from django.http import JsonResponse
# Create your views here.

def methane_derivatives(request):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("""
    SELECT
    mp.id 'Id', 
    mp.Price 'Precio',
    t.Name 'Tipo_de_producto',
    PT.Name 'Nombre_de_Producto',
    mp.CreationDate 'CreationDate'
    FROM MethanePetrochemicals mp
    JOIN Types t on mp.TypeId = t.Id
    JOIN ProductTypes PT on mp.ProductTypeId = PT.Id
    ;""")
    row = cursor.fetchall()
    cont = list(row)
    response = []
    for id, price, typepr, namep, creation_date in cont:
            context = {}
            context['id'] = id
            context['price'] = price
            context['productType'] = typepr
            context['productName'] = namep
            context['creationDate'] = creation_date
            response.append(context)

    return JsonResponse(data=response, safe=False)
    # return render(request, 'index.html', {'context': context})


    

def gasoline_prices(request):
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("""
    SELECT
        g.id,
        gt.Name,
        g.Price,
        g.CreationDate
    FROM 
        GasolinePrices g
    JOIN GasolineType gt on gt.Id = g.id;
    """)
    row = list(cursor.fetchall())
    response = []
    for id, name, price, dt in row:
        context = {}
        context['id'] = id
        context['name'] = name
        context['price'] = price
        context['creationDate'] = dt
        response.append(context)

    return JsonResponse(data=response, safe=False) 
