import streamlit as st
from PIL import Image
import os

# ===== Scene Mapping (Root-Level Files) =====
scene_images = {
    "Battle Mage": "lily_scene_battle_mage.png",
    "Soccer (Best)": "lily_best_soccer.png",
    "Soccer (Okay)": "lily_soccer_okay_not_great.jpg",
    "Warrior Pose": "lily_warrior_good.png"
}

# ===== UI Config =====
st.set_page_config(page_title="Pixar Scene Generator", layout="centered")
st.title("🎬 Pixar-Style Scene Generator")
st.write("Upload a symbolic photo and choose a scene to preview a Pixar-style illustration.")

# ===== Image Upload =====
uploaded_image = st.file_uploader("📤 Upload a symbolic photo", type=["jpg", "jpeg", "png"])
if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Photo", use_column_width=True)

# ===== Scene Selector =====
scene = st.selectbox("🎨 Choose a Scene", list(scene_images.keys()))

# ===== Generate Button =====
if st.button("✨ Generate Scene"):
    image_filename = scene_images.get(scene)
    image_path = image_filename  # root folder

    st.write(f"🔍 Looking for: `{image_filename}`")

    if os.path.exists(image_path):
        preview_image = Image.open(image_path)
        st.image(preview_image, caption=f"{scene}", use_column_width=True)
        with open(image_path, "rb") as f:
            st.download_button("📥 Download Image", f, file_name=image_filename)
    else:
        st.error("❌ Could not find the image in the project directory.")
