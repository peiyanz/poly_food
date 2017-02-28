from sqlalchemy import create_engine
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler



def kmean_clusters():
    engine = create_engine('postgresql://peiyan:peiyan@localhost:8000/peiyan')
    db_points = pd.read_sql_query('SELECT * FROM restaurant',con=engine)
    # new_data = pd.DataFrame({"category": db_points.my_category, "stars": db_points.stars, "price": db_points.price, "review_count":db_points.review_count})

    c = pd.get_dummies(db_points.my_category)
    p = pd.get_dummies(db_points.price)
    result = pd.concat([c, p], axis=1, join = 'inner')
    # rest = pd.DataFrame({"stars": db_points.stars, "review_count":db_points.review_count})
    rest = db_points[['review_count','stars']] #, 
    final_result = pd.concat([result, rest], axis=1, join='inner')

    X = StandardScaler().fit_transform(final_result)
    rm = final_result['review_count'].mean()
    rstd = final_result['review_count'].std()
    final_result['review_count'] -= rm
    final_result['review_count'] /= rstd
    X = final_result
    kmeans = KMeans(n_clusters = 4, max_iter=1000, random_state=2, precompute_distances="auto", algorithm="auto").fit(X)
    db_points['clustering'] = kmeans.labels_
    # db_points['clustering'] = db_points['clustering'].map(lambda x: str(x))
    
    return db_points