## Milestone 2 reflection

In this milestone we built a prototype of our dashboard. We were able to create the major sections of our proposal: applying filters to the data, creating summary statistics, displaying a time-series trend plot, and creating a map to further explore the data. Additionally, we created filters and a simple prediction model for our prediction page and added information about ourself to the credentials page. However, some of the detailed functionality we wanted to implement has not been completed due to time constraints. We found that both the map and summary statistics only appear once a filter value has been selected; this makes the dashboard initially visually unappealing, in further milestones we would like to rectify this issue. We would also like to add more detail to the map by changing the colour of each point to refelct it's price and replacing the information on latitude/longitude with the price for the tooltip. For the summary statistics we would like to add another tab displaying histograms for the categorical variables.

Our main deviation from the initial proposal was that our request for additional data is still under request, meaning we only had access to three yearly quarters of data. We proceeded with this data for the filtering, summary statistics and map. However, we decided to simulate additional data in order to plot our time-series component of the dashboard. The notebook of how we simulated the data can be found [here](https://github.com/UBC-MDS/DSCI-532_2024_18_VancouverAirbnbPrices/blob/main/notebooks/data_exploration_time_series.ipynb). Additionally, this lack of data limited out ability to include a play button to demonstrate how the data changed over time, which was included in our original proposal, instead we added the quartly data as additional filters.

We tried to follow the best practices for creating effective visualizations, any deviations from this were non-intentional. We believe that our current dashboard is well functioning (except for the minor issue of displaying the summary stats/map without filter values) and has a nice layout. In addition to the future improvements outlined above, the current limitation of our dashboard is aesthetics. We would like to make it more visually appealing to users in subsequent milestones.