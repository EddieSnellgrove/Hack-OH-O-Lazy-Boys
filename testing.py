import geopandas as gpd

file_path = r"C:\Users\bobth\Downloads\Data1\arcos_prod_damage_09_28_Clip.shp"
gdf = gpd.read_file(file_path)

# 1. Safely calculate the middle coordinates (handles lines or points automatically)
centroids = gdf.geometry.centroid
gdf['latitude_calc'] = centroids.y
gdf['longitude_calc'] = centroids.x

# 2. Print out ALL column names for this specific dataset
print("--- New Dataset Column Names ---")
columns = list(gdf.columns)
for i in range(0, len(columns), 3):
    print(", ".join(columns[i:i+3]))
print("--------------------------------")

time_column = 'Report_Tim' 

if time_column in gdf.columns:
    # Filter down to only what you care about
    outage_data = gdf[[time_column, 'latitude_calc', 'longitude_calc', ]].copy()
    outage_data.columns = ['report_time', 'latitude', 'longitude']
    
    # Clean up dates and drop missing rows
    outage_data['report_time'] = gpd.pd.to_datetime(outage_data['report_time'])
    outage_data = outage_data.dropna().reset_index(drop=True)
    
    print("\n--- Cleaned Data Preview ---")
    print(outage_data.head())
    outage_data.to_string(r"C:\Users\bobth\Hackathon\cleaned_outages.txt", index=False)
else:
    print(f"\n[!] '{time_column}' is not a column in this new file.")
    print("Look at the column names printed above, find the time or date column, and update time_column in the script.")
