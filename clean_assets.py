import pygame
import os

def clean_image(file_path):
    print(f"Processing {file_path}...")
    try:
        # Load image (convert to allow transparency)
        image = pygame.image.load(file_path).convert_alpha()
        width, height = image.get_size()
        
        # We assume the background is made of a checkerboard pattern
        # The two common colors are usually the top-left pixel and sometimes a neighbor
        # Let's sample a few corner pixels to find the "background colors"
        
        bg_colors = set()
        bg_colors.add(image.get_at((0, 0)))
        bg_colors.add(image.get_at((width-1, 0)))
        bg_colors.add(image.get_at((0, height-1)))
        bg_colors.add(image.get_at((width-1, height-1)))
        
        # Filter out obvious non-backgrounds (alpha == 0 is already good)
        bg_colors = {c for c in bg_colors if c.a != 0}
        
        if not bg_colors:
            print(f"Skipping {file_path}: Seems fully transparent or empty.")
            return

        print(f"Detected background candidates: {bg_colors}")

        new_image = pygame.Surface((width, height), pygame.SRCALPHA)
        
        # Simple pixel replacement
        # This is slow for large images but fine for assets
        for x in range(width):
            for y in range(height):
                pixel = image.get_at((x, y))
                if pixel in bg_colors:
                    new_image.set_at((x, y), (0, 0, 0, 0)) # Transparent
                else:
                    new_image.set_at((x, y), pixel)
                    
        # Save overwriting the original
        pygame.image.save(new_image, file_path)
        print(f"Saved cleaned {file_path}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def main():
    if not os.path.exists("assets"):
        print("Assets directory not found.")
        return

    pygame.init()
    # Need a display to use convert methods sometimes, though headless might work for image ops
    # We'll create a hidden one just in case
    pygame.display.set_mode((1, 1), pygame.NOFRAME | pygame.HIDDEN)

    for filename in os.listdir("assets"):
        if filename.lower().endswith(".png"):
            clean_image(os.path.join("assets", filename))
            
    pygame.quit()

if __name__ == "__main__":
    main()
