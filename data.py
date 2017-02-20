import json
import pandas as pd
import io
from is_within_polygon import inside_polygon_math
import time


def is_in_polygon(polyY, polyX, points):
    """Only return all the points that lives in the polygon"""

    time1 = time.time()
    x, y = points.longitude, points.latitude
    info = points.loc[inside_polygon_math(polyY, polyX, x, y)]

    time2 = time.time()
    print '%s function took %0.3f ms' % ("inside_polygon_math", (time2-time1)*1000.0)
    
    info_json = info.to_json(orient = "records")
    return info_json



