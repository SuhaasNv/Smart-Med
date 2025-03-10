import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import os
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load models
try:
    diabetes_model = pickle.load(open('saved_models/diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open('saved_models/heart_disease_model.sav', 'rb'))
    parkinsons_model = pickle.load(open('saved_models/parkinsons_model.sav', 'rb'))
except Exception as e:
    logger.error(f"Error loading models: {e}")
    st.error("Failed to load models. Please check the model files.")
    st.stop()

# Sidebar navigation
with st.sidebar:
    selected = option_menu("SmartMed", ["Home", "Diabetes Prediction", "Heart Disease Prediction", "Parkinson's Prediction", "Chatbot"],
                           icons=["house", "activity", "heart", "person", "chat"], default_index=0)

# Home Page
if selected == "Home":
    st.title("Welcome to SmartMed 🏥")

    # Display the image
    st.image("pic.jpg", width=800)  # Adjust the width as needed

    st.write("""
    **SmartMed** is an AI-powered health prediction system that helps users detect early signs of diseases
    like **Diabetes, Heart Disease, and Parkinson's Disease**. Use the sidebar to navigate between different features.

    ### About Me
    - 👨‍💻 **Developer:** Vijaya Suhaas Nadukooru
    - 🎓 **Education:** B.Tech in Information Technology, VIT Vellore
    - 🏆 **Expertise:** AI, Cloud Computing, Full Stack Development
    - 📚 **Research:** Published paper on Steganography
    """)


# Function to display prediction results
def display_prediction(result, disease_name):
    if result == f"{disease_name} Detected":
        st.error(f"Prediction: {result}")
    else:
        st.success(f"Prediction: {result}")

# Diabetes Prediction Page
if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction")

    # Input fields
    Pregnancies = st.number_input("Number of Pregnancies", min_value=0)
    Glucose = st.number_input("Glucose Level", min_value=0)
    BloodPressure = st.number_input("Blood Pressure", min_value=0)
    SkinThickness = st.number_input("Skin Thickness", min_value=0)
    Insulin = st.number_input("Insulin Level", min_value=0)
    BMI = st.number_input("BMI", min_value=0.0)
    DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0)
    Age = st.number_input("Age", min_value=0)

    if st.button("Predict Diabetes"):
        try:
            prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            result = "Diabetes Detected" if prediction[0] == 1 else "No Diabetes"
            display_prediction(result, "Diabetes")
        except Exception as e:
            logger.error(f"Error predicting diabetes: {e}")
            st.error("Failed to predict diabetes. Please try again.")

# Heart Disease Prediction Page
elif selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction")

    # Input fields
    age = st.number_input("Age", min_value=0)
    sex = st.number_input("Sex (0 = Female, 1 = Male)", min_value=0, max_value=1)
    cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3)
    trestbps = st.number_input("Resting Blood Pressure", min_value=0)
    chol = st.number_input("Cholesterol Level", min_value=0)
    fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl (0 = No, 1 = Yes)", min_value=0, max_value=1)
    restecg = st.number_input("Resting ECG Results (0-2)", min_value=0, max_value=2)
    thalach = st.number_input("Max Heart Rate Achieved", min_value=0)
    exang = st.number_input("Exercise Induced Angina (0 = No, 1 = Yes)", min_value=0, max_value=1)
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0)
    slope = st.number_input("Slope of Peak Exercise ST Segment (0-2)", min_value=0, max_value=2)
    ca = st.number_input("Number of Major Vessels Colored (0-4)", min_value=0, max_value=4)
    thal = st.number_input("Thalassemia (0-3)", min_value=0, max_value=3)

    if st.button("Predict Heart Disease"):
        try:
            prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"
            display_prediction(result, "Heart Disease")
        except Exception as e:
            logger.error(f"Error predicting heart disease: {e}")
            st.error("Failed to predict heart disease. Please try again.")

# Parkinson's Disease Prediction Page
elif selected == "Parkinson's Prediction":
    st.title("Parkinson's Disease Prediction")

    # Input fields
    fo = st.number_input("MDVP:Fo(Hz)")
    fhi = st.number_input("MDVP:Fhi(Hz)")
    flo = st.number_input("MDVP:Flo(Hz)")
    jitter_percent = st.number_input("MDVP:Jitter(%)")
    jitter_abs = st.number_input("MDVP:Jitter(Abs)")
    rap = st.number_input("MDVP:RAP")
    ppq = st.number_input("MDVP:PPQ")
    ddp = st.number_input("Jitter:DDP")
    shimmer = st.number_input("MDVP:Shimmer")
    shimmer_db = st.number_input("MDVP:Shimmer(dB)")
    apq3 = st.number_input("Shimmer:APQ3")
    apq5 = st.number_input("Shimmer:APQ5")
    apq = st.number_input("MDVP:APQ")
    dda = st.number_input("Shimmer:DDA")

    if st.button("Predict Parkinson's Disease"):
        try:
            prediction = parkinsons_model.predict([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda]])
            result = "Parkinson's Detected" if prediction[0] == 1 else "No Parkinson's"
            display_prediction(result, "Parkinson's")
        except Exception as e:
            logger.error(f"Error predicting Parkinson's disease: {e}")
            st.error("Failed to predict Parkinson's disease. Please try again.")

# Chatbot Page
elif selected == "Chatbot":
    st.title("🤖 AI ChatBOT")

    try:
        import google.generativeai as gen_ai
    except ImportError:
        logger.error("Google Generative AI library not installed.")
        st.error("Google Generative AI library not installed. Please install it.")
        st.stop()

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    try:
        gen_ai.configure(api_key=GOOGLE_API_KEY)
        model = gen_ai.GenerativeModel('gemini-2.0-flash-exp')
    except Exception as e:
        logger.error(f"Error configuring Google Generative AI: {e}")
        st.error("Failed to configure Google Generative AI. Please check your API key.")
        st.stop()

    def translate_role_for_streamlit(user_role):
        return "assistant" if user_role == "model" else user_role

    if "chat_session" not in st.session_state:
        try:
            st.session_state.chat_session = model.start_chat(history=[])
        except Exception as e:
            logger.error(f"Error starting chat session: {e}")
            st.error("Failed to start chat session. Please try again.")
            st.stop()

    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    user_prompt = st.chat_input("Ask me anything...")
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        try:
            gemini_response = st.session_state.chat_session.send_message(user_prompt)
            with st.chat_message("assistant"):
                st.markdown(gemini_response.text)
        except Exception as e:
            logger.error(f"Error sending message to Gemini-Pro: {e}")
            st.error("Failed to get a response from Gemini-Pro. Please try again.")