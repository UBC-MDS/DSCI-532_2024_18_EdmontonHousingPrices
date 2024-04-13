## Milestone 3 reflection

In this milestone we made numerous improvements to the dashboard, both addressing feedback from Joel and adding additional improvements we had identified during milestone 2. Changes made to the dashboard this week include:

1. Switching the order of the map and dataframe tabs on our observation page. This makes the dashboard more visually interesting.

2. Updating the map so that the colour of each data point reflects the binned price per night of the rental, which allows for easier comparison of properties. When discussing with Joel, our original plan was to colour the data points by neighbourhood, but upon further reflection we decided that colouring by price provided more information to users.

3. Implementing a selection feature from the map. When a neighbourhood is selected on the map it updates the summary statistics and time-series plot to reflect only the data points in that region. However, we noticed that there is a small error in this functionality, where the map does not keep displaying the selected region after the summary stats and time-series are updated. This is something we would like to address in milestone 4.

4. Fixing the margins on the map and added more information to the tooltip function, this improves the aesthetics and useability of our dashboard.

5. Updating the summary statistics. This included changing the layout of the cards, adding colours and increasing the font size. We also added in a selection to display both the mean and median values, as well as created another tab to displayed bar charts of the categorical variables. This provides more information to users.

6. Fixing the issue of the map and summary statistics not displaying with default values, which improves the aesthetics of the dashboard.

7. Changing the filtering of the neighbourhood value to allow for multiple selections, improving useability.

8. Changing the layout of the prediction tab to display the selected values and create a point on the map corresponding to the given longitude and latitude values, this makes the prediction tab more visually interesting.

9. Spliting the code into multiple files to modularize our code.

We completed most of the updates identified during milestone 2 and our discussion with Joel. The only improvement we did not include was colouring by neighbourhood, as we decided that colouring by price was more useful to users. We believe that our dashboard is now functional and visually interesting, meeting the goals of our intended use case. One limitation of our dashboard is that we still have not recieved additional data from Airbnb and continue to use simulated data to display the intended purpose of the time-series plot. Aside from fixing the display of the map selection, we will add future improvements based on feedback from the peer reviews.