import pandas as pd
import streamlit as st

# Load and filter data
df = pd.read_csv('combined.csv')

# Streamlit setup
st.set_page_config(page_title='Bugis Food🍴', layout="wide")
st.title("Because deciding where to eat for lunch is tough 😩")
st.markdown(":orange[New] to Bugis? Want to :green[explore] food gems? Gathering :red[top] food places in Bugis on Google for **next team lunches or dinner dates**!")

st.subheader("What do you feel like eating today?", divider="gray")
query = st.text_input("Search Keywords")
if query:
    mask = df.applymap(lambda x: query.lower() in str(x).lower()).any(axis=1)
    result_df = df[mask]
    st.data_editor(
        result_df,
        column_config={
            "displayName.text": "Name",
            "primaryTypeDisplayName.text": "Keyword Category",
            "shortFormattedAddress": "Address", 
            "userRatingCount": "# of Ratings",
            "rating": st.column_config.NumberColumn(
                "Ratings",
                help="Number of stars on Google",
                format="%s ⭐",
            ),
            "googleMapsUri": st.column_config.LinkColumn("Maps URL"),
            "websiteUri": st.column_config.LinkColumn("Web URL"),
            "nationalPhoneNumber": "Phone", 
            "servesVegetarianFood": "Vegetarian Options",
        },
        hide_index=True,
    )

# Random selection
st.subheader("No preference? Choose for me", divider="gray")
if st.button("Generate", type="secondary", use_container_width=True):
    random_rows = df.sample(n=3)
    st.dataframe(
        random_rows,
        column_config={
            "displayName.text": "Name",
            "primaryTypeDisplayName.text": "Keyword Category",
            "shortFormattedAddress": "Address", 
            "userRatingCount": "# of Ratings",
            "rating": st.column_config.NumberColumn(
                "Ratings",
                help="Number of stars on Google",
                format="%s ⭐",
            ),
            "googleMapsUri": st.column_config.LinkColumn("Maps URL"),
            "websiteUri": st.column_config.LinkColumn("Web URL"),
            "nationalPhoneNumber": "Phone", 
            "servesVegetarianFood": "Vegetarian Options",
        },
        hide_index=True,
    )

# Full list
st.subheader("Tired of searching? Here's a list", divider="gray")
st.dataframe(
    df,
    column_config={
        "displayName.text": "Name",
        "primaryTypeDisplayName.text": "Keyword Category",
        "shortFormattedAddress": "Address", 
        "userRatingCount": "# of Ratings",
        "rating": st.column_config.NumberColumn(
            "Ratings",
            help="Number of stars on Google",
            format="%s ⭐",
        ),
        "googleMapsUri": st.column_config.LinkColumn("Maps URL"),
        "websiteUri": st.column_config.LinkColumn("Web URL"),
        "nationalPhoneNumber": "Phone", 
        "servesVegetarianFood": "Vegetarian Options",
    },
    hide_index=True,
    height=500,
)

#
st.subheader("Specially curated for:", divider="gray")
column_1, column_2 = st.columns(2)
if column_1.button('Anjum'):
    st.markdown(":orange[Learning preferences in progress]")
if column_2.button('Eugene'):
    st.markdown(":orange[Learning preferences in progress]")
# Footer
st.markdown('Just for fun :D For feedback / more places to suggest, you can tele me @kohkaelyn')
st.text("Cheers,")
st.text("Kaelyn")


