# Convert Cities CSV Into HTML 
import pandas as pd 

# Read in csv file
i = pd.read_csv("cities.csv")

# Save Cities CSV to Cites HTML
i.to_html('cities.html')