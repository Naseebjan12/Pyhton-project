import streamlit as st
import os
import time
from openai import OpenAI
client = OpenAI(api_key=os.environ['key'])
st.header(' Factified 🧑‍🚀')

command=st.chat_input(placeholder='Enter Country , Animal , place or any place you want to generate Fact ?')
if command:
    



    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {"role": "system", "content": " You are a fact Teller developed by Naseeb jan .your role is a fact teller about a spacific word, place or animal according to the user command u are responsible to generate at least 30 fact about a spacific command enter by the user . donot generate fact which is duplicated. all the fact must be true and have no error or emission is present in the fact. the fact will be in the following table form using the format like this (the first column of the table contain the fact number the second column contain  the fact  ) "},
        {"role": "user", "content": f"{command}"}
    ]
    )
    result_response=response.choices[0].message.content
    st.write(f'{command}')
    st.spinner(text=f'Generating Fact about {command}')
    with st.chat_message(name='Assistant',avatar='🧑‍🚀'):
        st.write(result_response)
    
