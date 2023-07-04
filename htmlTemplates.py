import streamlit as st
css = '''
<style>
.stApp {
        padding: 2rem;
        background-image:url("https://img.freepik.com/free-photo/chat-message-yellow-speech-bubble-icon-notification-button-talk-dialog-symbol-conversation-button-icon-symbol-background-3d-illustration_56104-2068.jpg");
        background-repeat:no-repeat;
        background-size:cover;

    }
    .stApp header {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 1rem;
        font-family:Georgia;
        background-color:rgb(201 207 196 / 79%);
        border-radius: 5px;
    }
    .stApp header .stApp-title {
        font-size: 2rem;
        margin-right: 0.5rem;
        color: white;
    }
    .css-ue6h4q{
        margin-bottom:20px;
        font-weight:bold;
    }
    h2{
        font-family:serif;
        font-size:50px;
    }
    .st-b8{
        width:550px;
    }
    .stApp header .stApp-icon {
        font-size: 2rem;
        color:white;
    }
    .stTextInput {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .stButton {
        margin-top: 1rem;
        text-align:center;
    }
    p{
        font-family:georgia;
    }
    .stSpinner {
        margin-top: 1rem;
    }
    .stFileUploader {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .css-vk3wp9{
       background-color:rgb(201 207 196 / 79%);
    }
    .css-1txgwv8 .eqdbnj015{
        margin-top:70px;
    }

    .stSidebar {
        padding: 0.5rem;
        border-radius: 5px;
       
    }
    .stSidebar .stButton {
        margin-top: 1rem;
        margin-bottom: 1rem;
        background-color:grey;
    }
    .stSidebar .stSubheader {
        margin-bottom: 0.5rem;
    }
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''