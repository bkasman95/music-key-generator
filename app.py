from flask import Flask, render_template, request, jsonify
from key_detector import KeyDetector
import os

app = Flask(__name__)
detector = KeyDetector()

# Define valid chords (should match frontend options)
VALID_CHORDS = set([
    # Major, minor, dim
    *(root + t for root in ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"] for t in ["", "m", "dim"]),
    # mb5, m-5
    *(root + "mb5" for root in ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"]),
    *(root + "m-5" for root in ["C", "C#", "Db", "D", "D#", "Eb", "E", "F", "F#", "Gb", "G", "G#", "Ab", "A", "A#", "Bb", "B"]),
])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    chord_progression = data.get('chords', '').split()
    print('Received chords:', chord_progression)
    # Clean the chords
    cleaned_chords = []
    for chord in chord_progression:
        clean_chord = chord.strip().replace(',', '').replace("'", '').replace('"', '')
        if clean_chord:
            cleaned_chords.append(clean_chord)
    print('Cleaned chords:', cleaned_chords)
    # Validate chords
    if not cleaned_chords or not all(chord in VALID_CHORDS for chord in cleaned_chords):
        return jsonify({'error': 'Please enter a valid chord.'})
    # Find possible keys
    possible_keys = detector.find_possible_keys(cleaned_chords)
    
    # Format the results
    results = []
    for key, progression in possible_keys.items():
        key_result = {
            'key': key,
            'progression': [{'chord': chord, 'roman': roman} for chord, roman in progression.items()]
        }
        results.append(key_result)
    
    return jsonify({'results': results})

# For local development
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 