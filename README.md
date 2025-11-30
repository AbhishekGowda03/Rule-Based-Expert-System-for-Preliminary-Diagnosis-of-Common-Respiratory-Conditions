# Respiratory Diagnosis Expert System 🩺

**Rule-based AI system for preliminary assessment of common respiratory conditions**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Project Overview

A **rule-based expert system** designed for preliminary respiratory health interpretation. The system evaluates symptoms such as temperature, cough type, breathing difficulty, chest pain, and phlegm type using transparent, auditable medical-style rules.

**Domain:** Healthcare → Respiratory Condition Assessment

---

## ✨ Key Features

- **Explicit medical-style IF–THEN rules**
- **Transparent reasoning — displays triggered rules**
- **Streamlit UI for interactive input**
- **No machine learning — deterministic logic**
- **Works on Windows / Mac / Linux**
- **Minimal setup & lightweight**

---

## 🧠 Decision Criteria (Knowledge Rules)

| Condition | Trigger Pattern |
|----------|-----------------|
| Common cold | No fever + mild/dry cough + sneezing + sore throat |
| Flu-like viral illness | Fever + cough + fatigue |
| Pneumonia-like | High fever + wet cough + chest pain + colored phlegm |
| Asthma-like | Wheezing + shortness of breath |
| COVID-like | Fever + dry cough + loss of smell |
| Allergy-related | Sneezing + itchy eyes + no fever |
| Non-specific | Fever + cough (unclear origin) |

---
