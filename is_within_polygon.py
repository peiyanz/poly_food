def pointInPolygon(polySides, polyY,  polyX, x, y):
    i, j = polySides-1, polySides-1
    oddNodes = False

    for i in range(0, polySides):
        if ((polyY[i]< y and polyY[j]>=y or
             polyY[j]< y and polyY[i]>=y) and
           (polyX[i]<=x or polyX[j]<=x)):
            oddNodes^=(polyX[i]+(y-polyY[i])/(polyY[j]-polyY[i])*(polyX[j]-polyX[i])<x)
        j=i; 

    return oddNodes; 

# from shapely.geometry import Polygon, Point

# def poly_contains(polyY, polyX, 
#                   longitude,
#                   latitude):
#     poly = Polygon((zip(polyX, polyY)))
#     a =poly.boundary.contains((latitude,longitude))
#     return a




