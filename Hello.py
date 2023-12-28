import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.llms import VertexAI
import os

import os
import json
from google.oauth2 import service_account

st.set_page_config(page_title="CSV Agent", page_icon=":robot_face:")

def main():
  user_csv = st.file_uploader("Upload your CSV file", type="csv")
  if user_csv is not None:
    user_question = st.text_input("Ask your question about the CSV file")
    if user_question:
      llm = VertexAI(model_name="gemini-pro", temperature=0)
      agent = create_csv_agent(llm, user_csv, verbose=True)
      with st.spinner("Thinking..."):
        response = agent.run(user_question)
      st.write(response)


if __name__ == "__main__":
  main()