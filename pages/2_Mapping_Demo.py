# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from urllib.error import URLError

import pandas as pd
import pydeck as pdk

import streamlit as st
from streamlit.hello.utils import show_code


def mapping_demo():
    @st.cache_data
    def from_data_file(filename):
        url = (
            "https://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename
        )
        # https://raw.githubusercontent.com/streamlit/example-data/master/hello/v1/bike_rental_stats.json
        return pd.read_json(url)

    data_bike = from_data_file("bike_rental_stats.json");
    data_bike['tooltip'] = data_bike.apply(lambda x: f" Racks: {x['racks']}\n at {x['address']}", axis=1)

    arc_data = from_data_file("bart_path_stats.json");
    arc_data['tooltip'] = arc_data.apply(lambda x: f" {x['lat']} ", axis=1)

    stop_data = from_data_file("bart_stop_stats.json");
    stop_data['tooltip'] = stop_data.apply(lambda x: f" {x['address']} ", axis=1)
    
    #st.dataframe(data_bike[0]);

    try:
        ALL_LAYERS = {
            "Bart Stop Exits": pdk.Layer(
                "ScatterplotLayer",
                data=stop_data,
                get_position=["lon", "lat"],
                get_color=[200, 30, 0, 160],
                get_radius="[exits]",
                radius_scale=0.01,
                pickable=True,
                auto_highlight=True,
            ),
            "Bike Rentals": pdk.Layer(
                "ColumnLayer",
                data=data_bike,
                get_position=["lon", "lat"],
                radius=10,
                #elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
                pickable=True,
                auto_highlight=True,
                get_radius=10,
                radius_scale=2,
                get_elevation="racks",
                elevation_scale=20,
            ),
            "Bart Stop Names": pdk.Layer(
                "TextLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_text="name",
                get_color=[0, 0, 0, 200],
                get_size=10,
                get_alignment_baseline="'bottom'",
            ),
            "Outbound Flow": pdk.Layer(
                "ArcLayer",
                data=arc_data,
                get_source_position=["lon", "lat"],
                get_target_position=["lon2", "lat2"],
                get_source_color=[200, 30, 0, 160],
                get_target_color=[200, 30, 0, 160],
                auto_highlight=True,
                width_scale=0.0001,
                get_width="outbound",
                width_min_pixels=3,
                width_max_pixels=30,
                pickable=True,
            ),
        }
        st.sidebar.markdown("### Map Layers")
        selected_layers = [
            layer
            for layer_name, layer in ALL_LAYERS.items()
                if st.sidebar.checkbox(layer_name, True)
        ]
        if selected_layers:
            st.pydeck_chart(
                pdk.Deck(
                    map_style=None,
                    initial_view_state={
                        "latitude": 37.76,
                        "longitude": -122.4,
                        "zoom": 11,
                        "pitch": 50,
                    },
                    layers=selected_layers,
                    tooltip={"text": "{tooltip}"}
                )
            )
        else:
            st.error("Please choose at least one layer above.")
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )


st.set_page_config(page_title="Mapping Demo", page_icon="🌍")
st.markdown("# Mapping Demo")
st.sidebar.header("Mapping Demo")
st.write(
    """This demo shows how to use
[`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
to display geospatial data."""
)

mapping_demo()

show_code(mapping_demo)
