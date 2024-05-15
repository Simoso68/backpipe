import streamlit as st

st.set_page_config("BackPipe Docs", "📖")

home, server, responses, request_object, redirect, config = st.tabs(["Home", "Server", "Responses", "Request Objects", "Redirects", "Config"])

home.write(open("docs/home.md", "r").read())
server.write(open("docs/server.md", "r").read())
responses.write(open("docs/responses.md", "r").read())
request_object.write(open("docs/request_object.md", "r").read())
redirect.write(open("docs/redirects.md", "r").read())