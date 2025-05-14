import streamlit as st
from PIL import Image
from diffusers import StableDiffusionPipeline
import torch
import os

# Set up file paths
model_path = "model/lily_model_output"  # Adjust path if necessary
output_dir = "generated_images"
os.makedirs(output_dir, exist_ok=True)

# Load model (simplified version, reduced complexity)
@st.cache_resource
def load_model():
    try:
        pipe = StableDiffusionPipeline.from_pretrained(
            model_path,
            torch_dtype=torch.float32
        )
        pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
        return pipe
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Image generation function
def generate_image(pipe, uploaded_image):
    prompt = "Pixar-style cartoon of Lily with large expressive eyes, symmetrical face, and cheerful smile."
    try:
        result = pipe(
            prompt=prompt,
            num_inference_steps=20,
            guidance_scale=7.5,
            height=768,
            width=768
        )
        img = result.images[0]
        return img
    except Exception as e:
        st.error(f"Error generating image: {e}")
        return None

# Streamlit UI
def main():
    st.title("Lily Pixar-Style Image Generator")
    st.write("Upload a photo of Lily and generate a Pixar-style cartoon.")

    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        if st.button("Generate Pixar-Style Image"):
            pipe = load_model()
            if pipe:
                generated_image = generate_image(pipe, uploaded_image)
                if generated_image:
                    generated_image_path = os.path.join(output_dir, "generated_lily.png")
                    generated_image.save(generated_image_path)
                    st.image(generated_image, caption="Generated Pixar-style Image", use_column_width=True)
                    st.download_button(label="Download Image", data=generated_image_path, file_name="lily_pixar.png")

if __name__ == "__main__":
    main()
