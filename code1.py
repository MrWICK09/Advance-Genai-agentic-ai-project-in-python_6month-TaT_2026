import streamlit as st
import pandas as pd
import numpy as np

# --- Page Config ---
st.set_page_config(page_title="My First App", layout="centered")

# --- Title ---
st.title("🚀 My First Streamlit App")
st.write("This is a simple and interactive app built using Streamlit.")

# --- Sidebar ---
st.sidebar.header("👤 User Input Features")

user_name = st.sidebar.text_input("What is your name?", "Aryan Singh")
age = st.sidebar.slider("Select your age", 0, 100, 25)
favorite_color = st.sidebar.selectbox(
    "Favorite color?", ["Blue", "Red", "Green", "Yellow"]
)

# --- Greeting ---
st.header(f"👋 Welcome, {user_name}!")

st.write(f"""
- 🎂 Age: **{age}**
- 🎨 Favorite Color: **{favorite_color}**
""")

# --- Fun message ---
if age < 18:
    st.info("You're young and energetic! 💪")
elif age < 50:
    st.success("You're in your prime! 🚀")
else:
    st.warning("You're full of experience! 👑")

# --- Data Section ---
st.subheader("📊 Random Data")

# Generate data
data = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])

st.dataframe(data)

# --- Chart ---
st.subheader("📈 Simple Chart")
st.line_chart(data)

# --- Show raw data ---
if st.checkbox("Show raw data"):
    st.write(data)

# --- Refresh button ---
if st.button("🔄 Generate New Data"):
    st.experimental_rerun()

# --- Button interaction ---
if st.button("👋 Say Hello"):
    st.success(f"Hello {user_name}! Have a great day 😄")
else:
    st.write("Click the button to get a greeting!")

# --- Footer ---
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
