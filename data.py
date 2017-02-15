import json
import pandas as pd
import csv
import io
from is_within_polygon import point_in_poly, pointInPolygon
import time


# json_file = open("static/yelp_academic_dataset_business.json").read()
# json_text = '[' + ','.join(json_file.strip().split('\n')) + ']'

# rest_info = pd.read_json(json_text) #all restaurant info
# rest_info = rest_info[rest_info["state"] == 'NV']
# rest_info = pd.DataFrame({'address': rest_info['address']+ " " +rest_info['city']+ " " +rest_info['state']+ " "+ rest_info['postal_code'],
#                         'name': rest_info['name'],
#                         # 'hours': rest_info['hours'],
#                         'review_count': rest_info['review_count'],
#                         'stars': rest_info['stars'],
#                         'latitude': rest_info['latitude'],
#                         'longitude': rest_info['longitude'],
#                         'category': rest_info['categories']})



def rest_in_poly(polyY, polyX, rest_info):
    # restaurant
    time1 = time.time()

    # info = rest_info[rest_info.apply(
    #             lambda x: pointInPolygon(
    #                             polySides, 
    #                             polyY, polyX, 
    #                             x.longitude,
    #                             x.latitude),
    #                             axis = 1) == True]
       
    x, y = rest_info.longitude, rest_info.latitude
    info = rest_info[point_in_poly(polyY, polyX, x, y)]

    time2 = time.time()
    print '%s function took %0.3f ms' % ("rip", (time2-time1)*1000.0)
            
            

                    

    # def rest_in_poly(polySides, polyY, polyX):
    #     info = rest_info[rest_info.apply(
    #                 lambda x: poly_contains( 
    #                                 polyY, polyX, 
    #                                 x.longitude,
    #                                 x.latitude),
    #                                 axis = 1) == True 
    #                     ]
    info.to_json("info.json")
    info_json = info.to_json(orient = "records")
    return info_json



