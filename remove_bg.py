import os
import sys

try:
    from rembg import remove
except ImportError:
    print("rembg is not installed. Please install it first.")
    sys.exit(1)

image_dir = 'images'
for filename in os.listdir(image_dir):
    if filename.lower().endswith('.jpeg') or filename.lower().endswith('.jpg'):
        input_path = os.path.join(image_dir, filename)
        # Create output path with .png extension
        output_path = os.path.join(image_dir, filename.rsplit('.', 1)[0] + '.png')
        
        print(f"Processing {input_path}...")
        try:
            with open(input_path, 'rb') as i:
                input_data = i.read()
                output_data = remove(input_data)
            
            with open(output_path, 'wb') as o:
                o.write(output_data)
            print(f"Saved {output_path}")
        except Exception as e:
            print(f"Error processing {input_path}: {e}")

print("Background removal complete.")
