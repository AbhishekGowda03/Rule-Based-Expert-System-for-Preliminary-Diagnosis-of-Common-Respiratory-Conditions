Respiratory Expert System (Rule-Based Diagnosis)

This project is a rule-based expert system built using Python and Streamlit to provide a preliminary interpretation of common respiratory conditions based on user-reported symptoms. It is meant as an educational demonstration of rule-based inference logic and deterministic reasoning.

Overview

Unlike machine learning models that rely on training data, this system uses explicit IF–THEN expert rules derived from typical respiratory diagnostic patterns. The application maps combinations of symptoms (such as fever, cough type, wheezing, phlegm, etc.) to likely explanations like:

Common cold

Flu-like viral infection

Asthma-like pattern

Possible pneumonia

Allergy-related symptoms

COVID-like symptom profile

Non-specific respiratory infection

Unclassified / unclear pattern

The focus is on transparency: the system not only gives a suggestion, but also shows which reasoning rules were triggered.

Features

Interactive symptom questionnaire via Streamlit UI

Clear rule-based reasoning

Deterministic, transparent inference (no AI black-box)

Human-readable explanation of triggered rules

Lightweight and easy to run locally

How It Works

At the core of the system is a knowledge base implemented as conditional rules in Python. Example logic:

IF high fever + wet cough + chest pain + colored phlegm  
THEN pneumonia-like condition


Rules are evaluated in sequence, with specific patterns taking priority. This is similar to how early AI expert systems and clinical decision support tools were implemented.
