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

import numpy as np
import pandas as pd


def point_in_poly(py, px, x, y):
    odd_nodes = False & x.astype(bool).copy()
    index = x.index
    py, px, x, y = map(np.array, [py, px, x, y])
    # py = np.insert(py, 0, py[-1])
    # px = np.insert(px, 0, px[-1])
#     y = y[:, np.newaxis]
#     x = x[:, np.newaxis]
#     lessy = y<=py
#     morex = x>=px
#     l1 = np.logical_and(lessy[:,:-1], np.negative(lessy[:,1:]))
#     l2 = np.logical_and(np.negative(lessy[:,:-1]), lessy[:,1:])
#     l3 = np.logical_or(l1, l2)
#     l4 = np.logical_or(morex[:,:-1], morex[:,1:])
#     idx = np.logical_and(l3, l4)
#     r = ((px[1:]+(y-py[1:]))/(py[:-1]-py[1:])*(px[:-1]-px[1:]<x)).astype(bool)
#     # r[np.negative(idx)] = bool(np.logical_xor.identity)
#     # print np.flatnonzero(r), np.flatnonzero(idx)
#     # odd_nodes = np.logical_xor.reduce(np.insert(r, 0, False, axis=1), axis=1)
#     odd_nodes = np.logical_xor.reduce(r, axis=1)
# #     print len(np.flatnonzero(odd_nodes))


    for i in range(len(py)):
        j = i - 1
        l1 = np.logical_and(y<=py[j], y>py[i])
        l2 = np.logical_and(y>py[j], y<=py[i])
        l3 = np.logical_or(l1, l2)
        l4 = np.logical_or(x>=px[j], x>=px[i])
        idx = np.logical_and(l3, l4)
        r = (px[i]+(y-py[i])/(py[j]-py[i])*(px[j]-px[i])<x)
        odd_nodes.iloc[idx] = np.logical_xor(odd_nodes.iloc[idx], r[idx])
    return pd.Series(odd_nodes, index=index)
    # return odd_nodes; 

# from shapely.geometry import Polygon, Point

# def poly_contains(polyY, polyX, 
#                   longitude,
#                   latitude):
#     poly = Polygon((zip(polyX, polyY)))
#     a =poly.boundary.contains((latitude,longitude))
#     return a




