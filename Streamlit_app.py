import streamlit as st
import openai

# -------------------------------------------------
# 🔑 SETUP
# Paste your API key here (replace with your real key)
openai.api_key = "YOUR_API_KEY"
# -------------------------------------------------

# Streamlit Page Setup
st.set_page_config(page_title="AI Product Copy Generator", layout="wide")
st.title("🛍️ AI Product Description & Ad Copy Generator")
st.markdown("Boost your eCommerce sales with AI-powered product descriptions & ad copy.")

# User Inputs
product_name = st.text_input("📦 Enter Product Name")
features = st.text_area("✨ Enter Product Features (comma separated)")
tone = st.selectbox("🎭 Choose Tone", ["Professional", "Friendly", "Luxury", "Casual", "Funny"])
length = st.slider("📝 Length of Description (words)", 50, 300, 120)

# Generate Button
if st.button("🚀 Generate Copy"):
    if product_name.strip() == "" or features.strip() == "":
        st.error("⚠️ Please enter both product name and features.")
    else:
        with st.spinner("⏳ Generating your AI copy..."):
            prompt = f"""
            Write a {tone} eCommerce product description and ad copy.
            Product: {product_name}
            Features: {features}
            Length: {length} words.
            Optimize for SEO, make it persuasive, and include a catchy ad copy.
            """
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # Upgrade to gpt-4 if available
                    messages=[{"role": "user", "content": prompt}]
                )
                output = response['choices'][0]['message']['content']
                st.success("✅ Generated Copy")
                st.write(output)
            except Exception as e:
                st.error(f"❌ Error: {e}")
