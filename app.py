from flask import Flask, render_template, request, jsonify
from key_detector import KeyDetector

app = Flask(__name__)
detector = KeyDetector()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    chord_progression = data.get('chords', '').split()
    
    # Clean the chords
    cleaned_chords = []
    for chord in chord_progression:
        clean_chord = chord.strip().replace(',', '').replace("'", '').replace('"', '')
        if clean_chord:
            cleaned_chords.append(clean_chord)
    
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

if __name__ == '__main__':
    app.run(debug=True) 