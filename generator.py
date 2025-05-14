import streamlit as st
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import os

# Function to load the model
@st.cache_resource
def load_model():
    model_path = "C:/Users/realt/Work for Peter/lily_model_output"
    pipe = StableDiffusionPipeline.from_pretrained(
        model_path,
        torch_dtype=torch.float32
    )
    pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    return pipe

# Function to generate the image based on the prompt
def generate_image(pipe, prompt, num_steps, guidance_scale):
    result = pipe(
        prompt,
        num_inference_steps=num_steps,
        guidance_scale=guidance_scale,
        height=768,
        width=768
    )
    image = result.images[0]
    return image

# Streamlit UI
st.title("Lily Pixar-Style Image Generator")

# User inputs for the prompt, steps, and guidance scale
prompt = st.text_area("Enter your prompt", 
                      "Pixar-style image of Lily playing in a sunny backyard with strawberry blonde hair, large expressive eyes, "
                      "symmetrical face, and a cheerful expression. Wearing blue overalls and a red shirt, surrounded by cartoon grass, "
                      "flowers, and a wooden fence. Soft afternoon lighting with whimsical proportions and vibrant colors. "
                      "3D cartoon style with high detail.")

num_steps = st.slider("Number of Inference Steps", min_value=1, max_value=50, value=30, step=1)
guidance_scale = st.slider("Guidance Scale", min_value=1.0, max_value=20.0, value=7.5, step=0.1)

# Load the model
pipe = load_model()

# Button to generate the image
if st.button("Generate Image"):
    st.spinner("Generating image...")  # Show a loading spinner while generating
    image = generate_image(pipe, prompt, num_steps, guidance_scale)
    
    # Display the result
    st.image(image, caption="Generated Image", use_column_width=True)
    
    # Option to save the image
    save_button = st.button("Save Image")
    if save_button:
        image_path = os.path.join("C:/Users/realt/Work for Peter/training_output/generated_lily_tests", "generated_lily.png")
        image.save(image_path)
        st.success(f"Image saved to {image_path}")
