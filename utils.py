from PIL import Image, ImageDraw, ImageFont
import numpy as np
from PIL.Image import Resampling

class GradientTextureGenerator:
    def __init__(self, width=1024, height=1024, base_color=(255, 255, 255), noise_intensity_range=(0.01, 0.05)):
        self.width = width
        self.height = height
        self.base_color = base_color  # Base color for the gradient, default is white
        self.noise_intensity_range = noise_intensity_range

    def create_gradient(self):
        # Start with a base color array
        Z = np.full((self.height, self.width, 3), self.base_color, dtype=np.uint8)

        # Create a slight linear gradient
        for i in range(3):  # For each color channel
            gradient = np.linspace(0, 1, self.width) * 10  # Adjust the factor for the gradient effect
            Z[:, :, i] = np.clip(Z[:, :, i] - gradient[None, :], 0, 255).astype(np.uint8)

        # Add noise with varying intensity to each channel
        for i in range(3):  # For each color channel
            noise_intensity = np.random.uniform(*self.noise_intensity_range)
            noise = np.random.normal(0, noise_intensity * 255, (self.height, self.width))
            Z[:, :, i] = np.clip(Z[:, :, i] + noise, 0, 255).astype(np.uint8)

        return Z

    def get_pil_image(self, Z):
        try:
            # Create a PIL Image from the numpy array
            image = Image.fromarray(Z, 'RGB')
            return image
        except Exception as e:
            print(f"Error in creating PIL image: {e}")

            traceback.print_exc()

            return None

    def save_image(self, Z, file_path):
        """
        Save the generated gradient as an image using PIL.

        :param Z: The numpy array representing the gradient texture.
        :param file_path: Path to save the image.
        """
        # Convert the numpy array to an image and save it
        image = self.get_pil_image(Z)
        if image:
            image.save(file_path)