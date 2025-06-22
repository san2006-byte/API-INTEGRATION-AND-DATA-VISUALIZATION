# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME* : SANDHYA M

*INTERN ID*: CT04DG1363

*DOMAIN*: PYTHON PROGRAMMING 

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

   In order to complete this task, I used Python to integrate a public API and convert the raw data into an understandable, clear visual format. The objective was to connect the dots between data collection, processing, and visualization-based storytelling, not merely to create a chart.
   The OpenWeatherMap 5-day/3-hour forecast API, which provides comprehensive weather forecasts in brief time intervals, is what I chose to use. It is ideal for integrating into a Python script because it is dependable, freely available, and returns data in JSON format. I decided to concentrate on Chennai because the task was flexible in terms of the data I could visualise. This decision was made for the straightforward reason that I was interested in seeing how the city's temperature changed over a few days.
   I was able to access a number of parameters, including temperature, humidity, wind speed, and more, after retrieving the Chennai weather data via an API call. For this task, I chose to use the temperature data. For five days, the API gave me this information at 3-hour intervals, which gave me enough detail to make an engaging line chart.   
   I organised the data into a structured DataFrame using pandas after retrieving it using the requests library. I then used matplotlib to plot the timestamps and the associated temperature values that I had extracted. It is simple to observe trends, peaks, and cooler times thanks to the line graph I made that illustrates Chennai's temperature variations over various days and times. In order to make the chart readable even at a glance, I also added labels, a title, and changed the layout.
   This chart tells a story and wasn't created purely for show. The daytime and nighttime temperature variations, as well as the recurring patterns over time, are readily apparent. I saved the finished image as dashboard.png so that it could be used in a weather dashboard, shared, or included in reports.

This assignment taught me a number of valuable lessons in addition to writing a script and creating a graph:
  How to use real-world APIs, such as parsing JSON responses, formatting requests, and reading API documentation

  How to clean up and turn data into something useful, particularly when the raw API response is nested or fairly large

  The significance of selecting the appropriate visualisation type according to the data type (in this case, a line chart for time series)

  Additionally, how to professionally save output files for presentations or documentation

Research projects, dashboards, analytics tools, and weather apps all use this type of API integration and visualisation. I gained a practical understanding of how data moves from the internet, through Python, and into a chart that aids in understanding by doing it myself.

In conclusion, this assignment assisted me in bridging the communication and coding divide. It forced me to not only gather information but also to accurately, readable, and perceptively present it. I now feel more comfortable using Python's APIs and data visualisation tools, which are critical abilities for any developer, data analyst, or engineer in the tech-driven world of today.

*OUTPUT*: ![Image](https://github.com/user-attachments/assets/432824e6-0a8e-4656-a986-7490fabc929e)
