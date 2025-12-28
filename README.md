# AI Laptop Recommendation System (Machine Learning + LLM)

Live Website: https://mlproject-ijbodtrg3qxrhhukeuuxky.streamlit.app/
GitHub Repo: https://github.com/ArunkarthickS-04/ML_Project
 
# ABSTRACT
This project introduces a smart AI-based laptop recommendation system that helps users select the best laptop based on their personal needs like gaming, office use, student use, or editing and budget. The system uses a Machine Learning model (K-Nearest Neighbors) to find laptops with similar specifications and a Large Language Model (OpenAI GPT) to understand natural language input and generate explanations. The application is deployed online using Streamlit Cloud so users can access it anywhere.

# OBJECTIVE
• Understand user requirements using natural language input  
• Recommend laptops that fit performance needs and budget  
• Provide an intelligent explanation for each recommended device  
• Reduce manual laptop searching time  

# FEATURES
• Natural language input (e.g., "gaming laptop under 60000")  
• Top-3 accurate recommendations  
• AI-based explanation for why each laptop is suitable  
• Easy-to-use web interface  
• Fast cloud-hosted system  

# TECHNOLOGY STACK
• Python  
• Streamlit (Web UI)  
• OpenAI GPT-4o-mini (LLM)  
• Scikit-Learn (KNN Algorithm)  
• Pandas, NumPy (Data Processing)  
• Streamlit Cloud Deployment  
• Pickle (.pkl) dataset format  

# SYSTEM ARCHITECTURE
User Input → LLM extracts usage + budget → ML KNN Model → Recommendations + Explanation Output

# DATASET DETAILS
• 1000+ laptop entries  
• Preprocessed and stored in laptops.pkl  
• Main ML features: RAM, CPU cores, threads, price  

# METHODOLOGY
1. Data preprocessing and feature extraction  
2. Standardization using StandardScaler  
3. KNN model training for similarity detection  
4. LLM for requirement extraction and explanation  
5. Online deployment using Streamlit  

# PROJECT FILES OVERVIEW
app.py → Main Streamlit application  
model.pkl → Trained KNN ML model  
scaler.pkl → StandardScaler model  
laptops.pkl → Preprocessed dataset  
requirements.txt → Required libraries  
README.md → Documentation  

# HOW TO RUN LOCALLY
git clone https://github.com/ArunkarthickS-04/ML_Project.git
 cd ML_Project
 pip install -r requirements.txt
 streamlit run app.py
(Ensure OpenAI API key is set in Streamlit Secrets)

# RESULTS
• Successful cloud deployment  
• Instant and relevant recommendations  
• Increased user convenience and efficiency  

# CONCLUSION
The system successfully recommends laptops based on both technical specifications and user intent. The combination of Machine Learning + Generative AI makes the system accurate and easy to use. The project proves that hybrid AI can greatly assist decision-making.

# FUTURE ENHANCEMENTS
• Real-time pricing from Amazon/Flipkart  
• GPU score and benchmark ranking  
• Voice-enabled chatbot  
• Mobile application  

# DEVELOPER DETAILS
Name: Arunkarthick S  
Course: B.E. CSE  
Year: 2nd Year  
Project Type: Mini Project (AI + ML)

