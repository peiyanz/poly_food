from yelp.api.v3 import Yelp
from constant import app_id, app_secret
import pandas as pd
import time
from sqlalchemy import create_engine


yelp = Yelp(
    app_id,
    app_secret,
)
engine = create_engine('postgresql://peiyan:peiyan@localhost:8000/peiyan')
existing_data = pd.read_sql_query('SELECT * FROM restaurants',con=engine)

# Simple Examples
# print yelp.search(term='food', latitude=37.773972, longitude=-122.431297, radius=1000, limit=1)

# print yelp.autocomplete(text='pizza', latitude=37.77493, longitude=-122.419415)


def api_call(latitude, longitude, radius, offset):
    time1 = time.time()
    # results = yelp.search(term='food', latitude=37.773972, longitude=-122.431297, radius=1000, offset=offset,limit=1)
    results = yelp.search(term='restaurants', latitude=latitude, longitude=longitude, radius=radius, offset=offset+950,limit=50)
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
        id = []
        # for r in results:#, restaurants3, restaurants4, restaurants5]:
        for i in results.get('businesses'):
            id.append(i.get('id'))
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


        rest_info = pd.DataFrame({"id": id, "name": name, "category": category, "address": location, "latitude": latitude, "longitude": longitude,
                      "stars": rating, "price": price, "review_count": review_count, "url": url, "image": image})
        # print rest_info
        time2 = time.time()
        print '%s function took %0.3f ms' % ("rip", (time2-time1)*1000.0)

        #rest_info is the new data from api call
        
        new_data = rest_info[~rest_info["id"].isin(existing_data["id"].tolist())]
        # print "this is new data"
        # print new_data
        existing_data.append(new_data)
        # print existing_data
        data = new_data.set_index("id")
        data.to_sql('restaurants', engine, if_exists='append')                    
        
        return rest_info

    else: 
        return pd.DataFrame()

