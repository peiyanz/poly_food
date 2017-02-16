# def pointInPolygon(polySides, polyY,  polyX, x, y):
#     i, j = polySides-1, polySides-1
#     oddNodes = False

#     for i in range(0, polySides):
#         if ((polyY[i]< y and polyY[j]>=y or
#              polyY[j]< y and polyY[i]>=y) and
#            (polyX[i]<=x or polyX[j]<=x)):
#             oddNodes^=(polyX[i]+(y-polyY[i])/(polyY[j]-polyY[i])*(polyX[j]-polyX[i])<x)
#         j=i; 

#     return oddNodes; 

import numpy as np

def points_in_poly(py, px, x, y):   
    index = x.index
    py, px, x, y = map(np.array, [py, px, x, y])
    py = np.insert(py, 0, py[-1])
    px = np.insert(px, 0, px[-1])
    y = y[:, np.newaxis]
    x = x[:, np.newaxis]
    lessy = y<=py
    morex = x>=px
    idx, l = np.copy(lessy[:,:-1]), np.copy(lessy[:,:-1])
    np.logical_and(lessy[:,:-1], np.negative(lessy[:,1:]), out=idx)
    np.logical_and(np.negative(lessy[:,:-1]), lessy[:,1:], out=l)
    np.logical_or(l, idx, out=idx)
    np.logical_or(morex[:,:-1], morex[:,1:], out=l)
    np.logical_and(l, idx, out=idx)
    r = (px[1:]+(y-py[1:])/(py[:-1]-py[1:])*(px[:-1]-px[1:])<x)
    r[np.negative(idx)] = bool(np.logical_xor.identity)
    return index[np.logical_xor.reduce(r, axis=1)]


