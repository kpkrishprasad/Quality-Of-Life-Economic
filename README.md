# Quality-Of-Life-Economic
Infographic of the US Quality of life based on median income and cost of living


In this project, I set out to create an interactive and detailed map visualization to depict the quality of life across U.S. counties, informed by a Cost-Income Index. My design choices aimed to present complex geographic and demographic data in a way that was both clear and visually engaging.

I opted for a choropleth map with visual encodings that used a blue color scale in varying intensities to represent the range of data values. This scale was chosen because it intuitively shows the spectrum from lower to higher values of the Quality of Life Cost-Income Index, transitioning from light to dark blue. This particular color choice was preferable over diverging or qualitative color schemes because it provides a straightforward gradient that enhances readability and quick comprehension by viewers. The use of a sequential color scheme also avoids the potential confusion that can come from more complex color mappings.

The interactivity features of the map include a zoom function that allows users to focus in on specific areas for more detailed examination, and interactive tooltips that appear when hovering over a county. These tooltips display precise data such as the county name and its specific index value, providing immediate and relevant information without cluttering the visual space. I chose this interaction model over static labels to maintain a clean map aesthetic and to ensure the interface remained user-friendly.

The development process involved data preparation and processing with Python scripts, integration of geographic data, and the careful design and implementation of the visualization using D3.js. Aligning the data accurately with the geographic outlines was particularly challenging, needing multiple iterations to refine the map projections and scale. Another  portion of the project was dedicated to crafting and fine-tuning the interactive elements of the map to ensure it was intuitive for users, allowing them to engage  with the visualization while exploring the data effectively.
