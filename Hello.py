import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.llms import VertexAI
import os

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"] = r'C:\Users\kllkt\Downloads\norse-carport-257701-eff34531b53d.json'


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