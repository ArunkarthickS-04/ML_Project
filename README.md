Smart Laptop Recommendation System using Machine Learning

A machine learning based laptop recommendation system that helps users choose the best laptop based on budget and performance requirements. The system filters laptops step-by-step similar to e-commerce recommendations and ranks options by price suitability and ratings.

PROJECT OBJECTIVE:
• Recommend the best laptop based on user requirements
• User inputs: Budget, Usage Type, RAM, Storage
• Helps decision-making for students, office users and gamers
• Provides best value within budget range

METHODOLOGY – MACHINE LEARNING:
• Features used: price, ram_num, core_num, threads_num
• StandardScaler used for normalization
• NearestNeighbors recommendation model
• Ranking logic: 1) Price closest to budget 2) Higher rating

TECHNOLOGY USED:
• Python
• Streamlit for UI
• Pandas and NumPy for data processing
• Scikit-learn for machine learning
• GitHub for version control

HOW TO INSTALL AND RUN:
Install required libraries using:
pip install pandas numpy scikit-learn streamlit

Run the application using:
streamlit run app.py
Application will open automatically in the browser.

DATASET INFORMATION:
Contains laptop details such as:
• Brand and Model
• CPU cores and threads
• RAM and Storage
• GPU availability
• Price in ₹ and user rating

Files included:
• laptop_cleaned_dataset.csv
• laptops.pkl

MAIN FEATURES IMPLEMENTED:
• Real-time budget filtering
• Step-by-step guided selection
• Ten usage categories (Gaming / Office / Student / Editing etc.)
• Shows number of laptops available after each filter
• Displays top 3 best options matching needs

FUTURE IMPROVEMENTS:
• Live price fetch from Amazon / Flipkart
• GPU performance score calculation
• Deploy to cloud for public access
• Voice guided recommendation

DEVELOPER DETAILS:
Name: Arunkarthick S
Project: Machine Learning Mini Project
Year: 2025
