import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import plotly.express as px
import warnings
import plotly.graph_objects as go
from PIL import Image



pd.set_option('display.max_columns', None)
warnings.filterwarnings("ignore")
def read_data(filename):
    df = pd.read_csv(filename)
    return df
def home_page():
    st.markdown(
        """
        <style>
            .big-font {
                font-size: 24px;
                font-weight: bold;
                color: #2f4f4f;
            }
            .info-box {
                background-color: #f0f8ff;
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
            }
            .marquee {
                color: #4682b4;
                font-size: 18px;
                white-space: nowrap;
                overflow: hidden;
                border: 1px solid #b0c4de;
                padding: 10px;
                border-radius: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    

    st.markdown("<p class='big-font'>Exploring Airbnb Trends and Insights</p>", unsafe_allow_html=True)
    
    st.markdown("""
        <div class='info-box'>
            <p><strong>About Airbnb:</strong></p>
            <p>Airbnb is a leading platform for short-term rental accommodations. It connects travelers with unique lodging options around the world, offering a diverse range of homes, apartments, and experiences.</p>
            <p><strong>Uses of Airbnb:</strong></p>
            <ul>
                <li>Discovering Unique Accommodations</li>
                <li>Exploring Local Experiences</li>
                <li>Connecting Hosts and Guests</li>
            </ul>
            <p>Explore Airbnb Insights to understand market trends, traveler preferences, and the impact of short-term rentals on the hospitality industry.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("""
        Airbnb Insights is a comprehensive project designed to offer valuable insights into short-term rental accommodations and travel trends.
        Dive into the data to gain valuable information about property listings, guest preferences, and much more.
    """)
    
def price_analysis(df):
    with st.expander("PRICE ANALYSIS"):
        st.title("**PRICE ANALYSIS**")
        col1,col2= st.columns(2)

        with col1:
            
            
            country= st.selectbox("Select the Country",df["country"].unique())

            df1= df[df["country"] == country]
            df1.reset_index(drop= True, inplace= True)

            room_ty= st.selectbox("Select the Room Type",df1["room_type"].unique())
            
            df2= df1[df1["room_type"] == room_ty]
            df2.reset_index(drop= True, inplace= True)

            df_bar= pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
            df_bar.reset_index(inplace= True)

            fig_bar= px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY_TYPES",hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
            st.plotly_chart(fig_bar)

        
        with col2:
            
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
     
            proper_ty= st.selectbox("Select the Property_type",df2["property_type"].unique())

            df4= df2[df2["property_type"] == proper_ty]
            df4.reset_index(drop= True, inplace= True)

            df_pie= pd.DataFrame(df4.groupby("host_response_time")[["price","bedrooms"]].sum())
            df_pie.reset_index(inplace= True)

            fig_pi= px.pie(df_pie, values="price", names= "host_response_time",
                            hover_data=["bedrooms"],
                            color_discrete_sequence=px.colors.sequential.BuPu_r,
                            title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                            width= 600, height= 500)
            st.plotly_chart(fig_pi)

        col1,col2= st.columns(2)

        with col1:

            
            hostresponsetime= st.selectbox("Select the host_response_time",df4["host_response_time"].unique())

            df5= df4[df4["host_response_time"] == hostresponsetime]

            df_do_bar= pd.DataFrame(df5.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
            df_do_bar.reset_index(inplace= True)

            fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
            title='MINIMUM NIGHTS AND MAXIMUM NIGHTS',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow, width=600, height=500)
            

            st.plotly_chart(fig_do_bar)

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

            df_do_bar_2= pd.DataFrame(df5.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
            df_do_bar_2.reset_index(inplace= True)

            fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
            title='BEDROOMS AND BEDS ACCOMMODATES',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r, width= 600, height= 500)
           
            st.plotly_chart(fig_do_bar_2)

def availability_analysis(df):
    with st.expander("AVAILABILITY ANALYSIS"):
        st.title("**AVAILABILITY ANALYSIS**")
        def datafr():
            df_a= pd.read_csv("Airbnb_data.csv")
            return df_a

        df_a= datafr()

        col1,col2= st.columns(2)

        country_a= st.selectbox("Select the Country_a",df_a["country"].unique())

        df1_a= df[df["country"] == country_a]
        df1_a.reset_index(drop= True, inplace= True)

        property_ty_a= st.selectbox("Select the Property Type",df1_a["property_type"].unique())

        df2_a= df1_a[df1_a["property_type"] == property_ty_a]
        df2_a.reset_index(drop= True, inplace= True)

        roomtype_a= st.selectbox("Select the Room Type_a", df2_a["room_type"].unique())

        df3_a= df2_a[df2_a["room_type"] == roomtype_a]

        df_a_sunb_30= px.sunburst(df3_a, path=["room_type","bed_type","is_location_exact"], values="availability_30",width=600,height=500,title="Availability_30",color_discrete_sequence=px.colors.sequential.Peach_r)
        st.plotly_chart(df_a_sunb_30)

        df_a_sunb_60= px.sunburst(df3_a, path=["room_type","bed_type","is_location_exact"], values="availability_60",width=600,height=500,title="Availability_60",color_discrete_sequence=px.colors.sequential.Blues_r)
        st.plotly_chart(df_a_sunb_60)

        df_a_sunb_90= px.sunburst(df3_a, path=["room_type","bed_type","is_location_exact"], values="availability_90",width=600,height=500,title="Availability_90",color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
        st.plotly_chart(df_a_sunb_90)

        df_a_sunb_365= px.sunburst(df3_a, path=["room_type","bed_type","is_location_exact"], values="availability_365",width=600,height=500,title="Availability_365",color_discrete_sequence=px.colors.sequential.Greens_r)
        st.plotly_chart(df_a_sunb_365)

        df_mul_bar_a= pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].sum())
        df_mul_bar_a.reset_index(inplace= True)

        fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
        title='AVAILABILITY BASED ON HOST RESPONSE TIME',hover_data="price",
        barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)

        st.plotly_chart(fig_df_mul_bar_a)


