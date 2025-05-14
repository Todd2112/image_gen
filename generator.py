import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import io

# Load the model from Hugging Face Hub
@st.cache_resource
def load_model():
    model_id = "your-username/lily-model"  # <-- Replace with your actual model repo ID
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32
    )
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe

# Generate the image
def generate_image(pipe, prompt, num_steps, guidance_scale):
    result = pipe(
        prompt,
        num_inference_steps=num_steps,
        guidance_scale=guidance_scale,
        height=512,
        width=512
    )
    return result.images[0]

# UI Layout
st.title("🎨 Lily Pixar-Style Image Generator")

prompt = st.text_area("Prompt", 
    "Pixar-style image of Lily playing in a sunny backyard. Light reddish-blonde hair, large expressive eyes, "
    "symmetrical face, cheerful expression. Blue overalls, red shirt, cartoon grass and flowers, wooden fence. "
    "Warm lighting, bright colors, 3D cartoon style with whimsical proportions.")

num_steps = st.slider("Inference Steps", 1, 50, 30)
guidance_scale = st.slider("Guidance Scale", 1.0, 20.0, 7.5)

pipe = load_model()

if st.button("Generate Image"):
    with st.spinner("🧠 Thinking..."):
        image = generate_image(pipe, prompt, num_steps, guidance_scale)
        st.image(image, caption="Generated Image", use_column_width=True)

        # Convert image to in-memory byte stream
        img_bytes = io.BytesIO()
        image.save(img_bytes, format="PNG")
        img_bytes.seek(0)

        # Download button
        st.download_button(
            label="📥 Download Image",
            data=img_bytes,
            file_name="lily_pixar.png",
            mime="image/png"
        )
