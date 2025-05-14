import gradio as gr
from PIL import Image
import os

# ===== Static Scene Mapping =====
scene_images = {
    "Battle Mage": "lily_scene_battle_mage.png",
    "Soccer": "lily_best_soccer.png",  # Remove duplicate keys
    "Warrior Pose": "lily_warrior_good.png"
}

def generate_scene(uploaded_image, scene):
    if not uploaded_image:
        return None, "❌ No uploaded image provided."

    image_filename = scene_images.get(scene)
    image_path = os.path.join("static", image_filename)

    if os.path.exists(image_path):
        preview_image = Image.open(image_path)
        return preview_image, f"✅ Scene: {scene}"
    else:
        return None, "❌ Scene image not found in 'static/' directory."

# ===== Gradio Interface =====
scene_choices = list(scene_images.keys())

demo = gr.Interface(
    fn=generate_scene,
    inputs=[
        gr.Image(type="pil", label="📤 Upload a symbolic photo"),
        gr.Dropdown(choices=scene_choices, label="🎨 Choose a Scene")
    ],
    outputs=[
        gr.Image(type="pil", label="🎬 Generated Scene"),
        gr.Textbox(label="ℹ️ Status")
    ],
    title="Pixar-Style Scene Generator",
    description="Upload a symbolic photo and choose a scene to preview a Pixar-style illustration."
)

if __name__ == "__main__":
    demo.launch()
