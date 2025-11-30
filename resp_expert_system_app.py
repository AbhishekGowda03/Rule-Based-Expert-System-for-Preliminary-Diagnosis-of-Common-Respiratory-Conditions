import streamlit as st


# -----------------------------
# Domain Knowledge - Rules
# -----------------------------

def diagnose_respiratory_condition(
        age,
        temperature,
        cough_type,
        chest_pain,
        sore_throat,
        loss_of_smell,
        wheezing,
        shortness_of_breath,
        sneezing,
        itchy_eyes,
        phlegm_color,
        duration_days,
        fatigue
):
    """
    Simple rule-based expert system for preliminary respiratory diagnosis.
    Returns (diagnosis, explanation).
    """

    rules_triggered = []

    # Helper flags
    has_fever = temperature is not None and temperature >= 38.0
    high_fever = temperature is not None and temperature >= 39.0
    long_duration = duration_days is not None and duration_days >= 7

    # -----------------------------
    # RULES
    # -----------------------------

    # Rule 1: Pneumonia-like pattern
    if high_fever and cough_type == "Wet / productive" and chest_pain and phlegm_color in ["Yellow/Green",
                                                                                           "Rusty/Bloody"]:
        rules_triggered.append(
            "High fever + wet cough + chest pain + colored phlegm → possible pneumonia or lower respiratory infection."
        )
        diagnosis = "Possible pneumonia / lower respiratory tract infection"

    # Rule 2: Flu-like illness (Influenza)
    elif has_fever and cough_type in ["Dry", "Wet / productive"] and fatigue and not (sneezing and itchy_eyes):
        rules_triggered.append(
            "Fever + cough + fatigue → flu-like viral illness."
        )
        diagnosis = "Flu-like illness (Influenza or similar viral infection)"

    # Rule 3: COVID-like viral infection
    elif has_fever and cough_type == "Dry" and loss_of_smell:
        rules_triggered.append(
            "Fever + dry cough + loss of smell → COVID-like viral infection pattern."
        )
        diagnosis = "COVID-like viral infection pattern"

    # Rule 4: Common cold
    elif not has_fever and cough_type in ["Mild / occasional", "Dry"] and sore_throat and sneezing:
        rules_triggered.append(
            "No fever + mild/dry cough + sore throat + sneezing → common cold."
        )
        diagnosis = "Common cold / mild upper respiratory infection"

    # Rule 5: Allergic rhinitis / allergy
    elif not has_fever and sneezing and itchy_eyes and not cough_type == "Wet / productive":
        rules_triggered.append(
            "No fever + sneezing + itchy eyes → allergic rhinitis / allergy."
        )
        diagnosis = "Allergic rhinitis / allergy-related symptoms"

    # Rule 6: Asthma-like pattern
    elif wheezing and shortness_of_breath and (cough_type in ["Dry", "Mild / occasional"]):
        rules_triggered.append(
            "Wheezing + shortness of breath + dry/mild cough → asthma-like pattern."
        )
        diagnosis = "Asthma-like pattern / bronchospasm"

    # Rule 7: Chronic / prolonged symptoms
    elif long_duration and cough_type in ["Dry", "Wet / productive"]:
        rules_triggered.append(
            "Symptoms lasting more than 7 days with cough → chronic or unresolved respiratory issue; needs medical evaluation."
        )
        diagnosis = "Prolonged / chronic respiratory symptoms"

    # Rule 8: Non-specific viral infection
    elif has_fever and cough_type in ["Dry", "Wet / productive"]:
        rules_triggered.append(
            "Fever + cough without strong specific pattern → non-specific viral respiratory infection."
        )
        diagnosis = "Non-specific acute respiratory infection"

    # Fallback rule
    else:
        rules_triggered.append(
            "Pattern does not clearly match any rule → recommend medical consultation."
        )
        diagnosis = "Unclear pattern – consult a healthcare professional"

    explanation = "\n".join(f"- {r}" for r in rules_triggered)

    # Safety disclaimer
    disclaimer = (
        "This is NOT a medical diagnosis.\n"
        "This tool is for educational/demo purposes only."
    )

    return diagnosis, explanation, disclaimer


# -----------------------------
# Streamlit UI
# -----------------------------

def main():
    st.title("Respiratory Expert System 🩺")
    st.write(
        """
        A simple **rule-based expert system** for the **preliminary assessment** of common respiratory conditions.
        """
    )

    st.sidebar.header("Patient Information")

    # Basic info
    age = st.sidebar.number_input("Age (years)", min_value=0, max_value=120, value=25, step=1)
    temperature = st.sidebar.number_input("Body temperature (°C)", min_value=34.0, max_value=42.0, value=37.5, step=0.1)

    st.header("Symptoms")

    cough_type = st.selectbox(
        "Cough type",
        ["None", "Mild / occasional", "Dry", "Wet / productive"]
    )

    chest_pain = st.checkbox("Chest pain")
    sore_throat = st.checkbox("Sore throat")
    loss_of_smell = st.checkbox("Loss of smell / taste")
    wheezing = st.checkbox("Wheezing")
    shortness_of_breath = st.checkbox("Shortness of breath")
    sneezing = st.checkbox("Sneezing")
    itchy_eyes = st.checkbox("Itchy / watery eyes")
    fatigue = st.checkbox("Significant fatigue / body ache")

    phlegm_color = st.selectbox(
        "If you have phlegm, what color is it?",
        ["None", "Clear/White", "Yellow/Green", "Rusty/Bloody"]
    )

    duration_days = st.number_input(
        "Duration of symptoms (days)",
        min_value=0,
        max_value=60,
        value=3,
        step=1
    )

    if st.button("Run Expert System"):
        diagnosis, explanation, disclaimer = diagnose_respiratory_condition(
            age=age,
            temperature=temperature,
            cough_type=cough_type,
            chest_pain=chest_pain,
            sore_throat=sore_throat,
            loss_of_smell=loss_of_smell,
            wheezing=wheezing,
            shortness_of_breath=shortness_of_breath,
            sneezing=sneezing,
            itchy_eyes=itchy_eyes,
            phlegm_color=phlegm_color,
            duration_days=duration_days,
            fatigue=fatigue
        )

        st.subheader("Suggested Preliminary Interpretation")
        st.success(diagnosis)

        st.subheader("Reasoning (Rules Triggered)")
        st.markdown(explanation)

        st.subheader("Important Disclaimer")
        st.warning(disclaimer)

        st.markdown("---")
        st.caption(
            "Built as an educational expert system demo (rule-based inference, not a trained ML model)."
        )


if __name__ == "__main__":
    main()
