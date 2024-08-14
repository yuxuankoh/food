import pandas as pd
import streamlit as st

# st.set_page_config(page_title="Bugis Food🍴", layout="wide")
df = pd.read_csv('/Users/kohyuxuan/Desktop/food_bot/web/combined.csv')
df = df[df['displayName.text'] != 'THE THAI SPA (BEST SPA IN SINGAPORE)']
df_2 = pd.read_csv('/Users/kohyuxuan/Desktop/food_bot/web/combined.csv')
df_2 = df[df['displayName.text'] != 'THE THAI SPA (BEST SPA IN SINGAPORE)']
st.set_page_config(page_title= 'Food🍴', layout="wide" )
st.title("Because deciding where to eat for lunch is tough 😩")
st.markdown(":orange[New] to Bugis? Want to :green[explore] food gems? Gathering :red[top] food places in Bugis on Google for **next team lunches or dinner dates**!")

st.subheader("What do you feel like eating today?", divider = "gray")
query = st.text_input("Search Keywords")
if query:
    mask = df.applymap(lambda x: query in str(x).lower()).any(axis=1)
    df = df[mask]
    st.data_editor(
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
        },
        hide_index=True, 
    )
### RANDOM
st.subheader("No preference? Choose for me", divider="gray")

if st.button("Generate", type="secondary", use_container_width = True):
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
    },
    hide_index=True,
    )

### LIST
st.subheader("Tired of searching? Here's a list", divider="gray")
st.dataframe(
    df_2,
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
    },
    hide_index=True,
    height = 500,
)

st.text("Cheers,")
st.text("Kaelyn")
st.markdown('Just for fun :D For feedback / more places to suggest, you can tele me @kohkaelyn')

