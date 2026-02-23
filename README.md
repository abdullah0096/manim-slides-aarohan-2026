# Manim Slides — Aarohan 2026

> **Talk:** *Modern Cryptography, ECDLP & Quantum Computers — Present and Future*
> **Speaker:** Dr. Abdullah Ansari
> **Event:** Aarohan 2026 — DES PU, 23 February 2026
> **Department:** Department of Scientific Computing, Modeling and Simulation, SPPU

▶ **Full presentation video:** [https://www.youtube.com/watch?v=xirQ3nqCptE](https://www.youtube.com/watch?v=xirQ3nqCptE)

---

## Table of Contents

1. [Slides Overview](#slides-overview)
2. [Project Structure](#project-structure)
3. [Dependencies & Installation](#dependencies--installation)
4. [Rendering (Compiling) the Slides](#rendering-compiling-the-slides)
5. [Presenting with manim-slides](#presenting-with-manim-slides)
6. [Converting to HTML](#converting-to-html)
7. [Distributing to Another Machine](#distributing-to-another-machine)
8. [LastSlide — Animation Notes](#lastslide--animation-notes)
9. [License](#license)

---

## Slides Overview

The presentation consists of **13 slides** (Manim `Slide` classes), all defined in
[`aarohan_main.py`](aarohan_main.py) (plus helpers in
[`cryptologySlide.py`](cryptologySlide.py), [`piryamid.py`](piryamid.py) and
[`utils.py`](utils.py)).

| # | Class | Description |
|---|-------|-------------|
| 1 | `Title` | Opening title card — animates the talk title *"Modern Cryptography, ECDLP & Quantum Computers"*, speaker name, event name, and date. Contains a looping entry animation. |
| 2 | `Introduction` | Sets the scale of the digital world — 6 billion+ internet users, 20 billion+ connected devices, YouTube (2.7B users), Meta platforms (3.9B users) — motivating why cryptography matters. |
| 3 | `InsecureChannel` | Illustrates the classic Alice → Server → Bob communication model using WhatsApp as an example. Shows why a public channel is inherently insecure and introduces the need for encryption. |
| 4 | `EncDec` | Explains the core ideas of Encryption and Decryption through a simple Caesar-cipher walkthrough: `HELLO` → scramble → `KHOOR` → unscramble → `HELLO`. Introduces the concept of a key. |
| 5 | `Cryptology` | Animated top-down tree of the full field of Cryptology. The camera zooms into the **Cryptography** sub-tree (Public Key, Private Key, Digital Signatures, Hashing, Advanced Topics with leaves) and then into the **Cryptanalysis** sub-tree (Classical, Symmetric, Asymmetric, Side-Channel attacks). Ends with the equation *Cryptology = Cryptography + Cryptanalysis* and transitions focus to Public Key Cryptography. |
| 6 | `OneWayFunction` | Explains one-way functions as the mathematical foundation of Public Key Cryptography. Shows the three hard problems: **DLP** (Discrete Logarithm Problem), **IFP** (Integer Factorisation Problem), and **ECC** (Elliptic Curve Cryptography). |
| 7 | `ECDLP` | Introduces Elliptic Curves — the equation $\mathcal{E}: y^2 = x^3 + ax + b$ — plots the curve $y^2 = x^3 - 3x + 3$ on a coordinate plane, demonstrates the group law, and shows point addition geometrically. |
| 8 | `DoubleAndAdd` | Explains the **Double-and-Add** algorithm for efficiently computing the scalar multiple $mP$ on an elliptic curve. Uses the binary representation of $m$ (example: $9 = (1001)_2$) to illustrate the steps and derives the $O(\log_2 m)$ complexity. |
| 9 | `ECDLP2` | Contrasts the *easy* direction ($mP = Q$ given $m$ and $P$, which is fast via Double-and-Add) with the *hard* inverse problem — the ECDLP: given $P$ and $Q$, find $m$. Shows why this asymmetry is the security foundation of ECC. |
| 10 | `ECDLP3` | Surveys real-world applications of ECC: WhatsApp End-to-End Encryption, UPI / Google Pay / PhonePe, Cryptocurrencies (Bitcoin, Ethereum), SSL/TLS / HTTPS. Concludes with a pyramid diagram linking Elliptic Curve Cryptography to ECDLP. |
| 11 | `CryptoPyramid` | The *big picture* animated pyramid with five tiers: **Math** (ECDLP/DLP/IFP) → **Hardness Assumptions** → **Algorithms** (ECDH, ECDSA, RSA, …) → **Protocols** (TLS, Signal, …) → **Applications** (HTTPS, Banking, …). The camera zooms into each tier in sequence. |
| 12 | `QuantumThreat` | Covers the quantum threat to current cryptography. Sub-slides include: quantum computer introduction, exponential vs polynomial complexity, key-security table (AES-128/256, RSA, ECC vs quantum), HNDL (*Harvest Now, Decrypt Later*) attack timeline, cryptographic shelf-life, and the NIST Post-Quantum Cryptography (PQC) standards table. |
| 13 | `LastSlide` | Closing *"Questions?"* slide. Features a continuously looping generative mathematical animation (see [LastSlide — Animation Notes](#lastslide--animation-notes) below). |

---

## Project Structure

```
aarohanSlides/
├── aarohan_main.py        # All 13 slide classes
├── cryptologySlide.py     # Helper functions for the Cryptology tree slide
├── piryamid.py            # Helper functions for the CryptoPyramid slide
├── utils.py               # Shared utilities (colours, fonts, etc.)
├── compile_all.sh         # Render all slides with manim
├── run_all.sh             # Present all slides with manim-slides
├── convert_all.sh         # Convert slides to self-contained HTML
├── requirement.txt        # Python package dependencies
├── INSTALL                # System-level installation notes
├── images/                # SVG / PNG image assets used in animations
├── slides/                # JSON metadata files produced by manim-slides
│   └── files/             # Symlinked / copied video segments
└── media/                 # Rendered video output from manim
    └── videos/
```

---

## Dependencies & Installation

### 1 — System packages (Ubuntu / Debian)

```bash
sudo apt update
sudo apt install -y \
  python3 python3-pip python3-venv \
  ffmpeg \
  libcairo2-dev \
  libpango1.0-dev \
  libpangocairo-1.0-0 \
  pkg-config \
  texlive-latex-base \
  texlive-latex-extra \
  texlive-fonts-extra \
  texlive-fonts-recommended \
  texlive-latex-recommended \
  texlive-science \
  dvisvgm \
  sox \
  fonts-rajdhani
```

> **Note:** `dvisvgm` is required by manim-slides for LaTeX → SVG conversion.
> `fonts-rajdhani` is used in the `LastSlide` animation labels.
> If the package is not available via `apt`, install it manually:
>
> ```bash
> wget https://github.com/google/fonts/raw/main/ofl/rajdhani/Rajdhani-Regular.ttf
> mkdir -p ~/.local/share/fonts
> mv Rajdhani-Regular.ttf ~/.local/share/fonts/
> fc-cache -f -v
> ```

### 2 — Python virtual environment

```bash
python3 -m venv manim-env
source manim-env/bin/activate
```

### 3 — Install Python packages

```bash
pip install --upgrade pip wheel setuptools
pip install -r requirement.txt
```

`requirement.txt` pins the following key packages:

| Package | Version | Purpose |
|---------|---------|---------|
| `manim` | 0.19.1 | Core animation engine |
| `manim-slides` | 5.1.3 | Interactive slide presenter |
| `av` | 12.0.0 | Video backend (must be binary-compatible with manim-slides) |
| `numpy` | latest | Scientific computing |
| `scipy` | ≥ 1.10 | Used internally by manim |
| `pillow` | ≥ 10.0 | Image handling |
| `pycairo` | ≥ 1.23 | Cairo rendering backend |
| `manimpango` | ≥ 0.6.0 | Pango text rendering |

To eliminate flickering between slides, optionally install the PySide6 backend:

```bash
pip install manim-slides[pyside6]
# or
pip install PySide6
```

---

## Rendering (Compiling) the Slides

All slides are rendered in a single command. The `-qk` flag renders at **4K quality**.

```bash
# Activate the virtual environment first
source manim-env/bin/activate

# Render all slides (4K)
time manim render aarohan_main.py -qk \
    Title Introduction InsecureChannel EncDec \
    Cryptology OneWayFunction ECDLP DoubleAndAdd \
    ECDLP2 ECDLP3 CryptoPyramid QuantumThreat LastSlide
```

Or use the provided convenience script:

```bash
bash compile_all.sh
```

> **Quality flags:**
> | Flag | Quality | Resolution |
> |------|---------|------------|
> | `-ql` | Low | 480p |
> | `-qm` | Medium | 720p |
> | `-qh` | High | 1080p |
> | `-qk` | 4K | 2160p |
>
> Use `-qh` for faster test renders during development.

Rendered videos are saved under `media/videos/aarohan_main/<quality>/`.

---

## Presenting with manim-slides

Once rendered, present the slides interactively:

```bash
manim-slides present \
    Title Introduction InsecureChannel EncDec \
    Cryptology OneWayFunction ECDLP DoubleAndAdd \
    ECDLP2 ECDLP3 CryptoPyramid QuantumThreat LastSlide \
    --fullscreen --hide-info-window
```

Or use the convenience script:

```bash
bash run_all.sh
```

**Keyboard controls during presentation:**

| Key | Action |
|-----|--------|
| `→` / `Space` | Next slide |
| `←` | Previous slide |
| `F` | Toggle fullscreen |
| `Q` / `Esc` | Quit |

---

## Converting to HTML

Produce a single self-contained HTML file (suitable for sharing or browser-based presentation):

```bash
manim-slides convert \
    Title Introduction InsecureChannel EncDec \
    Cryptology OneWayFunction ECDLP DoubleAndAdd \
    ECDLP2 ECDLP3 CryptoPyramid QuantumThreat LastSlide \
    final_aarohan_slides.html
```

Or:

```bash
bash convert_all.sh
```

This generates:
- `final_aarohan_slides.html` — the main HTML file
- `final_aarohan_slides_assets/` — directory containing embedded video segments

---

## Distributing to Another Machine

### Option A — HTML (browser, no manim-slides required)

Copy **both** of the following to the target machine:

```
final_aarohan_slides.html
final_aarohan_slides_assets/         ← entire directory
```

Open `final_aarohan_slides.html` in any modern browser. No installation required.

> Keep the `.html` file and `_assets/` folder **in the same directory**.
> The HTML file references the assets folder by relative path.

---

### Option B — Video files + manim-slides (full presenter experience)

Copy the following directories to the target machine:

```
slides/                              ← JSON metadata + file references
media/                               ← rendered video segments
```

On the target machine, install manim-slides:

```bash
pip install manim-slides==5.1.3
```

Then present:

```bash
manim-slides present \
    Title Introduction InsecureChannel EncDec \
    Cryptology OneWayFunction ECDLP DoubleAndAdd \
    ECDLP2 ECDLP3 CryptoPyramid QuantumThreat LastSlide \
    --fullscreen --hide-info-window
```

> The `slides/*.json` files point to video paths inside `media/`. Both directories
> must be present and their relative paths must be preserved.

---

## LastSlide — Animation Notes

The `LastSlide` class is the closing *"Questions?"* slide and contains a rich,
looping generative animation driven entirely by number theory.

### Structure

The slide has three logical phases that loop indefinitely until the presenter
advances:

| Phase | What you see |
|-------|-------------|
| **Phase 1 — Modular Multiplication Spiral** | `N` points are placed evenly on a circle. Each point `k` is connected to point `(M × k) mod N` by a line. As `N` and `M` animate through a sequence of waypoints, the chord diagram morphs continuously through striking geometric patterns: binary star, trefoil knot, mandala burst, golden-ratio sunflower (Fibonacci, $M ≈ 137°$), daisy, and 5-fold symmetry. Lines are coloured along a gold gradient. |
| **Phase 2 — Prime Filter** | The same chord diagram fades to show only connections where `k` is a **prime number**. Prime chords glow brightly in gold; composite chords dim to near-invisible. The pattern morphs through additional prime-only constellations and a dense prime weave. |
| **Phase 3 — Ulam Spiral** | The chord diagram crossfades to the **Ulam Spiral** — a square spiral arrangement of integers where **prime positions are highlighted in bright gold** and composites are dim. The camera breathes in and out while the spiral is displayed for ~22 seconds before crossfading back to the chord diagram. |
| **Phase 4 — Reset** | The animation smoothly returns to the Phase 1 start state for a seamless loop restart. |

Throughout all phases, a `QUESTIONS?` banner (set in *Cinzel* typeface, gold) is
anchored at the bottom of the screen, and a small mathematical label in the corner
shows the current values of `N` and `M` (e.g. `k → 137k mod 300`).

### Key parameters (tweakable)

```python
RADIUS    = 3.0       # chord circle radius
NUM_LINES = 220       # number of chord lines drawn
SEG_NORMAL = 9.0      # seconds per waypoint in Phase 1
SEG_PRIME  = 11.0     # seconds per waypoint in Phase 2
ULAM_HOLD  = 22.0     # seconds the Ulam spiral is displayed
ULAM_N     = 361      # number of integers in the Ulam spiral (19×19 grid)
ZOOM_AMT   = 0.18     # camera zoom depth (±18 %)
```

---

## License

This project is released under the **MIT License** — see [`LICENSE`](LICENSE) for details.