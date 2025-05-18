# Music Key Generator

A web app that analyzes chord progressions and suggests possible musical keys. Supports major and minor keys, flat and sharp notation, and various diminished chord notations (e.g., mb5, m-5, dim).

## ⚠️ Deployment Notice

**Cloudflare Pages and Cloudflare Workers do NOT support Python/Flask applications.**

For Python web apps like this one, we recommend using [Render.com](https://render.com/) for deployment. Render.com offers a free tier and is straightforward for Flask apps.

## 🚀 Deploying on Render.com

1. **Push your code to GitHub.**
2. **Sign up or log in** at [https://render.com/](https://render.com/).
3. Click **"New +"** and select **"Web Service"**.
4. Connect your GitHub repository.
5. Fill in the service details:
   - **Name:** music-key-generator
   - **Environment:** Python
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
   - **Python Version:** 3.9 (set in environment variables or render.yaml)
   - **Plan:** Free
6. Click **Create Web Service** and wait for the build and deploy to finish.

## Usage
- Enter a chord progression (e.g., `C Em G` or `Cm Dmb5 Fm`).
- The app will suggest possible keys.
- Diminished chords can be entered as `mb5`, `m-5`, or `dim` (e.g., `Dmb5`, `Dm-5`, `Ddim`).

## Project Structure
- `app.py` — Flask web app
- `chord_data.py` — Chord normalization and CSV loading
- `key_detector.py` — Key detection logic
- `data/major_keys.csv` and `data/minor_keys.csv` — Chord data
- `render.yaml` — Render.com deployment config

## Development
1. Clone the repo and install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Run locally:
   ```sh
   python app.py
   ```

---

**Cloudflare is not supported for this project. Use Render.com for best results.**

## Features

- Input chord progressions and get possible keys
- Support for both major and minor keys
- Shows roman numeral analysis for each possible key
- Handles 14 major keys and 13 minor keys (including enharmonic equivalents)
- Modern, responsive web interface
- Support for various chord notations:
  - Flats (e.g., Eb, Bb)
  - Diminished chords (mb5, m-5, or dim)
  - Minor chords (m)
  - Major chords (no suffix)

## Local Development

1. Clone the repository:
```bash
git clone [your-repo-url]
cd music-key-generator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
python app.py
```

5. Open http://localhost:5000 in your browser

## Usage Examples

Enter chord progressions using any of these notations:
```
C Em G           # Basic major/minor chords
Eb Ab Bb         # Flats
Dm F Bmb5        # Diminished chord (mb5)
Dm F Bm-5        # Diminished chord (m-5)
Dm F Bdim        # Diminished chord (dim)
```

## Project Structure

- `app.py`: Flask application
- `key_detector.py`: Key detection logic
- `chord_data.py`: Chord data loading and processing
- `templates/`: HTML templates
- `data/`: CSV files for chord data
- `requirements.txt`: Project dependencies
- `render.yaml`: Render.com configuration

## Contributing

Feel free to submit issues and enhancement requests! 