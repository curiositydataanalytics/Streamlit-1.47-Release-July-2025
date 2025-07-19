import pandas as pd
import streamlit as st
import pydeck as pdk
import time
import datetime as dt
import plotly.express as px

# App config
#----------------------------------------------------------------------------------------------------------------------------------#
# Page config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(
    """
    <style>
    img[data-testid="stLogo"] {
                height: 6rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("What's new in Streamlit 1.47 ?")
st.divider()

with st.sidebar:
    st.logo('https://raw.githubusercontent.com/curiositydataanalytics/Integrate-a-PyDeck-map-into-Streamlit-using-Python-Tutorial/refs/heads/main/CDA_logo_2025_grey.png', size='large')
    st.empty()
#
#

def page1():
    st.header(':one: theme configs')
    st.write("""


This is an example paragraph.

- Item one
- Item two
- Item three

[This is an example URL](https://streamlit.io)

""")
    st.code('''
df = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [10, 20, 30, 40, 50]
})''')
    st.write("""         
# H1 Heading
## H2 Heading
### H3 Heading
#### H4 Heading
##### H5 Heading
###### H6 Heading
    """)



    df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
    st.dataframe(df)


    df_cat = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        'Value': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    })
    fig_cat = px.bar(df_cat, x='Category', y='Value', color='Category')
    st.plotly_chart(fig_cat, use_container_width=True)



def page2():
    st.header(':two: st.chat_input')

    st.code('''
if st.button("Ask for today's menu"):
    st.session_state["my_chat_input"] = "Hi, can you show me today's menu?"
if st.button("Ask for today's weather"):
    st.session_state["my_chat_input"] = "Hi, can you show me today's weather?"

user_input = st.chat_input(key="my_chat_input")

if user_input:
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write("Sure! Here is the information you requested.")
            ''')
    
    cols = st.columns((1,1,1,4), gap='small')

    if cols[0].button("Ask for today's menu"):
        st.session_state["my_chat_input"] = "Hi, can you show me today's menu?"
    if cols[1].button("Ask for today's weather"):
        st.session_state["my_chat_input"] = "Hi, can you show me today's weather?"

    user_input = st.chat_input(key="my_chat_input")

    if user_input:
        st.chat_message("user").write(user_input)
        st.chat_message("assistant").write("Sure! Here is the information you requested.")


def page3():
    st.header(':three: st.code')

    cols = st.columns(2)

    cols[0].subheader('Streamlit 1.46')

    cols[0].code('''
st.code(\'\'\'
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["Toronto", "Vancouver", "Calgary"]
    }
    df = pd.DataFrame(data)
\'\'\')
''')

    cols[0].code('''
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Toronto", "Vancouver", "Calgary"]
}
df = pd.DataFrame(data)''')

    cols[1].subheader('Streamlit 1.47')

    cols[1].code('''
st.code(\'\'\'
    data = {
        "Name": ["Alice", "Bob", "Charlie"],
        "Age": [25, 30, 35],
        "City": ["Toronto", "Vancouver", "Calgary"]
    }
    df = pd.DataFrame(data)
\'\'\', width='content')
''')

    cols[1].code('''
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["Toronto", "Vancouver", "Calgary"]
}
df = pd.DataFrame(data)''', width='content')


def page4():
    st.header(':four: st.cache_data')

    st.code('''
@st.cache_data(show_spinner="Loading...", show_time=True)
def load_data():
    time.sleep(7)
    return {"data": [1, 2, 3]}

if st.button('Load Data'):
    load_data()
''')

    @st.cache_data(show_spinner="Loading...", show_time=True)
    def load_data():
        time.sleep(7)
        return {"data": [1, 2, 3]}
    
    if st.button('Load Data'):
        load_data()


def page5():
    st.header(':five: NumberColumn')

    st.code('''
import pandas as pd

data = {
    "File Name": ["Report.pdf", "Data.csv", "Presentation.pptx"],
    "Size (Bytes)": [2048, 1572864, 10485760],
}
df = pd.DataFrame(data)

st.dataframe(
    df,
    column_config={"Size (Bytes)": st.column_config.NumberColumn(format="bytes")},
    width=400
)
''')

    data = {
        "File Name": ["Report.pdf", "Data.csv", "Presentation.pptx"],
        "Size (Bytes)": [2048, 1572864, 10485760],
    }
    df = pd.DataFrame(data)

    st.dataframe(
        df,
        column_config={
            "Size (Bytes)": st.column_config.NumberColumn(format="bytes")
        },
        width=400
    )

def page6():
    st.header(':six: st.navigation')

    st.code('''
pg = st.navigation({'Section A' : [st.Page(page1, title='theme configs'),
                    st.Page(page2, title='st.chat_input'),
                    st.Page(page3, title='st.code'),
                    st.Page(page4, title='st.cache_data'),
                    st.Page(page5, title='NumberColumn'),
                    st.Page(page6, title='st.navigation'),
                    st.Page(page7, title='st.date_input')],
                    'Section B' : [
                    st.Page(page8, title="Test Page A"),
                    st.Page(page9, title="Test Page B")]})
pg.run()
''')


def page7():
    st.header(':seven: st.date_input')

    st.code('''
import datetime as dt
                    
today = dt.date.today()
start = today - dt.timedelta(days=7)

st.date_input("Select a date range:", (start, today))           
''')

    today = dt.date.today()
    start = today - dt.timedelta(days=7)

    st.date_input("Select a date range:", (start, today))

def page8():
    st.write("Page 1")

def page9():
    st.write("Page 2")



pg = st.navigation({'Section A' : [st.Page(page1, title='theme configs'),
                    st.Page(page2, title='st.chat_input'),
                    st.Page(page3, title='st.code'),
                    st.Page(page4, title='st.cache_data'),
                    st.Page(page5, title='NumberColumn'),
                    st.Page(page6, title='st.navigation'),
                    st.Page(page7, title='st.date_input')],
                    'Section B' : [
                    st.Page(page8, title="Test Page A"),
                    st.Page(page9, title="Test Page B")]})
pg.run()