import streamlit as st
import openai
from config import OPENAI_API_KEY
# import ktrain

openai.api_key = OPENAI_API_KEY

# predictor = ktrain.load_predictor('Empathy_Segment_Classifier')
# @st.cache


def empathy_prompt(text: str) -> str:
    response = openai.Completion.create(
        model='curie:ft-contentware-2022-07-24-17-38-44',
        prompt=f"{text}\n\n###\n\n",
        temperature=0.7,
        max_tokens=35,
        top_p=1,
    )
    out_text = response['choices'][0]['text'].strip('\n')
    out_text = out_text.split('\n')[0]
    return out_text


st.title('Empathy Segment Prediction')
st.header('Please enter the User and Caregiver Text')

client_text_input = st.text_input('Client Input')

cg_text_input = st.text_input('Caregiver Input')
text_input = f'Client: {client_text_input}\nCaregiver: {cg_text_input}'

class_text_input = ''
if st.button('Create Empathy Segment') and client_text_input != '' and cg_text_input != '':
    result = empathy_prompt(text_input)
    st.success(result)
else:
    st.success('No input')

st.write('\nPlease feel free to adjust the input from above as needed. The adjusted input can then be placed below to classify the segment')
class_text_input = st.text_input('Classification Input')
if st.button('Classify Output') and class_text_input:
    st.success('Model Loading Error')
#     try:
#         classification = predictor.predict(class_text_input)
#         st.success(classification)
#     except Exception as e:
#         print(e)
#         st.success('Model Loading Error')
else:
    st.success('No Classification')
