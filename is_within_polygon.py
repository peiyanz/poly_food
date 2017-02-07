# polySides  =  5
# polyX =  [-115.199995549,
#           -115.195085683,
#           -115.1087298,
#           -115.162160698,
#           -115.200861996]
# polyY = [36.1950122039,
#           36.1579440924,
#           36.1656389161,
#           36.1889519511,
#           36.1952452812
#         ]
# x, y  =  [-115.108523,36.212760]

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

# print pointInPolygon(polySides, polyY,  polyX, x, y)



