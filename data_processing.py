import pandas as pd 
import geopandas as gpd

cost_of_living = pd.read_csv('./cost_of_living_us.csv')



#cost_of_living['cost_of_living'] = cost_of_living.iloc[:,6:-1].sum(axis=1 )



agg_data = cost_of_living.groupby('county').agg({'case_id': lambda x: x.mode().iloc[0], 
                                                     'state': lambda x: x.mode().iloc[0],
                                                     'areaname': lambda x: x.mode().iloc[0],
                                                     'median_family_income': 'mean', 
                                                     'total_cost': 'mean'
                                                     }).reset_index()

# agg_data['normalized_income'] = (agg_data['median_family_income'] - agg_data['median_family_income'].min()) / (agg_data['median_family_income'].max() - agg_data['median_family_income'].min())
# agg_data['normalized_cost'] = (agg_data['total_cost'] - agg_data['total_cost'].min()) / (agg_data['total_cost'].max() - agg_data['total_cost'].min())

# # Weighting
# income_weight = 0.7
# cost_weight = 0.3

# # Calculate composite index
# agg_data['index'] = income_weight * agg_data['normalized_income'] + cost_weight * agg_data['normalized_cost']

agg_data['index'] = agg_data['median_family_income'] / agg_data['total_cost']
agg_data['index'] = (agg_data['index'] - agg_data['index'].min()) / (agg_data['index'].max() - agg_data['index'].min())


agg_data['county'] = agg_data['county'].str.replace(' County', '', regex=False)


# Load the CSV data

# Assume the CSV file has 'county' and 'index' columns
# You may need to clean or transform the 'county' data to match the GeoJSON properties
agg_data['county'] = agg_data['county'].str.replace(' County', '').str.strip()

# Load the GeoJSON data
geo_data = gpd.read_file('counties.geojson')

# Merge the CSV data with the GeoJSON data
# Ensure that the GeoJSON file has a 'NAME' property that matches the 'county' entries in the CSV
merged_data = geo_data.merge(agg_data, left_on='NAME', right_on='county', how='left')

# Save the merged data back to a new GeoJSON file
merged_data.to_file('merged_county_data.geojson', driver='GeoJSON')



agg_data.to_csv('agg-data.csv', index = True)