def location_analysis(df):
    with st.expander("LOCATION ANALYSIS"):
        st.title("LOCATION ANALYSIS")
        st.write("")

        def datafr():
            df = pd.read_csv("Airbnb_data.csv")
            return df

        df_l = datafr()

        country_l = st.selectbox("Select the Country_l", df_l["country"].unique())

        df1_l = df_l[df_l["country"] == country_l]
        df1_l.reset_index(drop=True, inplace=True)

        proper_ty_l = st.selectbox("Select the Property_type_l", df1_l["property_type"].unique())

        df2_l = df1_l[df1_l["property_type"] == proper_ty_l]
        df2_l.reset_index(drop=True, inplace=True)

        st.write("")

        def select_the_df(sel_val):
            if sel_val == str(df2_l['price'].min()) + ' ' + str('to') + ' ' + str(
                    differ_max_min * 0.30 + df2_l['price'].min()) + ' ' + str("(30% of the Value)"):
                df_val_30 = df2_l[df2_l["price"] <= differ_max_min * 0.30 + df2_l['price'].min()]
                df_val_30.reset_index(drop=True, inplace=True)
                return df_val_30
            elif sel_val == str(differ_max_min * 0.30 + df2_l['price'].min()) + ' ' + str('to') + ' ' + str(
                    differ_max_min * 0.60 + df2_l['price'].min()) + ' ' + str("(30% to 60% of the Value)"):
                df_val_60 = df2_l[df2_l["price"] >= differ_max_min * 0.30 + df2_l['price'].min()]
                df_val_60_1 = df_val_60[df_val_60["price"] <= differ_max_min * 0.60 + df2_l['price'].min()]
                df_val_60_1.reset_index(drop=True, inplace=True)
                return df_val_60_1
            elif sel_val == str(
                    differ_max_min * 0.60 + df2_l['price'].min()) + ' ' + str('to') + ' ' + str(
                    df2_l['price'].max()) + ' ' + str("(60% to 100% of the Value)"):
                df_val_100 = df2_l[df2_l["price"] >= differ_max_min * 0.60 + df2_l['price'].min()]
                df_val_100.reset_index(drop=True, inplace=True)
                return df_val_100

        differ_max_min = df2_l['price'].max() - df2_l['price'].min()

        submit_button = st.button("Submit")

        if submit_button:
            val_sel = st.radio("Select the Price Range",
                               [str(df2_l['price'].min()) + ' ' + str('to') + ' ' + str(
                                   differ_max_min * 0.30 + df2_l['price'].min()) + ' ' + str("(30% of the Value)"),
                                str(differ_max_min * 0.30 + df2_l['price'].min()) + ' ' + str('to') + ' ' + str(
                                    differ_max_min * 0.60 + df2_l['price'].min()) + ' ' + str(
                                    "(30% to 60% of the Value)"),
                                str(differ_max_min * 0.60 + df2_l['price'].min()) + ' ' + str('to') + ' ' + str(
                                    df2_l['price'].max()) + ' ' + str("(60% to 100% of the Value)")])

            df_val_sel = select_the_df(val_sel)

            st.dataframe(df_val_sel)

            df_val_sel_corr = df_val_sel.drop(columns=["listing_url", "name", "property_type",
                                                       "room_type", "bed_type", "cancellation_policy",
                                                       "images", "host_url", "host_name", "host_location",
                                                       "host_response_time", "host_thumbnail_url",
                                                       "host_response_rate", "host_is_superhost",
                                                       "host_has_profile_pic",
                                                       "host_picture_url", "host_neighbourhood",
                                                       "host_identity_verified", "host_verifications",
                                                       "street", "suburb", "government_area", "market",
                                                       "country", "country_code", "location_type",
                                                       "is_location_exact",
                                                       "amenities"]).corr()

            st.dataframe(df_val_sel_corr)

            df_val_sel_gr = pd.DataFrame(
                df_val_sel.groupby("accommodates")[["cleaning_fee", "bedrooms", "beds", "extra_people"]].sum())
            df_val_sel_gr.reset_index(inplace=True)

            fig_1 = px.bar(df_val_sel_gr, x="accommodates", y=["cleaning_fee", "bedrooms", "beds"], title="ACCOMMODATES",
                           hover_data="extra_people", barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,
                           width=1000)
            st.plotly_chart(fig_1)

            room_ty_l = st.selectbox("Select the Room_Type_l", df_val_sel["room_type"].unique())

            df_val_sel_rt = df_val_sel[df_val_sel["room_type"] == room_ty_l]

            fig_2 = px.bar(df_val_sel_rt, x=["street", "host_location", "host_neighbourhood"], y="market", title="MARKET",
                           hover_data=["name", "host_name", "market"], barmode='group', orientation='h',
                           color_discrete_sequence=px.colors.sequential.Rainbow_r, width=1000)
            st.plotly_chart(fig_2)

            fig_3 = px.bar(df_val_sel_rt, x="government_area",
                           y=["host_is_superhost", "host_neighbourhood", "cancellation_policy"], title="GOVERNMENT_AREA",
                           hover_data=["guests_included", "location_type"], barmode='group',
                           color_discrete_sequence=px.colors.sequential.Rainbow_r, width=1000)
            st.plotly_chart(fig_3)




