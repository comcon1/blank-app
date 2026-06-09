import streamlit as st

st.set_page_config(page_title="Blank app with Google auth")

cur_title = "🎈 Testing G.Auth 🎈"


if not st.user.is_logged_in:
    st.title(cur_title)
    st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
    st.write("Please sign in.")
    st.button("Log in with Google", on_click=st.login)
else:
    st.title(cur_title)
    st.success(f"Signed in as {st.user.name}")
    st.write(f"Email: {st.user.email}")
    st.button("Log out", on_click=st.logout)