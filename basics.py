import streamlit as st
st.title("Welcome to my streamlit application 🚀")
st.header("Deployed By Khaja Mainuddin")
st.subheader("Want to know more about me")
st.text("Hi my name is Khaja Mainuddin . I am currently training  at Innomatics Research Labs")
st.markdown("This is my **Linked Page**. Here you can *connect* with me and this is my linkedin account [Linkedin Profile Link](https://www.linkedin.com/in/sonam-pawar-029345211)")
st.caption("Thank you for connecting.")
st.subheader("Below is the simple Python Program")
st.code("""
def hello_world():
    print("Hello, World!")
    return "Welcome to Streamlit"
""", language="python")
st.subheader("Below is the simple SQL Code")
st.code("""
SELECT * FROM users
WHERE age > 18
ORDER BY name;
""", language="sql")
st.subheader("Below code shows the simple dataframe")
data = {
    "name": "Alice",
    "age": 25,
    "address": {
        "city": "New York",
        "zip": "10001"
    },
    "hobbies": ["reading", "coding", "gaming"]
}

st.json(data)