def geospatial_analysis(df):
    with st.expander("GEOSPATIAL VISUALIZATION"):
        st.title("GEOSPATIAL VISUALIZATION")
        st.write("")

        fig_4 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', size='accommodates',
                        color_continuous_scale= "rainbow",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                        zoom=1)
        fig_4.update_layout(width=1150,height=800,title='Geospatial Distribution of Listings')
        st.plotly_chart(fig_4) 

def topcharts_analysis(df):
    with st.expander("TOP CHARTS ANALYSIS"):
        st.title("TOP CHARTS ANALYSIS")

        country_t= st.selectbox("Select the Country_t",df["country"].unique())

        df1_t= df[df["country"] == country_t]

        property_ty_t= st.selectbox("Select the Property_type_t",df1_t["property_type"].unique())

        df2_t= df1_t[df1_t["property_type"] == property_ty_t]
        df2_t.reset_index(drop= True, inplace= True)

        df2_t_sorted= df2_t.sort_values(by="price")
        df2_t_sorted.reset_index(drop= True, inplace= True)


        df_price= pd.DataFrame(df2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
        df_price.reset_index(inplace= True)
        df_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
        
        col1, col2= st.columns(2)

        with col1:
            
            fig_price= px.bar(df_price, x= "Total_price", y= "host_neighbourhood", orientation='h',
                            title= "PRICE BASED ON HOST_NEIGHBOURHOOD", width= 600, height= 800)
            st.plotly_chart(fig_price)

        with col2:

            fig_price_2= px.bar(df_price, x= "Avarage_price", y= "host_neighbourhood", orientation='h',
                                title= "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",width= 600, height= 800)
            st.plotly_chart(fig_price_2)

        col1, col2= st.columns(2)

        with col1:

            df_price_1= pd.DataFrame(df2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
            df_price_1.reset_index(inplace= True)
            df_price_1.columns= ["host_location", "Total_price", "Avarage_price"]
            
            fig_price_3= px.bar(df_price_1, x= "Total_price", y= "host_location", orientation='h',
                                width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_3)

        with col2:

            fig_price_4= px.bar(df_price_1, x= "Avarage_price", y= "host_location", orientation='h',
                                width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                title= "AVERAGE PRICE BASED ON HOST_LOCATION")
            st.plotly_chart(fig_price_4)


        room_type_t= st.selectbox("Select the Room_Type_t",df2_t_sorted["room_type"].unique())

        df3_t= df2_t_sorted[df2_t_sorted["room_type"] == room_type_t]

        df3_t_sorted_price= df3_t.sort_values(by= "price")

        df3_t_sorted_price.reset_index(drop= True, inplace = True)

        df3_top_50_price= df3_t_sorted_price.head(100)

        fig_top_50_price_1= px.bar(df3_top_50_price, x= "name",  y= "price" ,color= "price",
                                 color_continuous_scale= "rainbow",
                                range_color=(0,df3_top_50_price["price"].max()),
                                title= "MINIMUM_NIGHTS MAXIMUM_NIGHTS AND ACCOMMODATES",
                                width=1200, height= 800,
                                hover_data= ["minimum_nights","maximum_nights","accommodates"])
        
        st.plotly_chart(fig_top_50_price_1)

        fig_top_50_price_2= px.bar(df3_top_50_price, x= "name",  y= "price",color= "price",
                                 color_continuous_scale= "greens",
                                 title= "BEDROOMS, BEDS, ACCOMMODATES AND BED_TYPE",
                                range_color=(0,df3_top_50_price["price"].max()),
                                width=1200, height= 800,
                                hover_data= ["accommodates","bedrooms","beds","bed_type"])

        st.plotly_chart(fig_top_50_price_2)


# Function for data exploration
def data_exploration(df):
    selected_option = st.selectbox("Select an Analysis", ["Price Analysis", "Availability Analysis", "Location Based Analysis", "Geospatial Visualization", "Top Charts Analysis"])

    if selected_option == "Price Analysis":
        price_analysis(df)

    elif selected_option == "Availability Analysis":
        availability_analysis(df)

    elif selected_option == "Location Based Analysis":
        location_analysis(df)

    elif selected_option == "Geospatial Visualization":
        geospatial_analysis(df)

    elif selected_option == "Top Charts Analysis":
        topcharts_analysis(df)


def about_page():
    st.title("AIRBNB DATA ANALYSIS - About Page")
    df = read_data("Airbnb_data.csv")
    st.write("Sample Data:")
    st.write(df.head())

    num_rows = len(df)
    st.write(f"Number of rows after processing: {num_rows}")

    if 'parking' in df.columns:
        free_parking_percentage = (df['parking'] == 'Free Parking').mean() * 100
    else:
        free_parking_percentage = None

    avg_price_property_type = df.groupby('property_type')['price'].mean()


    selected_table = st.radio("Select Table", ["Average Price by Property Type", "Top 10 Listings by Review Scores",
                                               "Summary Statistics for Numerical Columns",
                                               "Number of Listings by Room Type", "Average Price by Host Response Time",
                                               "Average Number of Bedrooms by Property Type", "Minimum Nights by Room Type",
                                               "Maximum Nights by Room Type", "Cancellation Policy Count"])
    if st.button("Submit"):
        if selected_table == "Average Price by Property Type":
            st.subheader("Average Price by Property Type:")
            st.write(avg_price_property_type)
        elif selected_table == "Top 10 Listings by Review Scores":
            st.subheader("Top 10 Listings by Review Scores:")
            top_listings_by_review_scores = df.nlargest(10, 'review_scores')
            st.write(top_listings_by_review_scores)
        elif selected_table == "Summary Statistics for Numerical Columns":
            st.subheader("Summary Statistics for Numerical Columns:")
            st.write(df.describe())
        elif selected_table == "Number of Listings by Room Type":
            st.subheader("Number of Listings by Room Type:")
            room_type_counts = df['room_type'].value_counts()
            st.write(room_type_counts)
        elif selected_table == "Average Price by Host Response Time":
            st.subheader("Average Price by Host Response Time:")
            avg_price_by_response_time = df.groupby('host_response_time')['price'].mean()
            st.write(avg_price_by_response_time)
        elif selected_table == "Average Number of Bedrooms by Property Type":
            st.subheader("Average Number of Bedrooms by Property Type:")
            avg_bedrooms_by_property_type = df.groupby('property_type')['bedrooms'].mean()
            st.write(avg_bedrooms_by_property_type)
        elif selected_table == "Minimum Nights by Room Type":
            st.subheader("Minimum Nights by Room Type:")
            min_nights_by_room_type = df.groupby('room_type')['minimum_nights'].min()
            st.write(min_nights_by_room_type)
        elif selected_table == "Maximum Nights by Room Type":
            st.subheader("Maximum Nights by Room Type:")
            max_nights_by_room_type = df.groupby('room_type')['maximum_nights'].max()
            st.write(max_nights_by_room_type)
        elif selected_table == "Cancellation Policy Count":
            st.subheader("Cancellation Policy Count:")
            cancellation_policy_count = df['cancellation_policy'].value_counts()
            st.write(cancellation_policy_count)



# Streamlit part
scrolling_text = "<h1 style='color:red; font-style: italic; font-weight: bold;'><marquee>AIRBNB DATA ANALYSING PROJECT</marquee></h1>"
st.markdown(scrolling_text, unsafe_allow_html=True)

st.markdown("<h1 style='color: green;'>Welcome to Visit!</h1>", unsafe_allow_html=True)


with st.sidebar:
    select = option_menu("Main Menu", ["Home", "Data Exploration", "Processed Data & Analysis"])


if select == "Home":
    image_url1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUNNJ-9mTnwrGOTy7fqC0Pxr647RR0_2RBUw&s"
    st.sidebar.image(image_url1, caption='**Airbnb Analysis**', use_column_width=True)
    home_page()

elif select == "Data Exploration":
    image_url1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUNNJ-9mTnwrGOTy7fqC0Pxr647RR0_2RBUw&s"
    st.sidebar.image(image_url1, caption='**Airbnb Analysis**', use_column_width=True)
    df = read_data("Airbnb_data.csv")
    data_exploration(df)

elif select == "About":
    image_url1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUNNJ-9mTnwrGOTy7fqC0Pxr647RR0_2RBUw&s"
    st.sidebar.image(image_url1, caption='**Airbnb Analysis**', use_column_width=True)
    about_page()