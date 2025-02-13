import pandas as pd
import numpy as np
import folium
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xlogit

def visualize_modal_share(df):
    """
    Visualizes the modal share distribution as a pie chart.

    Parameters:
        df (pd.DataFrame): source survey data
    """
    
    # Define the figure size and title
    plt.figure(figsize=(10, 8))
    plt.title('Modal Share (%)', fontsize=20)

    # Map numeric choices to transport mode names
    mode_mapping = {1: 'auto', 2: 'taxi', 3: 'bus', 4: 'subway', 5: 'integmode'}
    mode_counts = df['choice'].map(mode_mapping).value_counts()

    # Plot the pie chart with percentage labels
    mode_counts.plot.pie(
        autopct='%.2f%%',
        textprops={'fontsize': 12, 'weight': 'bold'}
    )

    # Show the plot
    plt.show()

def visualize_feature_correlation(df):
    """
    Visualizes the correlation matrix of selected features using a heatmap.

    Parameters:
        df (DataFrame): source survey data
    """

    # Assign unique ID to each observation
    df['id'] = np.arange(len(df))

    # Convert data from wide format to long format for choice modeling
    df = xlogit.utils.wide_to_long(
        df, id_col='id', alt_name='alt', sep='_',
        alt_list=['auto', 'taxi', 'bus', 'subway', 'integmode'], empty_val=0,
        varying=['dist', 'totaltime', 'invehicletime', 'outvehicletime', 'totalcost', 'trans']
    )

    # Map choice values to mode names
    df['choice'] = df['choice'].map({1: 'auto', 2: 'taxi', 3: 'bus', 4: 'subway', 5: 'integmode'})

    # Keep only rows where the chosen mode matches the alternative mode
    df = df[df['choice'] == df['alt']]

    # Convert mode names back to numerical values
    df['choice'] = df['choice'].map({'auto': 1, 'taxi': 2, 'bus': 3, 'subway': 4, 'integmode': 5})

    # Select relevant features for correlation analysis
    selected_features = ['dist', 'totaltime', 'invehicletime', 'outvehicletime', 
                         'totalcost', 'trans', 'admin', 'station']
    
    # Compute the correlation matrix
    corr_matrix = df[selected_features].astype(float).corr()

    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    plt.title('Correlation of Features', y=1.05, size=15)
    sns.heatmap(
        corr_matrix, linewidths=0.1, vmax=1.0, square=True, cmap='RdYlGn',
        linecolor='white', annot=True, annot_kws={'size': 16}
    )
    plt.show()

def visualize_taz(dong_csv_path, layer_json_paths, output_html, center_lat=37.4729081, center_lon=127.039306, zoom=11):
    """
    Visualizes administrative districts as Traffic Analysis Zones (TAZ) in the Seoul metropolitan area.

    Parameters:
        dong_csv_path (str): Path to the CSV file containing location data.
        layer_json_paths (dict): Dictionary with region names as keys and GeoJSON file paths as values.
        output_html (str): Path to save the generated HTML file.
        center_lat (float, optional): Latitude of the map's center. Default is 37.4729081.
        center_lon (float, optional): Longitude of the map's center. Default is 127.039306.
        zoom (int, optional): Initial zoom level of the map. Default is 11.

    Example:
        json_files = {
            "Seoul": "data/Layer_Seoul_EPSG4326.json",
            "Gyeonggi": "data/Layer_Gyeonggi_EPSG4326.json",
            "Incheon": "data/Layer_Incheon_EPSG4326.json"
        }

        visualize_taz('data/DongOffice.csv', json_files, 'figures/visualization_of_traffic_analysis_zone.html')
    """

    # Load location data from CSV (Coordinate system: WGS84)
    df = pd.read_csv(dong_csv_path, dtype=str)

    # Create a folium map centered at the given coordinates
    taz_map = folium.Map(location=[center_lat, center_lon], zoom_start=zoom)

    # Define the exterior style for GeoJSON layers
    exterior_style = {
        "color": "black",
        "weight": 1.5,
        "fillOpacity": 0,
    }

    # Load and add GeoJSON layers for each region
    for region, json_path in layer_json_paths.items():
        with open(json_path, encoding='utf-8-sig') as f:
            geojson_data = json.load(f)
        folium.GeoJson(geojson_data, style_function=lambda _: exterior_style).add_to(taz_map)

    # Add markers for each location
    for _, row in df.iterrows():
        folium.Marker(location=(row['Lat'], row['Lon']), popup=row['Dong']).add_to(taz_map)

    # Save the map as an HTML file
    taz_map.save(output_html)