# Smart Laptop Recommendation System (ML)

This project is a Machine Learning based web application that recommends the best laptops to users based on their requirements. The system applies step-by-step filtering like e-commerce platforms and ranks laptops according to user budget and performance rating.

---

## 1️⃣ Features

- Interactive multi-step filtering system  
- Recommendations based on:
  - Budget (real-time user input)
  - Usage category (Gaming / Office / Student / Editing / All-rounder)
  - RAM requirement
  - Storage requirement
- Sorts results based on:
  - Price closeness to budget
  - Laptop rating
- Simple and clean UI using Streamlit
- KNN-based recommendation model

---

## 2️⃣ Tech Stack

| Component | Technology |
|----------|------------|
| Programming | Python |
| ML Model | Scikit-learn (Nearest Neighbors + StandardScaler) |
| Dataset Handling | Pandas |
| UI | Streamlit |
| Deployment | GitHub |

---

## 3️⃣ Installation & Run

Install required libraries:

```bash
pip install pandas numpy scikit-learn streamlit
