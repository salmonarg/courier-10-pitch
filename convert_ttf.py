import os
import subprocess

def convert_type1_to_ttf(input_pfb, output_ttf):
    # convert pfb to ttf using fontforge
    print(f"Converting {input_pfb} to {output_ttf}...")
    try:
        subprocess.run([
            "fontforge", "-lang=py", "-c", 
            f"import fontforge; font = fontforge.open('{input_pfb}'); font.generate('{output_ttf}')"
        ], check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_pfb} with fontforge: {e.stderr.decode()}")

if __name__ == "__main__":
    bt_dir = "Type1"
    output_dir = "dist"
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    fonts = [
        "c0419bt_", # Courier10PitchBT-Roman
        "c0582bt_", # Courier10PitchBT-Italic
        "c0583bt_", # Courier10PitchBT-Bold
        "c0611bt_"  # Courier10PitchBT-BoldItalic
    ]

    for base_name in fonts:
        pfb = os.path.join(bt_dir, base_name + ".pfb")
        ttf = os.path.join(output_dir, base_name + ".ttf")
        
        if os.path.exists(pfb):
            convert_type1_to_ttf(pfb, ttf)
        else:
            print(f"File not found: {pfb}")
