from PIL import Image
import os

image_dir = 'images'
pad_factors = {
    'Amany Elsedawy.png': 1.45,
    'Doaa Ahmed New_bg_removed.png': 1.15,
}
default_pad_factor = 1.15

for filename in os.listdir(image_dir):
    if not filename.endswith('.png'): continue
    path = os.path.join(image_dir, filename)
    factor = pad_factors.get(filename, default_pad_factor)
    
    try:
        img = Image.open(path)
        # Ensure image has an alpha channel
        img = img.convert("RGBA")
        width, height = img.size
        
        # We want to increase the canvas size without resizing the image
        new_width = int(width * factor)
        new_height = int(height * factor)
        
        new_img = Image.new("RGBA", (new_width, new_height), (0, 0, 0, 0))
        
        paste_x = (new_width - width) // 2
        # Align bottom of the portrait with the bottom of the canvas, adding 5% padding so it sits beautifully in the curve
        padding_bottom = int(height * 0.05)
        paste_y = new_height - height - padding_bottom
        
        new_img.paste(img, (paste_x, paste_y), img) # Use img as mask to ensure alpha is pasted correctly
        new_img.save(path)
        print(f"Padded {filename} by factor {factor}")
    except Exception as e:
        print(f"Error padding {filename}: {e}")
