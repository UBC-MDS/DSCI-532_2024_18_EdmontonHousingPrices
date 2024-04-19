# Milestone 4 Reflection

For milestone 4 we implemented many changes, incorporating feedback from both Joel and the peer reviews. These are outlined below:

1. We implemented a major change of updating the map section of our dashboard, so that the legend is interactable and clicking on a price value also filters the data.

2. We also implemented a major change in making sure the widgets are functional after selection in the map, prior to this once the map was used to select points it created a disconnect from the filtering widgets. We have now solved this issue for increased functionality.

3. We fixed a minor issue of making sure that the selected points on the map remained displayed (previously they disappeared and all points were displayed).

4. We updated the latitude and longitude filters from input values to sliders. This helps users see the range of acceptable values easier. Since we only had data for the Vancouver region, predictions outside of this range were not reliable.

5. We added a notification for when none of the data matches the selected filters. This helps users understand why nothing is being returned.

6. We added a y-axis to the bar charts and changes the title to make them easier to understand.

7. We updated the map legend so that instead of showing 'inf' as the maximum price it shows '$999', which is the maximum price included in our dataset.

In regards to the original dashboard proposal, the only feature we did not implement was the 'email me' section of the prediction page. This task was more complicated than we initially anticipated and was not feasible due to time constraints. This is something that would be nice to add for future improvements. The rest of the proposal was completed as intended.

Additionally, we addressed all functionality issues in this milestone, and our dashboard now performs as expected. Additionally, we did not make an intentional deviations from the best practices for visualizations.

Finally, we believe that our dashboard does a good job of addressing the use case of our target users. We have a variety of ways to display the data (map, summary statistics, time-series, and prediction) to answer the most common questions that airbnb hosts would have. It also has good functionality, which is a benefit as it makes the dashboard easier to use. However, our main limitation is that even with changing our data to a binary format,the addition of cashing, and re-evaluating slow algorithms (filtering), our dashboard is still slow. Unfortunately our data set is large and the platform we used to deploy has limited memory size, which impacts the performance of our dashboard. This is something that would be useful to improve in the future.

We found that the lectures provided a good basis for the structue of the dashboard, especially for our map section. However, we ended up using plotly for our bar graphs since we found this easier to use, so it would have been beneficial to also include instructions on how to use plotly within dash.