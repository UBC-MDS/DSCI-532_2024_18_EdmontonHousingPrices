# Milestone 1 - Dashboard Proposal

## Section 2 Description of the data
Our project will delve into a detailed dataset representing the housing market in Strathcona County, Edmonton, covering the period from 2017 to the present. The initial part of this dataset, focusing on the year 2017, is based on property valuations as of July 1, 2017, and conditions as of December 31, 2017. It's crucial to note that while this data is provided by Strathcona County, the accuracy of the information isn't guaranteed, nor does the County accept liability for its use.

The dataset spans several years and encompasses a variety of key variables that are instrumental in portraying the diverse aspects of residential properties in Strathcona County. These variables are grouped into several categories:

1. Property Identification and Financial Data: This includes tax_year, roll_num (a unique property identifier), and assessment (the property's assessed value for taxation).

2. Property Characteristics: Detailed descriptions are offered through address, year_built, assessclas (assessment classification), bldg_desc (building description), and measurements like bldg_metre and bldg_feet.

3. Additional Features: Characteristics such as the presence of a garage, fireplace, and basement, as well as basement development status (bsmtdevl), are included.

4. Geographical Data: The dataset contains latitude and longitude for spatial analysis, highlighting the exact geographical location of each property in Strathcona County.

We intend to engineer a variable, property_age, derived by subtracting the year_built from the current year, to assess the impact of property age on its value.

While the dataset provides extensive insights into Strathcona County's housing market, additional data like recent sales prices or transaction frequency could further enrich our analysis. Our focus, however, will remain on evaluating property characteristics and assessment trends over the years, offering vital insights for homebuyers, real estate investors, and urban planners in Strathcona County.

Our exploratory data analysis (EDA) will identify key variables and trends for a focused and meaningful visualization. The results of this analysis, along with our visualizations, will be collated and shared in a GitHub repository for detailed examination and collaborative study.
