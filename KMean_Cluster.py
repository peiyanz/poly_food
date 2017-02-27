from sqlalchemy import create_engine
import pandas as pd
from sklearn.cluster import KMeans



def kmean_clusters():
    engine = create_engine('postgresql://peiyan:peiyan@localhost:8000/peiyan')
    db_points = pd.read_sql_query('SELECT * FROM restaurant',con=engine)
    # new_data = pd.DataFrame({"category": db_points.my_category, "stars": db_points.stars, "price": db_points.price, "review_count":db_points.review_count})

    c = pd.get_dummies(db_points.category)
    p = pd.get_dummies(db_points.price)
    result = pd.concat([c, p], axis=1, join = 'inner')
    rest = pd.DataFrame({"stars": db_points.stars, "review_count":db_points.review_count})
    final_result = pd.concat([result, rest], axis=1, join='inner')


    X = final_result
    kmeans = KMeans(n_clusters = 5, max_iter=500, random_state=2, precompute_distances="auto", algorithm="auto").fit(X)
    db_points['clustering'] = kmeans.labels_
    db_points['clustering'] = db_points['clustering'].map(lambda x: str(x))
    
    return db_points