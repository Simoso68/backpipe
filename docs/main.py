import streamlit as st

st.set_page_config("BackPipe Docs", "📖")

home, server, responses, request_objects, redirect, config, tools = st.tabs(["Home", "Server", "Responses", "Request Objects", "Redirects", "Config", "Tools"])

home.write(open("docs/home.md", "r").read())
server.write(open("docs/server.md", "r").read())
responses.write(open("docs/responses.md", "r").read())
request_objects.write(open("docs/request_objects.md", "r").read())
redirect.write(open("docs/redirects.md", "r").read())
config.write(open("docs/config.md", "r").read())
tools.write(open("docs/tools.md", "r").read())