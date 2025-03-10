import streamlit as st
import re

# --- Password strength checker ---
def password_strength(password):
    length_criteria = len(password) >= 8
    lower_criteria = re.search(r"[a-z]", password) is not None
    upper_criteria = re.search(r"[A-Z]", password) is not None
    digit_criteria = re.search(r"\d", password) is not None
    special_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    score = sum([length_criteria, lower_criteria, upper_criteria, digit_criteria, special_criteria])

    if score <= 2:
        return "Weak", "🔴"
    elif score == 3 or score == 4:
        return "Moderate", "🟡"
    else:
        return "Strong", "🟢"

# --- Detailed password validation ---
def validate_password(password):
    messages = []

    if len(password) < 8:
        messages.append("❌ Minimum length is 8 characters")
    if not re.search(r"[a-z]", password):
        messages.append("❌ Add at least one lowercase letter")
    if not re.search(r"[A-Z]", password):
        messages.append("❌ Add at least one uppercase letter")
    if not re.search(r"\d", password):
        messages.append("❌ Add at least one number")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        messages.append("❌ Add at least one special character")

    if not messages:
        return True, "✅ Password meets all the best practices!"
    else:
        return False, "\n".join(messages)

# --- Streamlit UI ---
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")

st.title("🔐 Password Strength Meter")

# Password input field
password = st.text_input("Enter your password", type="password")

# Check password only if input is not empty
if password:
    # Evaluate strength
    strength, icon = password_strength(password)
    st.markdown(f"### Strength: {icon} **{strength}**")

    # Perform validation checks
    valid, message = validate_password(password)
    st.markdown(message)

    # Suggestions if password is not strong yet
    if strength != "Strong":
        st.info("""
        **Suggestions to improve your password:**
        - Use at least 8 characters
        - Mix uppercase and lowercase letters
        - Include numbers and special characters
        - Avoid common words or patterns
        """)
else:
    st.warning("Please enter a password to check its strength!")

# Footer / Credits (optional)
st.caption("Made with ❤️ Basit Ali")
