import streamlit as st
from PIL import Image
import os

# ===== Static Scene Mapping =====
scene_images = {
    "Battle Mage (Final Scene)": "lily_scene_battle_mage.png",
    "Soccer (Best Shot)": "lily_best_soccer.png",
    "Soccer (Okay/Not Great)": "lily_soccer_okay_not_great.jpg",
    "Warrior Pose (Good)": "lily_warrior_good.png"
}

st.set_page_config(page_title="Lily Pixar Scene Generator", layout="centered")
st.title("🎬 Lily Pixar-Style Scene Generator")
st.write("Upload a symbolic photo of Lily and choose a scene to preview a Pixar-style illustration.")

# ===== Upload Image Placeholder =====
uploaded_file = st.file_uploader("📤 Upload a photo of Lily (symbolic only)", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Photo", use_column_width=True)

# ===== Scene Selector =====
scene = st.selectbox("🎨 Choose a Scene", list(scene_images.keys()))

# ===== Generate Button =====
if st.button("✨ Generate Scene"):
    image_filename = scene_images[scene]
    image_path = os.path.join("static", image_filename)

    st.write(f"🔍 Looking for: `{image_path}`")

    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption=f"{scene}", use_column_width=True)
        with open(image_path, "rb") as file:
            st.download_button("📥 Download Image", file, file_name=image_filename)
    else:
        st.error("❌ Could not find the image in the 'static/' directory.")
