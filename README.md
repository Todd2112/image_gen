# 🎬 Pixar-Style Scene Generator

A lightweight, proof-of-concept Streamlit app that demonstrates consistent character rendering across multiple Pixar-style scenes using pre-generated images.

---

## 🧠 What It Does

- 📤 Symbolic photo upload (no live training or customization)
- 🎨 Choose from pre-rendered scenes:
  - Battle Mage
  - Soccer
  - Warrior Pose
  - More coming soon...
- 🖼️ View consistent 3D cartoon-style illustrations with expressive character design
- 📥 Download the selected image with one click

---

## 🧪 Tech Stack

- **Streamlit** – clean, minimal frontend UI
- **DreamBooth + Stable Diffusion 1.5** – used offline to generate all images
- **ControlNet** – used to lock pose and structure
- **Pre-generated Images Only** – no runtime inference or model hosting required

---

## 🚀 Deployment Notes

This project is designed for Hugging Face Spaces or Streamlit Cloud.  
Runtime requirements are minimal:

```txt
streamlit
Pillow
