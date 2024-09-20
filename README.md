# CARLIFORNIA-HOUSE-PREDICTION

br>

<img src="image3.jpg" alt="Image description" width="1200" height="1000">

<br>

The US Census Bureau has published California Census Data which has 10 types of metrics such as the population, median income, median housing price, and so on for each block group in California. The dataset also serves as an input for project scoping and tries to specify the functional and nonfunctional r requirements for it.

**Problem Objective:**
The project aims at building a model of housing prices to predict median house values in California using the provided dataset. This model should learn from the data and be able to predict the median housing price in any district, given all the other metrics.

Districts or block groups are the smallest geographical units for which the US Census Bureau publishes sample data (a block group typically has a population of 600 to 3,000 people). There are 20,640 districts in the project dataset.


## Approach

* Import Libraries
* Data Reading 
* Exploratory Data Analysis
* Feature Engineering
* Train - Test Split
* Preprocessing
* Model Building
* Model Evaluation
* Cross Validation

## Data Dictionary

| Column Name         | Data Type                | Description                                                                                         |
|---------------------|--------------------------|-----------------------------------------------------------------------------------------------------|
| `longitude`         | float (signed numeric)    | Longitude value for the block in California, USA                                                     |
| `latitude`          | float (numeric)           | Latitude value for the block in California, USA                                                      |
| `housing_median_age`| int (numeric)             | Median age of the house in the block                                                                 |
| `total_rooms`       | int (numeric)             | Count of the total number of rooms (excluding bedrooms) in all houses in the block                   |
| `total_bedrooms`    | float (numeric)           | Count of the total number of bedrooms in all houses in the block                                     |
| `population`        | int (numeric)             | Count of the total number of population in the block                                                 |
| `households`        | int (numeric)             | Count of the total number of households in the block                                                 |



