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

Sofia is a young millenial looking to break into the Edmonton housing market. She would like to [explore] what type of property she can afford in Strathcona County and [compare] the features of these properties.

Sofia can assess this by using our "Strathcona County Housing Prices" dashboard. She can begin by using the map function to identify her desired neighbourhood. This will display the most current average statistics for property price and type of property in that area. She can also use the line chart of assessment value across time (available dates are 2017 to 2022) to visualize the trends in the housing market, and to determine whether a house in this neighbourhood would be a viable long-term investment. Finally, she can use the dropdown bar to filter the values of property type, fireplace, basement, and garage as well as the slider to filter by year range to recieve summary statistics for all properties matching her requirements.

Additionally, if Sofia flips to the second page, she can use our predictive model to estimate the future value of a house. To do this she would select the desired feature values and click the 'predict' button, this would then return the predicted house value.

Based on this information Sofia can make more informed decisions about the Strathcona Counting housing market, to determine whether she can afford a place that meets her criteria and if property is a suitable investment.