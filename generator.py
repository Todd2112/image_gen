import streamlit as st
from PIL import Image
import os

# ===== Scene Image Mapping (only files that exist) =====
scene_images = {
    "Battle Mage (Final Scene)": "lily_scene_battle_mage.png",
    "Soccer (Best Shot)": "lily_best_soccer.png",
    "Soccer (Okay/Not Great)": "lily_soccer_okay_not_great.jpg",
    "Warrior Pose (Good)": "lily_warrior_good.png"
}

# ===== UI Layout =====
st.set_page_config(page_title="Lily Pixar Scene Generator", layout="centered")
st.title("🎬 Lily Pixar-Style Scene Generator")
st.write("Upload a symbolic photo of Lily and choose a Pixar-style scene to preview.")

# ===== Upload Photo =====
uploaded_file = st.file_uploader("📤 Upload a photo of Lily (symbolic only)", type=["jpg", "png", "jpeg"])
if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Photo", use_column_width=True)

# ===== Scene Selector =====
scene = st.selectbox("🎨 Choose a Scene", list(scene_images.keys()))

# ===== Generate Button =====
if st.button("✨ Generate Scene"):
    image_filename = scene_images.get(scene)
    image_path = os.path.join("static", image_filename)

    st.write("🔍 Looking for image at:", image_path)

    if os.path.exists(image_path):
        image = Image.open(image_path)
        st.image(image, caption=f"{scene}", use_column_width=True)
        with open(image_path, "rb") as img_file:
            st.download_button("📥 Download Image", img_file, file_name=image_filename)
    else:
        st.error(f"❌ Image not found at path: {image_path}")
