import json
import pandas as pd
import csv
import io
from is_within_polygon import points_in_poly
import time


json_file = open("static/yelp_academic_dataset_business.json").read()
json_text = '[' + ','.join(json_file.strip().split('\n')) + ']'

rest_info_local = pd.read_json(json_text) #all restaurant info
# rest_info = rest_info[rest_info["state"] == 'NV']

rest_info_local = pd.DataFrame({'address': rest_info_local['address']+ " " +rest_info_local['city']+ " " +rest_info_local['state']+ " "+ rest_info_local['postal_code'],
                        'name': rest_info_local['name'],
                        # 'hours': rest_info_local['hours'],
                        'review_count': rest_info_local['review_count'],
                        'stars': rest_info_local['stars'],
                        'latitude': rest_info_local['latitude'],
                        'longitude': rest_info_local['longitude'],
                        'category': rest_info_local['categories']})



def rest_in_poly(polyY, polyX, rest_info_api=None):
    rest_info = rest_info_local
    if rest_info_api is not None:
        rest_info = rest_info_api
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
    # info = rest_info
    info = rest_info.loc[points_in_poly(polyY, polyX, x, y)]
    # print info

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
    # info.to_json("info.json")
    info_json = info.to_json(orient = "records")
    return info_json



