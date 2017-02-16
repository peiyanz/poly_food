from yelp.api.v3 import Yelp
from constant import app_id, app_secret
import pandas as pd
import time


yelp = Yelp(
    app_id,
    app_secret,
)

# Simple Examples
# print yelp.search(term='food', latitude=37.773972, longitude=-122.431297, radius=1000, limit=1)

# print yelp.autocomplete(text='pizza', latitude=37.77493, longitude=-122.419415)


def api_call(latitude, longitude, radius, offset):
    time1 = time.time()
    # results = yelp.search(term='food', latitude=37.773972, longitude=-122.431297, radius=1000, offset=offset,limit=1)
    results = yelp.search(term='restaurants', latitude=latitude, longitude=longitude, radius=radius, offset=offset,limit=50)
    if results.get("total") > 0:
        print "total"
        print results.get("total")
        category = []
        location = []
        longitude = []
        latitude = []
        rating = []
        review_count = []
        price = []
        url = []
        image = []
        name = []
        # for r in results:#, restaurants3, restaurants4, restaurants5]:
        for i in results.get('businesses'):
            category.append(i.get('categories')[0].get("alias") )
            location.append(i.get('location').get("display_address"))
            longitude.append(i.get('coordinates').get('longitude'))
            latitude.append(i.get('coordinates').get('latitude'))
            rating.append(i.get('rating'))
            review_count.append(i.get('review_count'))
            price.append(i.get('price'))
            url.append(i.get('url'))
            image.append(i.get('image_url'))
            name.append(i.get('name'))


        rest_info = pd.DataFrame({"name": name, "category": category, "address": location, "latitude": latitude, "longitude": longitude,
                      "stars": rating, "price": price, "review_count": review_count, "url": url, "image": image})
        # print rest_info
        time2 = time.time()
        print '%s function took %0.3f ms' % ("rip", (time2-time1)*1000.0)

        return rest_info

    else: 
        return pd.DataFrame()

