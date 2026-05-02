# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "Pillow",
#     "fonttools",
# ]
# ///

import os
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont

"""
Courier 10 Pitch BT Showcase Generator
--------------------------------------
You can adjust the parameters in the 'create_showcase' function to 
fine-tune the layout and spacing.

Run this script using:
    uv run gen-showcase.py
"""

def get_font_characters(font_path):
    """Extracts available Unicode characters from the font file."""
    ttfont = TTFont(font_path)
    chars = []
    for table in ttfont['cmap'].tables:
        if table.isUnicode():
            chars.extend(table.cmap.keys())
    return sorted(list(set(chars)))

def create_showcase(font_path, output_path):
    print(f"Generating showcase for {font_path}...")
    chars = get_font_characters(font_path)
    
    # Exclude control characters (0-31 and 127-159)
    display_chars = [c for c in chars if not (c < 32 or (127 <= c <= 159))]
    
    # --- ADJUST THESE PARAMETERS ---
    cols = 16          # Characters per row
    font_size = 42     # Font size in pixels
    cell_width = 80    # Width of each character cell
    cell_height = 100  # Height of each character cell
    margin = 50        # Padding around the entire grid
    # -------------------------------
    
    rows = (len(display_chars) + cols - 1) // cols
    width = cols * cell_width + margin * 2
    height = rows * cell_height + margin * 2
    
    # Create white background image
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype(font_path, font_size)
    except Exception as e:
        print(f"Error loading font {font_path}: {e}")
        return

    for i, codepoint in enumerate(display_chars):
        char = chr(codepoint)
        
        row = i // cols
        col = i % cols
        
        # Calculate the center of the cell for horizontal, and a fixed baseline for vertical
        cell_center_x = margin + col * cell_width + cell_width / 2
        cell_center_y = margin + row * cell_height + cell_height / 2
        
        # 'ms' anchor:
        # m = horizontal middle
        # s = baseline (standard alignment)
        # We shift cell_center_y slightly to make the baseline look vertically centered in the cell
        draw.text((cell_center_x, cell_center_y + font_size / 4), char, font=font, fill='black', anchor='ms')

    img.save(output_path)
    print(f"Successfully saved to {output_path}")

def main():
    # Mapping of source TTF files to output showcase images
    fonts = [
        ("dist/c0419bt_.ttf", "showcase/c0419bt_.png"),
        ("dist/c0582bt_.ttf", "showcase/c0582bt_.png"),
        ("dist/c0583bt_.ttf", "showcase/c0583bt_.png"),
        ("dist/c0611bt_.ttf", "showcase/c0611bt_.png"),
    ]
    
    os.makedirs("showcase", exist_ok=True)
    
    for font_path, out_path in fonts:
        if os.path.exists(font_path):
            create_showcase(font_path, out_path)
        else:
            print(f"Warning: Font file not found: {font_path}. Please run convert_ttf.py first.")

if __name__ == "__main__":
    main()
