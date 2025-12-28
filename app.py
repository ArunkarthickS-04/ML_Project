import streamlit as st
import pandas as pd
import pickle
import os
from openai import OpenAI

# ------------------ LOAD ML MODEL & DATA ------------------ #
model = pickle.load(open("model.pkl", "rb"))
laptops = pd.read_pickle("laptops.pkl")

# ------------------ SETUP OPENAI CLIENT ------------------ #
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Paste key here

# ------------------ LLM FUNCTION ------------------ #
def llm_request(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Latest OpenAI free chat model
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ------------------ EXTRACT USER REQUIREMENTS ------------------ #
def extract_info(user_text):
    prompt = f"""
    Extract laptop requirements: budget + usage.
    Return ONLY this Python dict format:

    {{
        'budget': number in ₹ (default 50000),
        'usage': one of ['gaming','editing','student','office','all-rounder']
    }}

    Text: "{user_text}"
    """
    try:
        data = eval(llm_request(prompt))
        return data
    except:
        return {'budget': 50000, 'usage': 'all-rounder'}

# ------------------ FILTER BEST LAPTOPS ------------------ #
def recommend_laptops(budget, usage):
    filtered = laptops.copy()
    filtered["score"] = abs(filtered["price"] - budget) * -1
    filtered = filtered.sort_values(by="score", ascending=False)
    return filtered.head(3)

def llm_explanation(names, usage, budget):
    laptop_names = ", ".join(names)
    prompt = f"""
    Explain in 4 bullets why these are recommended:
    Laptops: {laptop_names}
    Usage: {usage}
    Budget: ₹{budget}
    """
    return llm_request(prompt)

# ------------------ STREAMLIT UI ------------------ #
st.title("🤖 AI Laptop Recommendation ChatBot")
st.write("Example: *Suggest a gaming laptop under 70000 for editing*")

user_text = st.text_input("Tell me what type of laptop you need:")

if st.button("Recommend"):
    if not user_text.strip():
        st.warning("Please enter your requirement")
    else:
        st.info("🧠 Understanding your requirement...")

        extracted = extract_info(user_text)
        budget = extracted["budget"]
        usage = extracted["usage"]

        st.success(f"🎯 Budget: ₹{budget} | Usage: {usage}")

        results = recommend_laptops(budget, usage)

        if results.empty:
            st.error("No laptops matched. Try different text.")
        else:
            st.subheader("🔥 Best Recommendations")
            names = []
            for _, r in results.iterrows():
                names.append(r["model"])
                st.write(f"**{r['brand_name']} {r['model']}**")
                st.write(f"💰 ₹{r['price']}  ⭐ {r['rating']}")
                st.write("---")

            st.success(llm_explanation(names, usage, budget))

st.caption("Powered by OpenAI GPT + Machine Learning")

