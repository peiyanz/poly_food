import unittest
from unittest import TestCase
from server import app
from is_within_polygon import inside_polygon_math
import pandas as pd
from sqlalchemy import create_engine

class FlaskTests(TestCase):

    def setUp(self):
      """Stuff to do before every test."""

      self.client = app.test_client()
      app.config['TESTING'] = True

    def tearDown(self):
      """Stuff to do after each test."""

    def test_homepage(self):
        """Test if the map has been loaded correctly"""

        result = self.client.get("/")
        self.assertIn('<div id=\'map\'>', result.data)

    def test_polygon_test(self):
        """Test if the logic of determining if a point is within a polygon"""
        polyX = [-122.4157812986117, -122.41769631968708, -122.3954820751972]
        polyY = [37.7859575588399, 37.774303066407754, 37.77869263640672]
        points = pd.DataFrame({'name':'test', 'latitude': [-122.410709],
                               'longitude': [37.789806]})
        x =points.longitude
        y = points.latitude
        result = points.loc[inside_polygon_math(polyY, polyX, x, y)]
        if result.empty == True:
            check = "empty"
        else:
            check = "not empty"
        self.assertIn("empty", check)

    def test_dbt(self):
        """Test read from db"""
        engine = create_engine('postgresql://peiyan:peiyan@localhost:8000/peiyan')
        db_points = pd.read_sql_query("select price from restaurant where id='tacorea-san-francisco';",con=engine)
        result =  db_points['price'].iloc[0]
        self.assertIn("$", result)

if __name__ == "__main__":
    unittest.main()