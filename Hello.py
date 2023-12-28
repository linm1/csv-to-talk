import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.llms import VertexAI
import os
import json
from google.oauth2 import service_account
from google.cloud import aiplatform

# Assuming you have stored the JSON contents of your service account key in an environment variable
credentials_json = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
if credentials_json:
    credentials_info = json.loads(credentials_json)
    credentials = service_account.Credentials.from_service_account_info(credentials_info)
else:
    raise EnvironmentError("GOOGLE_APPLICATION_CREDENTIALS environment variable not found.")

# Use credentials to initialize the Google Cloud client
aiplatform.init(project='norse-carport-257701', credentials=credentials)


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