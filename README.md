
### Overview

This repository contains the **Courier 10 Pitch BT** font family in Type 1 format, derived from Xorg. It includes the original PostScript files and Python scripts to convert them into modern formats (OTF, WOFF2, TTF) for desktop and web use.

The font family includes 4 weights and styles. Each consists of a printer font file (`.pfb`) and an Adobe Font Metrics file (`.afm`):

| Style | PFB file | AFM file |
| :--- | :--- | :--- |
| **Roman** | c0419bt_.pfb | c0419bt_.afm |
| **Italic** | c0582bt_.pfb | c0582bt_.afm |
| **Bold** | c0583bt_.pfb | c0583bt_.afm |
| **Bold Italic** | c0611bt_.pfb | c0611bt_.afm |

The original source files are located in the [Type1/](./Type1/) directory.

### Prerequisites

The conversion scripts require `fontforge`. You can install it via your package manager:

```bash
# macOS or Linux if you installed homebrew
brew install fontforge
# Debian or Ubuntu
sudo apt install fontforge
# Arch Linux
sudo pacman -S fontforge
```

### Usage

```bash
# convert to otf (recommended)
python3 convert.py
# convert to woff2 (for web use)
python3 convert_web.py
# convert to ttf (for legacy compatibility)
python3 convert_ttf.py
```

or if you are using uv:

```bash
uv run convert.py
uv run convert_web.py
uv run convert_ttf.py
```

Outputs will be saved in the [dist/](./dist/) directory.

### Web Integration

Running `convert_web.py` generates the WOFF2 files. To use them on the web, remember to include the license info in your CSS, as shown in [`css/fonts.css`](./css/fonts.css).

### License

These fonts are provided under the Bitstream Charter Font License. See the [LICENSE](./Type1/LICENSE) file for details.

Additional PostScript Type 1 fonts can be found in sources like [Arch Linux Packages](https://archlinux.org/packages/extra/any/xorg-fonts-type1/).

