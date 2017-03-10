#Polyfood

#####Project Description:
Polyfood allows users to quickly identify the category, price range, quality and popularity of the restaurants within a custom defined polygon region on the map. Users can draw/edit/move multiple polygons directly on a map, the app then displays restaurants within each polygon area and filter out restaurants based on type of food, restaurant's rating, and many other filters. It also allows the user to compare the results by interacting with D3 built animated graphs.
![](https://github.com/peiyan08/poly_food/blob/master/readme_img/landing_page.png?raw=true "Landing Page")


## Table of Contents
* [Technologies](#technologies)
* [Features](#features)
* [Challenges](#features)
* [About Me](#aboutme)

## <a name="technologies"></a>Technologies
#####Project Tech Stack:
Python, Javascript, D3, Flask, Pandas, Numpy, HTML, CSS,  SQLAlchemy

#####API Used:
Yelp, Mapbox

## <a name="features"></a>Features
1. When the user is done drawing, it will automatically return all the restaurant info from both my database and the yelp API. Different size of dots represent the number of reviews for that restaurant and different colors represent the review stars of that restaurant.So, a large red dot means this restaurant is very popular and has good qualities. 
![](https://github.com/peiyan08/poly_food/blob/master/readme_img/draw_polygon.gif?raw=true "Draw Polygon")


2. The user could view a bar chart and a pie chart which are representing the distribution on the price range top 7 categories restaurants within that region. By hovering over to the specific price or category, it will show the distribution of the other feature. If the user wants to see a specific category restaurant on the map, they can click on the pie chart, and the circles on the map will be filtered to be only that category. When the user double clicks on the pie chart again, it brings back all the restaurants.
![](https://github.com/peiyan08/poly_food/blob/master/readme_img/bar_pie.gif?raw=true "View Bar/Pie chart")

3. Users can resize or move the polygon around, which will generate new data immediately.
![](https://github.com/peiyan08/poly_food/blob/master/readme_img/edit_polygon.gif?raw=true "edit Polygon")

4. Started using machine learning algorithm to cluster all the restaurants. For example, in the map, I have 4 clusters and try to look for insights on how different clusters are distributed geographically to try to find interesting insights. This is just one area that I would like to dig deeper in the future.
![](https://github.com/peiyan08/poly_food/blob/master/readme_img/clusters.gif?raw=true "Clustering Restaurants")


## <a name="challenges"></a>Challenges
1. Determining if a point exits in a polygon, the straightforward mathematical python implementation takes 5 seconds to determine 140,000 points, while the optimized numpy solution cut it down ot 0.1 second.
2. Utilizing multi-threading to send a batch call of 20 Yelp API(offset 50*n every time) calls to retrieve up to 1000 restaurants results per batch call. It allows more results within a faster turn around time.
3. Setting up a chain of Listeners to automatic trigger user behaviors, such as automatically trigger showing restaurants within that polygon when people finish draw/resize/move.


## <a name="aboutme"></a>About Me
I received my Bachelor of Science degree from Lehigh University where I double majored in Finance and Information System. After graduating, I worked as a Product Manager. In this role, I identified and implemented critical improvements to the company’s operations and built prototype web applications that improve operational inefficiencies across the team. I thought it was cool to help a lot of people saving a lot of manual work by coding, so I decided to transition to be a engineer. 