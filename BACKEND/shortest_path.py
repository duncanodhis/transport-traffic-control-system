#%%
!pip3 install geopandas tqdm osmnx
# %%
import osmnx as ox
origin_address = "jersey City, NJ"
G = ox.graph_from_place(origin_address, network_type='drive')
# %%
ox.plot_graph(G, bgcolor="w", node_color="r", edge_color="#aaa", figsize=(12,12))

# %%
print("node count:", len(G.nodes()))
print("edge count:", len(G.edges()))
# %%
station_st_node_id = ox.nearest_nodes(G, [40.729000], [-74.034920])[0]
station_st_node_id
# %%

# %%
# station nodes 
G.nodes.get(station_st_node_id)
# %%
list(G.neighbors(station_st_node_id))
# %%
import json

# show edge attributes
for edge in G.out_edges(station_st_node_id, data=True):
    print("\n=== Edge ====")
    print("Source and target node ID:", edge[:2])
    edge_attributes = edge[2]
    # remove geometry object from output
    edge_attributes_wo_geometry = {i:edge_attributes[i] for i in edge_attributes if i!='geometry'}
    print("Edge attributes:", json.dumps(edge_attributes_wo_geometry, indent=4))

# %%
import geopandas as gpd
import networkx as nx

# impute edge (driving) speeds and calculate edge traversal times
G = ox.add_edge_speeds(G)
G = ox.add_edge_travel_times(G)

# convert string address into geographical coordinates
def geocode_address(address, crs=4326):
    geocode = gpd.tools.geocode(address, provider='nominatim', 
                user_agent="drive time demo").to_crs(crs)
    return (geocode.iloc[0].geometry.y, geocode.iloc[0].geometry.x)

# get origin and destination coordinates
origin_point = geocode_address("30 River ct, Jersey City")
destination_point = geocode_address("575 Washington Blvd, jersey  City")

# get closes graph nodes to origin and destination
orig_node = ox.distance.nearest_nodes(G, origin_point[1], origin_point[0])
destination_node = ox.distance.nearest_nodes(G, 
    destination_point[1], destination_point[0])

# find shortest path based on travel time
route = nx.shortest_path(G, orig_node, destination_node, weight='travel_time')

fig, ax = ox.plot_graph_route(G, route, node_size=0, figsize=(40,40))
# %%
route
# %%
