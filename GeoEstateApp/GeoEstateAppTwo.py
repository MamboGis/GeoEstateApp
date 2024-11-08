# import streamlit as st
# import leafmap.foliumap as leafmap
# import pandas as pd
# import plotly.express as px
# import matplotlib.pyplot as plt
# from sqlalchemy import create_engine
# from shapely import wkb
# from shapely.ops import transform
# from pyproj import CRS, Transformer
# import folium
# from streamlit_folium import st_folium

# # Set up the database connection
# connection_string = f"postgresql+psycopg2://{'postgres'}:{'39208072'}@{'localhost'}/{'Estate'}"
# engine = create_engine(connection_string)

# # Layout and Sidebar
# st.set_page_config(page_title="Real Estate Business", page_icon="", layout="wide")
# st.sidebar.title("REAL ESTATE BUSINESS")
# logo = "https://cdn.vectorstock.com/i/500p/58/22/geodesic-device-and-wind-rose-vector-14905822.jpg"
# st.sidebar.image(logo)

# st.sidebar.header("Our Services")
# services = """
# - Title Deed and Lease Processing
# - Topographical Surveying
# - Beacons Identification
# - Land Consultancy
# - Area Confirmation
# - Subdivisions
# - Buying and Selling of Land
# """
# st.sidebar.markdown(services)

# # Fetch data from the database
# with engine.connect() as connection:
#     query = "SELECT * FROM diani_complex"
#     df = pd.read_sql(query, connection)

# # Calculate counts for each status
# status_counts = df['status'].value_counts()
# status_labels = ['Sold', 'Bought', 'None']
# status_values = [
#     status_counts.get('sold', 0),
#     status_counts.get('bought', 0),
#     status_counts.get('none', 0)
# ]

# # Display status distribution in a pie chart in the sidebar
# if sum(status_values) > 0:
#     try:
#         # Plotly Pie Chart
#         fig = px.pie(
#             names=status_labels,
#             values=status_values,
#             title="Parcel Status Distribution"
#         )
#         st.sidebar.plotly_chart(fig)
#     except Exception as e:
#         st.write("Plotly encountered an issue:", e)
        
#     # Fallback - Matplotlib Pie Chart
#     fig, ax = plt.subplots()
#     ax.pie(status_values, labels=status_labels, autopct='%1.1f%%', startangle=90)
#     ax.set_title("Parcel Status Distribution")
#     st.sidebar.pyplot(fig)

# # Dropdown for LA PID selection
# la_pid_list = ["All"] + df['la_pid'].astype(str).unique().tolist()
# selected_la_pid = st.selectbox('Select a Property by LA PID', options=la_pid_list)

# # Filter data and display map based on selected status and LA PID
# status_filter = st.sidebar.selectbox("Select Status", ["All", "SOLD", "BOUGHT", "None"])
# filtered_df = df if status_filter == "All" else df[df['status'].str.lower() == status_filter.lower()]

# # Filter based on selected LA PID if specified
# if selected_la_pid != "All":
#     filtered_df = filtered_df[filtered_df['la_pid'].astype(str) == selected_la_pid]

# # Display results
# if filtered_df.empty:
#     st.write("No data found for the selected filters.")
# else:
#     st.write(f"Data for status '{status_filter}' and selected LA PID '{selected_la_pid}':")
#     st.write(filtered_df)

#     # Initialize map
#     m = leafmap.Map(minimap_control=True, center=[-4, 39], zoom=9)
#     m.add_basemap("HYBRID")

#     # Plot parcels on map
#     for _, row in filtered_df.iterrows():
#         geom = row['geom']
#         polygon = wkb.loads(geom, hex=True)

#         # Reproject geometry to WGS84
#         src_crs = CRS.from_epsg(21037)
#         dst_crs = CRS.from_epsg(4326)
#         transformer = Transformer.from_crs(src_crs, dst_crs, always_xy=True)
#         reprojected_polygon = transform(transformer.transform, polygon)

#         # Get the color based on status
#         if row['status'] == 'SOLD':
#             color = 'green'
#         elif row['status'] == 'BOUGHT':
#             color = 'red'
#         else:  # For 'none'
#             color = 'blue'

#         # Add the polygon to the map with the appropriate color
#         folium.GeoJson(
#             data=reprojected_polygon.__geo_interface__,
#             name=f"Plot - LA PID: {row['la_pid']}",
#             tooltip=f"LA PID: {row['la_pid']}\nStatus: {row['status']}",
#             style_function=lambda x, color=color: {"color": color, "weight": 2, "fillOpacity": 0.3},
#         ).add_to(m)

#     # Display map
#     st_folium(m, height=500, width=1200)

# import streamlit as st
# import leafmap.foliumap as leafmap
# from sqlalchemy import create_engine
# from shapely import wkb
# from shapely.ops import transform
# from pyproj import CRS, Transformer
# import folium
# from streamlit_folium import st_folium
# import pandas as pd

# # Set up the database connection
# connection_string = f"postgresql+psycopg2://{'postgres'}:{'39208072'}@{'localhost'}/{'Estate'}"
# engine = create_engine(connection_string)

