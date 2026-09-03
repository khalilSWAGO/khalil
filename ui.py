import streamlit as st
from api_client import OpenLibraryClient
from reading_list import ReadingListManager
from reading_guide import ReadingGuideGenerator

def run_app():
    st.set_page_config(page_title="Book Companion", page_icon="📚")
    st.title("Book Discovery Companion")

    nav = st.sidebar.radio("Navigation", ["Search", "Reading List", "Reading Guide"])

    client = OpenLibraryClient()
    manager = ReadingListManager()
    guide = ReadingGuideGenerator()

    if nav == "Search":
        st.header("Search Books")
        query = st.text_input("Search title or author")
        if st.button("Search") and query:
            results = client.search_books(query)
            if results:
                for book in results:
                    st.write(f"### {book.title}")
                    st.write(f"Author: {book.authors}")
                    if st.button(f"Add to list", key=f"add_{book.title}"):
                        ok, msg = manager.add_book(book)
                        st.success(msg) if ok else st.warning(msg)

    elif nav == "Reading List":
        st.header("My Books")
        books = manager.load_books()
        if not books:
            st.info("No books saved yet.")
        else:
            for b in books:
                st.write(f"**{b.title}** - Status: {b.status}")
                new_status = st.selectbox("Change status", ["Want to Read", "Reading", "Completed"], key=f"s_{b.title}")
                if st.button("Update", key=f"u_{b.title}"):
                    manager.update_status(b.title, new_status)
                    st.rerun()

    elif nav == "Reading Guide":
        st.header("Get Reading Guide")
        title = st.text_input("Title")
        author = st.text_input("Author")
        if st.button("Generate") and title:
            res = guide.create_full_guide(title, author)
            st.write(res["summary"])
            for q in res["discussion_questions"]:
                st.write(f"* {q}")

if __name__ == "__main__":
    run_app()
