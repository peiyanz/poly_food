from yelp.api.v3 import Yelp
from constant import app_id, app_secret
import pandas as pd
import time
from sqlalchemy import create_engine
from restaurant_category import category_dict



yelp = Yelp(
    app_id,
    app_secret,
)

def call_yelp(latitude, longitude, radius, offset):
    """Sending out a yelp api call with a sepcified center point and radius."""

    results = yelp.search(term='restaurants', latitude=latitude, 
                          longitude=longitude, radius=radius, 
                          offset=offset,limit=50)
    if results.get("total") > 0:
        print "totalresults from api call", results.get('total')
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
        id_ = []

        for i in results.get('businesses'):
            id_.append(i.get('id'))
            if i.get('categories'):
                category.append(i.get('categories')[0].get('alias') )
            else:
                category.append(None)
            location.append(i.get('location').get('display_address'))
            longitude.append(i.get('coordinates').get('longitude'))
            latitude.append(i.get('coordinates').get('latitude'))
            rating.append(i.get('rating'))
            review_count.append(i.get('review_count'))
            price.append(i.get('price'))
            url.append(i.get('url'))
            image.append(i.get('image_url'))
            name.append(i.get('name'))

        # Put all the returned resutls from yelp api to a dataframe
        rest_info = pd.DataFrame({"id": id_, "name": name, "category": category, 
                                  "address": location, "latitude": latitude, 
                                  "longitude": longitude,"stars": rating, 
                                  "price": price, "review_count": review_count, 
                                  "url": url, "image": image})
        

        # Importing the existing_data in the memory
        # engine = create_engine('postgresql://peiyan:peiyan@localhost:8000/peiyan')
        # db_points = pd.read_sql_query('SELECT * FROM restaurant',con=engine)
        db_points = pd.read_csv("restaurants.csv")

        # grab the new data from the api calls that do not exit in the exiting database
        new_data = rest_info[~rest_info["id"].isin(db_points["id"].tolist())]
        new_data['my_category'] = new_data['category'].map(lambda x: category_dict.get(x, 'other'))
        new_db = new_data[new_data['my_category'] != 'other']
        data = new_db.set_index("id")
        # try:
        #     # write new data into database
        #     data.to_sql('restaurant', engine, if_exists='append')  
        # except Exception as err:
        #     print err                  
        
        return new_data

    else: 
        return pd.DataFrame() #return a empty dataframe