# # Page layout setup
# st.set_page_config(page_title="Real Estate Business", page_icon="", layout="wide")

# # Fetch data from the database
# with engine.connect() as connection:
#     query = "SELECT * FROM diani_complex"
#     df = pd.read_sql(query, connection)

# # Dropdown for LA PID selection
# la_pid_list = ["All"] + df['la_pid'].astype(str).unique().tolist()
# selected_la_pid = st.selectbox('Select a Property by LA PID', options=la_pid_list)

# # Filter data based on selected LA PID
# filtered_df = df if selected_la_pid == "All" else df[df['la_pid'].astype(str) == selected_la_pid]

# # Display map only
# if filtered_df.empty:
#     st.write("No data found for the selected LA PID.")
# else:
#     # Initialize map
#     m = leafmap.Map(minimap_control=True, center=[-4, 39], zoom=9)
#     m.add_basemap("HYBRID")

#     # Plot parcels on map
#     for _, row in filtered_df.iterrows():
#         geom = row['geom']
#         polygon = wkb.loads(geom, hex=True)

#         # Reproject geometry to WGS84
#         src_crs = CRS.from_epsg(21037)
#         dst_crs = CRS.from_epsg(4326)
#         transformer = Transformer.from_crs(src_crs, dst_crs, always_xy=True)
#         reprojected_polygon = transform(transformer.transform, polygon)

#         # Get the color based on status
#         if row['status'] == 'SOLD':
#             color = 'green'
#         elif row['status'] == 'BOUGHT':
#             color = 'red'
#         else:  # For 'none'
#             color = 'blue'

#         # Add the polygon to the map with the appropriate color
#         folium.GeoJson(
#             data=reprojected_polygon.__geo_interface__,
#             name=f"Plot - LA PID: {row['la_pid']}",
#             tooltip=f"LA PID: {row['la_pid']}\nStatus: {row['status']}",
#             style_function=lambda x, color=color: {"color": color, "weight": 2, "fillOpacity": 0.3},
#         ).add_to(m)

#     # Display map
#     st_folium(m, height=500, width=1200)


import streamlit as st
import leafmap.foliumap as leafmap
from sqlalchemy import create_engine
from shapely import wkb
from shapely.ops import transform
from pyproj import CRS, Transformer
import folium
from streamlit_folium import st_folium
import pandas as pd

# Set up the database connection
connection_string = f"postgresql+psycopg2://{'postgres'}:{'39208072'}@{'localhost'}/{'Estate'}"
engine = create_engine(connection_string)

# Page layout setup
st.set_page_config(page_title="Real Estate Business", page_icon="", layout="wide")

# Fetch data from the database
with engine.connect() as connection:
    query = "SELECT * FROM diani_complex"
    df = pd.read_sql(query, connection)

# Dropdown for LA PID selection
la_pid_list = ["All"] + df['la_pid'].astype(str).unique().tolist()
selected_la_pid = st.selectbox('Select a Property by LA PID', options=la_pid_list)

# Filter data based on selected LA PID
filtered_df = df if selected_la_pid == "All" else df[df['la_pid'].astype(str) == selected_la_pid]

# Define default map center and zoom level
map_center = [-4, 39]
zoom_level = 9

# Set up a transformer for reprojecting geometries from EPSG:21037 to EPSG:4326
src_crs = CRS.from_epsg(21037)
dst_crs = CRS.from_epsg(4326)
transformer = Transformer.from_crs(src_crs, dst_crs, always_xy=True)

# Adjust map center and zoom if a specific property is selected
if selected_la_pid != "All" and not filtered_df.empty:
    # Get the geometry for the selected property
    geom = filtered_df.iloc[0]['geom']
    polygon = wkb.loads(geom, hex=True)

    # Reproject geometry to WGS84 for accurate center calculation
    reprojected_polygon = transform(transformer.transform, polygon)

    # Calculate the center of the polygon
    map_center = [reprojected_polygon.centroid.y, reprojected_polygon.centroid.x]
    zoom_level = 14  # Set a closer zoom level for the selected property

# Initialize map with dynamic center and zoom
m = leafmap.Map(minimap_control=True, center=map_center, zoom=zoom_level)
m.add_basemap("HYBRID")

# Plot parcels on map
for _, row in filtered_df.iterrows():
    geom = row['geom']
    polygon = wkb.loads(geom, hex=True)

    # Reproject geometry to WGS84
    reprojected_polygon = transform(transformer.transform, polygon)

    # Get the color based on status
    if row['status'] == 'SOLD':
        color = 'green'
    elif row['status'] == 'BOUGHT':
        color = 'red'
    else:  # For 'none'
        color = 'blue'

    # Add the polygon to the map with the appropriate color
    folium.GeoJson(
        data=reprojected_polygon.__geo_interface__,
        name=f"Plot - LA PID: {row['la_pid']}",
        tooltip=f"LA PID: {row['la_pid']}\nStatus: {row['status']}",
        style_function=lambda x, color=color: {"color": color, "weight": 2, "fillOpacity": 0.3},
    ).add_to(m)

# Display map
st_folium(m, height=500, width=1500)
