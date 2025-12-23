import pygame

def make_transparent(image, bg_color=None, tolerance=30):
    """
    Makes the background of an image transparent.
    If bg_color is None, it uses the top-left pixel color.
    tolerance allows for slight variations in background color.
    """
    image = image.convert_alpha()
    if bg_color is None:
        bg_color = image.get_at((0, 0))
        
    width, height = image.get_size()
    
    # Lock the surface for faster pixel access
    # Note: In newer pygame versions, pixel access via get_at/set_at is slow, 
    # but for small sprites at startup it's acceptable.
    # For better performance we could use PixelArray but we need to be careful with locking.
    
    for x in range(width):
        for y in range(height):
            c = image.get_at((x, y))
            # Calculate difference
            diff = abs(c[0] - bg_color[0]) + abs(c[1] - bg_color[1]) + abs(c[2] - bg_color[2])
            if diff <= tolerance:
                image.set_at((x, y), (0, 0, 0, 0)) # Set to fully transparent
                
    return image
