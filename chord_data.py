import csv
from pathlib import Path

def load_chord_data(major_csv_path, minor_csv_path):
    """
    Load chord progression data from CSV files.
    
    Args:
        major_csv_path (str): Path to the major keys CSV file
        minor_csv_path (str): Path to the minor keys CSV file
        
    Returns:
        tuple: (major_chords_dict, minor_chords_dict)
    """
    major_chords = {}
    minor_chords = {}
    
    # Load major keys data
    with open(major_csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = row['Key']
            major_chords[key] = {
                'I': normalize_chord(row['I']),
                'ii': normalize_chord(row['ii']),
                'iii': normalize_chord(row['iii']),
                'IV': normalize_chord(row['IV']),
                'V': normalize_chord(row['V']),
                'vi': normalize_chord(row['vi*']),  # Note the * in the column name
                'vii': normalize_chord(row['vii'])
            }
    
    # Load minor keys data
    with open(minor_csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = row['Key']
            minor_chords[key] = {
                'i': normalize_chord(row['i']),
                'ii': normalize_chord(row['ii']),
                'III': normalize_chord(row['III']),
                'iv': normalize_chord(row['iv']),
                'v': normalize_chord(row['v']),
                'VI': normalize_chord(row['VI']),
                'VII': normalize_chord(row['VII'])
            }
    
    return major_chords, minor_chords

def normalize_chord(chord):
    """
    Normalize chord notation for comparison.
    Converts m♭5 to dim and handles other variations.
    Also normalizes flat notations (♭ and b).
    """
    # Convert to lowercase and remove any whitespace
    chord = chord.lower().strip()
    
    # Handle diminished chords
    if 'm♭5' in chord:
        return chord.replace('m♭5', 'dim')
    elif 'm♭5' in chord:
        return chord.replace('m♭5', 'dim')
    
    # Normalize flat notation
    chord = chord.replace('♭', 'b')
    
    return chord

def get_csv_template():
    """
    Returns the expected CSV structure for both major and minor key files.
    """
    major_template = """Key\tI\tii\tiii\tIV\tV\tvi*\tvii
C\tC\tDm\tEm\tF\tG\tAm\tBm♭5
C#\tC#\tD#m\tE#m\tF#\tG#\tA#m\tB#m♭5
D♭\tD♭\tE♭m\tFm\tG♭\tA♭\tB♭m\tCm♭5
D\tD\tEm\tF#m\tG\tA\tBm\tC#m♭5
E♭\tE♭\tFm\tGm\tA♭\tB♭\tCm\tDm♭5
E\tE\tF#m\tG#m\tA\tB\tC#m\tD#m♭5
F\tF\tGm\tAm\tB♭\tC\tDm\tEm♭5
F#\tF#\tG#m\tA#m\tB\tC#\tD#m\tE#m♭5
G♭\tG♭\tA♭m\tB♭m\tC♭\tD♭\tE♭m\tFm♭5
G\tG\tAm\tBm\tC\tD\tEm\tF#m♭5
A♭\tA♭\tB♭m\tCm\tD♭\tE♭m\tFm\tGm♭5
A\tA\tBm\tC#m\tD\tE\tF#m\tG#m♭5
B♭\tB♭\tCm\tDm\tE♭\tF\tGm\tAm♭5
B\tB\tC#m\tD#m\tE\tF#\tG#m\tA#m♭5"""

    minor_template = """Key\ti\tii\tIII\tiv\tv\tVI\tVII
Am\tAm\tBm♭5\tC\tDm\tEm\tF\tG
Em\tEm\tF#m♭5\tG\tAm\tBm\tC\tD
Bm\tBm\tC#m♭5\tD\tEm\tF#m\tG\tA
F#m\tF#m\tG#m♭5\tA\tBm\tC#m\tD\tE
C#m\tC#m\tD#m♭5\tE\tF#m\tG#m\tA\tB
G#m\tG#m\tA#m♭5\tB\tC#m\tD#m\tE\tF#
D#m\tD#m\tE#m♭5\tF#\tG#m\tA#m\tB\tC#
Dm\tDm\tEm♭5\tF\tGm\tAm\tBb\tC
Gm\tGm\tAm♭5\tBb\tCm\tDm\tEb\tF
Cm\tCm\tDm♭5\tEb\tFm\tGm\tAb\tBb
Fm\tFm\tGm♭5\tAb\tBbm\tCm\tDb\tEb
Bbm\tBbm\tCm♭5\tDb\tEbm\tFm\tGb\tAb"""

    return major_template, minor_template

def create_template_files():
    """
    Creates template CSV files in the data directory.
    """
    data_dir = Path('data')
    data_dir.mkdir(exist_ok=True)
    
    major_template, minor_template = get_csv_template()
    
    with open(data_dir / 'major_keys.csv', 'w', encoding='utf-8') as f:
        f.write(major_template)
    
    with open(data_dir / 'minor_keys.csv', 'w', encoding='utf-8') as f:
        f.write(minor_template) 