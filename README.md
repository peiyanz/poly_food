#Polyfood

#####Project Description:
Polyfood allows users to quickly identify the category, price range, quality and popularity of the restaurants within a custom defined polygon region on the map. Users can draw/edit/move multiple polygons directly on a map, the app then displays restaurants within each polygon area and filter out restaurants based on type of food, restaurant's rating, and many other filters. It also allows the user to compare the results by interacting with D3 built animated graphs.
![](https://github.com/peiyan08/poly_food/readme_img/landing_page.png?raw=true "Landing Page")


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
1.When the user is done drawing, it will automatically return all the restaurant info from both my database and the yelp api. Different sizes of circles represent the number of reviews for that restaurant and different colors represent the review stars of that restaurant. 
So, for example, big red circle means this restaurant is very popular and has good qualities. 
![](https://github.com/peiyan08/poly_food/readme_img/draw_polygon.gif?raw=true "Landing Page")


## <a name="challenges"></a>Challenges
1. Determining if a point exits in a polygon, the strightforward mathmatical python implementation takes 5 seconds to determine 140,000 points, while the optimized numpy solution cut it down ot 0.1 second.
2. Utilizing multi-threading to send a batch call of 20 Yelp API(offset 50*n every time) calls to retrieve up to 1000 restaurants results per batch call. It allows more results within a faster turn around time.

3.Setting up a chain of listerners to auto detect user behaviors, such as automatically trigger showing restaurants within that polygon when people finish draw/resize/move.


## <a name="aboutme"></a>About Me
I received my Bachelor of Science degree from Lehigh University where I double majored in Finance and Information System. After graduating, I worked as a Product Manager. In this role, I identified and implemented critical improvements to the company’s operations and built prototype web applications that improve operational inefficiencies across the team. I thought it was cool to help a lot of people saving a lot of manual work by coding, so I decided to transition to be a engineer. 