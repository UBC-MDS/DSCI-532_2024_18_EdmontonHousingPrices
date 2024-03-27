# Milestone 1 - Dashboard Proposal

## Section 1: Motivation and Purpose
Vancouver's housing market has been a major topic of discussion and in many cases a limitation, especially for people looking to move to one of Canada's largest and most scenic cities. As the housing prices rise, students and other newcomers to Vancouver are finding it more and more difficult to find affordable accomodations.

This dashboard offers an interactive platform for people who are looking to move to Vancouver. An interactive map of the city shows the appraised value of homes accross the city, giving the user an idea of which neighborhoods fall within their price-range. View historical data to see housing price trends broken down by size, neighborhood, and other important factors in considering a home. By visualizing breakdowns of the housing market in Vancouver, we hope to make renting or buying in Vancouver a much less daunting task.

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