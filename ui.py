import streamlit as st

st.set_page_config(page_title="Book Discovery Companion", page_icon="📚", layout="wide")

st.title("📚 Book Discovery Companion")

nav = st.sidebar.radio("Navigation", ["Search", "Reading List", "Reading Guide"])

if nav == "Search":
    st.header("🔍 Search for Books")
    query = st.text_input("Enter book title or author:")
    if st.button("Search") and query:
        st.success(f"Showing results for: {query}")
        # Placeholder search output
        st.write("• The Great Gatsby by F. Scott Fitzgerald")
        st.write("• To Kill a Mockingbird by Harper Lee")

elif nav == "Reading List":
    st.header("📋 My Reading List")
    st.info("Your saved books will appear here.")

elif nav == "Reading Guide":
    st.header("🤖 AI Reading Guide")
    title = st.text_input("Enter a book title to generate a guide:")
    if st.button("Generate Guide") and title:
        st.write(f"### Reading Guide for {title}")
        st.write("1. Key Themes")
        st.write("2. Chapter Summary")
        st.write("3. Discussion Questions")
