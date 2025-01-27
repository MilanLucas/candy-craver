import streamlit as st
import pandas as pd
import altair as alt

df_candy_ranks = pd.read_csv("candy-data.csv")
df_candy_ranks = df_candy_ranks.round(2)

candy_top_10 = df_candy_ranks.sort_values('winpercent', ascending=False).head(10)

candy_top_10_sugar = alt.Chart(candy_top_10).mark_bar().encode(
    x=alt.X("competitorname", sort=None, axis=alt.Axis(title="Candy Name")),
    y=alt.Y("sugarpercent", axis=alt.Axis(title="Sugar Percentage"))).properties(title="Top 10 candies sorted by winrate")

candy_top_10_price = alt.Chart(candy_top_10).mark_bar().encode(
    x=alt.X("competitorname", sort=None, axis=alt.Axis(title="Candy Name")),
    y=alt.Y("pricepercent", axis=alt.Axis(title="Price percentage"))).properties(title="Top 10 candies sorted by winrate")

candy_top_10_types_only = candy_top_10.drop(columns = ["competitorname", "sugarpercent", "pricepercent", "winpercent"])

candy_top_10_types = candy_top_10_types_only.sum()


st.write("""
    ### The top 10 halloween candies
    This is a simple dataset I want to run through to showcase some visualsiation methods and baseline analytics. To see
    what a simple dataset can tell us.

    First of, lets see what this top 10 looks like
    """)

st.dataframe(candy_top_10)

st.write("""
    It's a good set of information, but I want it to be a little easier to parse. I think the most relevant factors here
    are the following two: the win percentage and the sugar percentage. I will make a plot that is sorted by the former
    and showcases the latter.
    """)

st.altair_chart(candy_top_10_sugar, use_container_width=True)

st.write("""
    Now something here does catch my eye. Number 2, Reese's minatures has a sugar percentage of 3%, the next closet
    (kitkats at number 4) have a percentage of 31%.\n
    Now in the dataset at hand there is a few things I could look at for an explanation for this, which could
    """)
st.altair_chart(candy_top_10_price, use_container_width=True)

st.write("""
    Now there you go, that lines up with our speculation. The Reese's Miniatures are cheapest among the top 10. We can
    even see that kitkat's, having both second place when it comes to lowest sugar percentage and lower price.\n
    As a final piece, I want to do one more thing with this data, in the data at the top, you can see there is more
    than just percentage data. There is binary data on whether the candy is chocolate, fruity, caramel, etc, etc. I
    want to figure out the common elements between our top 10 candies.
    """)

st.bar_chart(candy_top_10_types)

st.write("""
    Here one particular thing jumps out: chocolate. It is the one common factor for these halloween candies. So, takeway?
    You want to make people happy during halloween, you give them chocolate.""")