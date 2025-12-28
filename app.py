import streamlit as st
import pandas as pd
import pickle

# Load model and dataset
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))
df = pd.read_pickle("laptops.pkl")

st.set_page_config(page_title="Smart Laptop Consultant")
st.title("Smart Laptop Consultant System 💻🤖")
st.write("Answer step-by-step & get the best laptop suggestion!")

# ================== STEP 1: BUDGET ==================
st.header("Step 1️⃣: Enter Your Budget 💰")
budget = st.number_input("Maximum Budget (₹)", min_value=20000, max_value=300000, step=1000)

if st.button("Next ➜ Filter by Budget"):
    st.session_state.filtered = df[df["price"] <= budget]
    if st.session_state.filtered.empty:
        st.error("⛔ Increase budget to get better options 🙏")
    else:
        count = len(st.session_state.filtered)
        st.success(f"✔ Found {count} laptops under ₹{budget}")
        st.info(f"📊 {count} laptops available after Budget filter")
        if count < 3:
            st.warning("⚠ Very few options left! Try increasing budget")

if "filtered" in st.session_state:

    # ================== STEP 2: USAGE ==================
    st.header("Step 2️⃣: Choose Your Purpose 🎯")

    usage_options = [
        "Gaming Only", "Office Only", "Student Only",
        "Gaming + Student", "Office + Gaming",
        "Gaming + Editing", "Student + Editing", "Office + Editing",
        "Editing Only", "All Rounder"
    ]
    usage = st.selectbox("Select Usage Purpose", usage_options)

    spec_map = {
        "Gaming Only": {"ram": 16, "cores": 6, "threads": 12, "gpu": True},
        "Office Only": {"ram": 8, "cores": 4, "threads": 6, "gpu": False},
        "Student Only": {"ram": 8, "cores": 4, "threads": 6, "gpu": False},
        "Gaming + Student": {"ram": 16, "cores": 6, "threads": 12, "gpu": True},
        "Office + Gaming": {"ram": 16, "cores": 6, "threads": 12, "gpu": True},
        "Gaming + Editing": {"ram": 16, "cores": 8, "threads": 12, "gpu": True},
        "Student + Editing": {"ram": 16, "cores": 6, "threads": 8, "gpu": False},
        "Office + Editing": {"ram": 16, "cores": 6, "threads": 8, "gpu": False},
        "Editing Only": {"ram": 16, "cores": 8, "threads": 10, "gpu": False},
        "All Rounder": {"ram": 16, "cores": 6, "threads": 10, "gpu": True},
    }

    if st.button("Next ➜ Filter by Usage"):
        req = spec_map[usage]
        filtered = st.session_state.filtered[
            (st.session_state.filtered["ram_num"] >= req["ram"]) &
            (st.session_state.filtered["core_num"] >= req["cores"]) &
            (st.session_state.filtered["threads_num"] >= req["threads"])
        ]

        if req["gpu"]:
            filtered = filtered[filtered["gpu_type"].notna()]

        if filtered.empty:
            st.error("⛔ Budget too low for selected use! Increase budget 🙏")
        else:
            st.session_state.filtered = filtered
            count = len(filtered)
            st.success(f"🎯 {count} laptops match your purpose!")
            st.info(f"📊 {count} laptops available after Usage filter")
            if count < 3:
                st.warning("⚠ Very limited options for this usage!")

if "filtered" in st.session_state:

    # ================== STEP 3: RAM ==================
    st.header("Step 3️⃣: Select RAM 🧠")
    ram_options = sorted(st.session_state.filtered["ram_num"].unique())
    ram = st.selectbox("Minimum RAM (GB)", ram_options)

    if st.button("Next ➜ Filter by RAM"):
        filtered = st.session_state.filtered[st.session_state.filtered["ram_num"] >= ram]
        if filtered.empty:
            st.error("⛔ Try selecting lower RAM requirement")
        else:
            st.session_state.filtered = filtered
            count = len(filtered)
            st.success(f"✔ {count} laptops after RAM filtering")
            st.info(f"📊 {count} laptops available after RAM filter")
            if count < 3:
                st.warning("⚠ Very few options left now!")

if "filtered" in st.session_state:

    # ================== STEP 4: STORAGE ==================
    st.header("Step 4️⃣: Storage Size Selection 💽")
    storage_options = sorted(st.session_state.filtered["memory_size"].unique())
    storage = st.selectbox("Minimum Storage (GB)", storage_options)

    if st.button("🎯 Recommend Best Laptop!"):
        filtered = st.session_state.filtered[
            st.session_state.filtered["memory_size"] >= storage
        ]
        if filtered.empty:
            st.error("⛔ Lower storage requirement to get results")
            st.stop()

        count = len(filtered)
        st.info(f"📊 {count} laptops available after Storage filter")

        if count < 3:
            st.warning("⚠ Try modifying filters for better range")

        # Best value + rating priority sorting
        filtered["price_diff"] = budget - filtered["price"]
        filtered = filtered.sort_values(by=["price_diff", "rating"], ascending=[True, False])

        st.success("🔥 Best Laptop Suggestions for You 🔥")
        for i in range(min(3, len(filtered))):
            lap = filtered.iloc[i]
            st.subheader(f"🌟 {lap['brand_name']} {lap['model']}")
            st.write(f"💰 Price: ₹{lap['price']}")
            st.write(f"🧠 CPU: {lap['core_num']} Cores / {lap['threads_num']} Threads")
            st.write(f"📌 RAM: {lap['ram_num']} GB | Storage: {lap['memory_size']} GB")
            st.write(f"⭐ Rating: {lap['rating']}")
            st.write(f"🎯 Perfect for: {usage}")
            st.write("---")
