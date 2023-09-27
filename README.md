<div align="center">
  <img src="https://profiles.howard.edu/sites/profiles.howard.edu/files/styles/profile_square/public/2023-09/BurgeHead2023.jpeg?h=806369ab&itok=lbCxswZK" alt="Slim GPT-2 Chatbot">
</div>

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://wardleychatbot.streamlit.app/)

# Slim Chat Bot

This is a Streamlit web app utilizing GPT-4 model of OpenAI to enable interactive chat with an assistant trained to provide responses on culture and history of HBCUs. The responses are designed to be at the comprehension level of a 12-year-old and the assistant can communicate using pop culture and African American vernacular.



## Features
- This chatbot utilizes the GPT-4 API from OpenAI.
- It is designed to provide responses in the context of expert cultural historian on HBCUs, incorporating content from wikipedia, and various HBCU websites.
- All interactions are kept in a session state, ensuring conversation continuity during the user's session.
- A simple user interface built with Streamlit.

## How to Run
1. Clone the repository.
2. Set the OpenAI API key in the Streamlit secrets manager.
3. Run the streamlit app using the command streamlit run SlimGPT.py.

## Dependencies
To run this code, you need the following Python packages:

- openai
- streamlit
- streamlit-chat

### API Keys
The application uses the OpenAI API. You will need to obtain an API key from OpenAI and set it in the Streamlit secrets manager.

## Using the Application
Once the application is running, you can use the input box labeled "Question for Slim?" to ask your question. After entering your question, the application will generate an answer and display it on the screen.

## Developer Info
This application is developed by Legand Burge

## Version Info
The current version of this application is 0.0.1.

## Disclaimer
This application is not optimized and may run out of OpenAI credits. 

Please use responsibly and in accordance with OpenAI's use-case policy.

## License
This project is licensed under Creative Commons Attribution Share-Alike.
