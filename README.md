# Smart Laptop Recommendation System using Machine Learning

A machine learning based web application that recommends the best laptops based on budget and performance needs.

The system filters laptops step-by-step and displays best matches similar to e-commerce product recommendations.

---

## Project Objective

To help users find the most suitable laptop based on:

• Budget  
• Usage type (Gaming / Office / Student / Editing / All-rounder)  
• RAM requirement  
• Storage requirement  

Provides best value suggestions within user budget.

---

## Machine Learning Methodology

Features used:

• price  
• ram_num  
• core_num  
• threads_num  

Data preprocessing:

• StandardScaler applied  

Model:

• NearestNeighbors (KNN-based similarity)  

Ranking logic:

1. Price closest to budget  
2. Higher rating preferred  

---

## Technology Used

• Python  
• Pandas  
• NumPy  
• Scikit-learn  
• Streamlit  
• GitHub  

---

## How to Install & Run

Install requirements:

pip install pandas numpy scikit-learn streamlit  

Run the app:

streamlit run app.py  

The interface will launch in browser automatically.

---

## Dataset Information

Contains laptop specification data including:

• Brand & Model  
• CPU cores and threads  
• RAM & Storage  
• GPU type (if available)  
• Price (₹)  
• Rating  

Files included:

• laptop_cleaned_dataset.csv  
• laptops.pkl  

---

## Main Features Implemented

• Real-time filtering after every step  
• 10 categorized usage options  
• Displays available laptop count  
• Shows top 3 best matching laptops  
• Guided experience like shopping platforms  

---

## Future Enhancements

• Online real-time price update from Flipkart / Amazon  
• GPU benchmark-based filtering  
• Cloud deployment for public use  
• Voice-driven recommendation  

---

## Developer

**Arunkarthick S**  
Machine Learning Mini Project — 2025  
