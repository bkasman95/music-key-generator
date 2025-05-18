# Music Key Detector

A web application that analyzes chord progressions to determine possible musical keys and their corresponding roman numeral progressions.

## Features

- Input chord progressions and get possible keys
- Support for both major and minor keys
- Shows roman numeral analysis for each possible key
- Handles all 12 major and minor keys
- Modern, responsive web interface
- Support for various chord notations (including flats and diminished chords)

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

## Deployment

This application is configured for deployment on Cloudflare Pages:

1. Push your code to GitHub:
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. In Cloudflare Pages:
   - Connect your GitHub repository
   - Set the build command: `pip install -r requirements.txt`
   - Set the build output directory: `.`
   - Set the Python version: `3.9`
   - Add environment variables if needed

## Project Structure

- `app.py`: Flask application
- `key_detector.py`: Key detection logic
- `chord_data.py`: Chord data loading and processing
- `templates/`: HTML templates
- `data/`: CSV files for chord data
- `requirements.txt`: Project dependencies
- `Procfile`: Production server configuration

## Contributing

Feel free to submit issues and enhancement requests! 