# Milestone 1 - Dashboard Proposal

## Section 2 Description of the data
Our project will delve into a detailed dataset representing the housing market in Strathcona County, Edmonton, covering the period from 2017 to the present. The initial part of this dataset, focusing on the year 2017, is based on property valuations as of July 1, 2017, and conditions as of December 31, 2017. It's crucial to note that while this data is provided by Strathcona County, the accuracy of the information isn't guaranteed, nor does the County accept liability for its use.

The dataset spans several years and encompasses a variety of key variables that are instrumental in portraying the diverse aspects of residential properties in Strathcona County. These variables are grouped into several categories:

1. Property Identification and Financial Data: This includes tax_year, roll_num (a unique property identifier), and assessment (the property's assessed value for taxation).

2. Property Characteristics: Detailed descriptions are offered through address, year_built, assessclas (assessment classification), bldg_desc (building description), and measurements like bldg_metre and bldg_feet.

3. Additional Features: Characteristics such as the presence of a garage, fireplace, and basement, as well as basement development status (bsmtdevl), are included.

Our exploratory data analysis (EDA) will be shared in our GitHub repository. This analysis will help us identify the most relevant variables and patterns for a more focused and impactful visualization effort.

## Section 3 Research questions and usage scenarios

Sofia is an airbnb host who wants to obtain the optimal price for her Vancouver airbnb property. She would like to [explore] the prices and features of other properties, [compare] her property to similar listings, and [predict] the price of a new listing.

Sofia can assess this by using our "Vancouver Airbnb Listings" dashboard. She can begin by using the map function to view the Vancouver neighbourhoods and the number of listings in each. Then she can use the dropdown filters to focus her comparison on specific types of properties, she can filter for the values: number of bedrooms, number of bathrooms, number of people to accomodate, neighbourhood, and type of property. She can also use the slider to select a range of prices. This will display the most current summary statistics for properties meeting the selected criteria. From this she can compare her listing to other similar airbnb properties. She can also use the line chart of listing values across time (available dates are quarterly for 2023) to visualize the most recent trends in listing prices. This will help her price her listing effectively, as she can adjust to the changing market.

Additionally, if Sofia goes to the second page of our dashboard, she can use our predictive model to estimate the price range for a new listing. To do this she would select the values that match her new property from the dropdown menu and click the 'predict' button. This would then return the predicted price range of properties matching these criteria. This would help Sofia find an appropriate price for her new new airbnb listing, making it attractive to people looking to book airbnbs in Vancouver.
