# SmartMed
SmartMed is an AI-powered health prediction system designed to detect early signs of diseases like Diabetes, Heart Disease, and Parkinson's Disease. This application utilizes machine learning models to provide predictions based on user input.

## Features
- **Diabetes Prediction**: Predicts the likelihood of diabetes based on factors like glucose levels, blood pressure, and BMI.
- **Heart Disease Prediction**: Assesses the risk of heart disease using inputs such as age, sex, and cholesterol levels.
- **Parkinson's Disease Prediction**: Uses voice analysis metrics to predict Parkinson's disease.
- **Chatbot**: Integrates a conversational AI chatbot for user interaction.

## Requirements
- Python 3.8+
- Streamlit
- Scikit-learn
- Google Generative AI (for chatbot functionality)
- Required models for disease prediction

## Installation
1. Clone the repository:
git clone https://github.com/SuhaasNv/SmartMed.git


2. Install necessary packages:
pip install -r requirements.txt


3. Set up your Google API key in a `.env` file:
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY


4. Run the application:
streamlit run app.py


## Usage
1. Navigate to the application URL in your web browser.
2. Select a disease prediction page from the sidebar.
3. Enter the required health metrics.
4. Click the "Predict" button to view the results.

## Contributing
Contributions are welcome! Please submit a pull request with your changes.

## License
[MIT License](https://opensource.org/licenses/MIT)

## Contact
For questions or feedback, please contact [Your Email](mailto:suhaasnvs@gmail.com).
