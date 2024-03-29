# Milestone 1 - Dashboard Proposal

## Section 2 Description of the data

Our project will focus on visualizing a comprehensive dataset obtained from the City of Vancouver's Open Data Portal. This dataset consists of seven main dataframes, each corresponding to property tax records for the years 2014 to 2020. Notably, the most recent dataframe (tax_2020) is still being updated and comprises 213,709 rows, while the others, ranging from 2014 to 2019, contain a static number of rows, varying from 200,925 to 213,182. Each dataframe includes 29 columns that provide detailed information about properties in Vancouver.

We will concentrate on several key variables that could offer valuable insights into property trends in Vancouver. The data includes both categorical and numerical types, such as:

Property identification variables like pid, legal_type, land_coordinate, and zone_name.
Descriptive location information including street_name, block, district_lot, and neighbourhood_code.
Financial variables such as current_land_value, current_improvement_value, previous_land_value, and tax_levy.
Temporal variables like year_built, big_improvement_year, and tax_assessment_year.
To enhance our analysis, we plan to engineer a new variable, property_age, calculated as the difference between the current year and the year_built. This variable will allow us to examine trends in property values relative to the age of the properties.

While the dataset is robust, additional information on recent sale prices or frequency of property transactions would have further enriched our analysis, allowing us to understand the real estate market's dynamics better. However, given the dataset's current structure, our focus will be on uncovering patterns and trends in property assessments and tax levies over the years, which can provide valuable insights for potential investors, city planners, and residents of Vancouver.

Our exploratory data analysis (EDA) will be shared in our GitHub repository. This analysis will help us identify the most relevant variables and patterns for a more focused and impactful visualization effort.

## Section 3 Research questions and usage scenarios

Sofia is an airbnb host who wants to obtain the optimal price for her Vancouver airbnb property. She would like to [explore] the prices and features of other properties, [compare] her property to similar listings, and [predict] the price of a new listing.

Sofia can assess this by using our "Vancouver Airbnb Listings" dashboard. She can begin by using the map function to view the Vancouver neighbourhoods and the number of listings in each. Then she can use the dropdown filters to focus her comparison on specific types of properties, she can filter for the values: number of bedrooms, number of bathrooms, number of people to accomodate, neighbourhood, and type of property. She can also use the slider to select a range of prices. This will display the most current summary statistics for properties meeting the selected criteria. From this she can compare her listing to other similar properties. She can also use the line chart of listing values across time (available dates are quareterly for 2023) to visualize the trends in listing prices. This will help her price her listing effectively, as she can adjust to the changing market.

Additionally, if Sofia goes to the second page of our dashboard, she can use our predictive model to estimate the price range for a new listing. To do this she would select the values that match her new property from the dropdown menu and click the 'predict' button. This would then return the predicted price range of properties matching these criteria. This would help Sofia make her new airbnb listing competitive and attractive to people looking to book airbnb's in Vancouver.