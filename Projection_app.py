import streamlit as st
from pyproj import Transformer

# PAGE CONFIGURATION

st.set_page_config(
    page_title="Ghana Projection Tool",
    page_icon="🌍",
    layout="centered"
)

# TITLE

st.title("🌍 Ghana Projection & Transformation Tool")

st.markdown("""
This application performs coordinate transformations between:

- Ghana National Grid
- Ghana Metre Grid
- WGS 84
""")

# EPSG DEFINITIONS

WGS84 = "EPSG:4326"
GHANA_NATIONAL_GRID = "EPSG:2136"
GHANA_METRE_GRID = "EPSG:25000"

# ---------------------------------------------------
# TRANSFORMATION OPTIONS
# ---------------------------------------------------

transformation = st.selectbox(
    "Select Coordinate Transformation",
    (
        "Ghana National Grid → Ghana Metre Grid",
        "Ghana Metre Grid → Ghana National Grid",
        "WGS84 → Ghana National Grid",
        "WGS84 → Ghana Metre Grid"
    )
)

# ---------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------

st.subheader("Enter Coordinates")

col1, col2 = st.columns(2)

with col1:
    x = st.number_input(
        "Easting / Longitude",
        format="%.6f"
    )

with col2:
    y = st.number_input(
        "Northing / Latitude",
        format="%.6f"
    )

# ---------------------------------------------------
# CONVERT BUTTON
# ---------------------------------------------------

if st.button("Convert Coordinates"):

    try:

        # ---------------------------------------------------
        # TRANSFORMATIONS
        # ---------------------------------------------------

        if transformation == "Ghana National Grid → Ghana Metre Grid":

            transformer = Transformer.from_crs(
                GHANA_NATIONAL_GRID,
                GHANA_METRE_GRID,
                always_xy=True
            )

            result_x, result_y = transformer.transform(x, y)

            st.success("Transformation Successful")

            st.write("### Converted Coordinates")
            st.write(f"**Easting:** {result_x:.3f} m")
            st.write(f"**Northing:** {result_y:.3f} m")

        elif transformation == "Ghana Metre Grid → Ghana National Grid":

            transformer = Transformer.from_crs(
                GHANA_METRE_GRID,
                GHANA_NATIONAL_GRID,
                always_xy=True
            )

            result_x, result_y = transformer.transform(x, y)

            st.success("Transformation Successful")

            st.write("### Converted Coordinates")
            st.write(f"**Easting:** {result_x:.3f}")
            st.write(f"**Northing:** {result_y:.3f}")

        elif transformation == "WGS84 → Ghana National Grid":

            transformer = Transformer.from_crs(
                WGS84,
                GHANA_NATIONAL_GRID,
                always_xy=True
            )

            result_x, result_y = transformer.transform(x, y)

            st.success("Transformation Successful")

            st.write("### Converted Coordinates")
            st.write(f"**Easting:** {result_x:.3f}")
            st.write(f"**Northing:** {result_y:.3f}")

        elif transformation == "WGS84 → Ghana Metre Grid":

            transformer = Transformer.from_crs(
                WGS84,
                GHANA_METRE_GRID,
                always_xy=True
            )

            result_x, result_y = transformer.transform(x, y)

            st.success("Transformation Successful")

            st.write("### Converted Coordinates")
            st.write(f"**Easting:** {result_x:.3f} m")
            st.write(f"**Northing:** {result_y:.3f} m")

    except Exception as e:
        st.error(f"Error: {e}")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
    <style>
    .footer {
        position:flex;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: yellow;
        padding: 10px;
        font-size: 20px;
        weight: bold;
    }
    </style>

    <div class="footer">
        Developed By: Abdul-Nasir Iddrisu
    </div>
""", unsafe_allow_html=True)