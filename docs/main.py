import streamlit as st

st.set_page_config("BackPipe Docs", "📖")

home, server, responses, rq_obj, config, redirect = st.tabs(["Home", "Server", "Responses", "Request Objects", "Config", "Redirects"])

home.write(open("docs/home.md", "r").read())
server.write(open("docs/server.md", "r").read())
responses.write(open("docs/responses.md", "r").read())