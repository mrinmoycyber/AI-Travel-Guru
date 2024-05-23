import streamlit as st
import langchain_helper

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("AI Travel Guru")

place = st.sidebar.selectbox("Pick a destination", ("India", "Italy", "Mexico", "UK", "USA", "Germany", "France", "UAE"))

if place:
    response = langchain_helper.generate_travel_package(place)
    st.header(response['package_name'].strip())

    with st.expander("Must Visit"):  # Creates a collapsible section
        menu_items = response['attractions'].strip().split("\n")
        for item in menu_items:
            item = item.strip()
            # Check if the item is not empty
            if item:
                # Remove leading numbers or dots
                while item and item[0] in "1234567890.":
                    item = item[1:].strip()
                # Display item in a scrollable container
                st.write(f"- {item}", unsafe_allow_html=True)



