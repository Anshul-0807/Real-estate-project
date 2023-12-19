from sentence_transformers import SentenceTransformer
import openai
import streamlit as st
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
import pickle

def query_refiner(conversation, query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Given the following user query and conversation log, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base.\n\nCONVERSATION LOG: \n{conversation}\n\nQuery: {query}\n\nRefined Query:",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']


def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses']) - 1):
        conversation_string += "Human: " + st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: " + st.session_state['responses'][i + 1] + "\n"
    return conversation_string


def update_embeddings_faiss():
    with open("../project_txt.txt", "r") as file:
        text = file.read()

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=400,
        chunk_overlap=20,
        length_function=len
    )
    faiss_chunks = text_splitter.split_text(text)


    # create embeddings
    # embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_texts(faiss_chunks, embeddings)


    with open('../db_faiss.pkl', 'wb') as file:
        pickle.dump(db, file)

def on_btn_click():
    st.session_state['responses'] = ["How can I assist you?"]
    st.session_state['requests'] = []
    st.session_state.buffer_memory = ConversationBufferWindowMemory(k=3, return_messages=True)
