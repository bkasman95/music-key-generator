from chord_data import load_chord_data, normalize_chord
from pathlib import Path

class KeyDetector:
    def __init__(self, major_csv_path=None, minor_csv_path=None):
        """
        Initialize the KeyDetector with chord data from CSV files.
        
        Args:
            major_csv_path (str, optional): Path to major keys CSV file
            minor_csv_path (str, optional): Path to minor keys CSV file
        """
        if major_csv_path is None:
            major_csv_path = Path('data/major_keys.csv')
        if minor_csv_path is None:
            minor_csv_path = Path('data/minor_keys.csv')
            
        self.major_chords, self.minor_chords = load_chord_data(major_csv_path, minor_csv_path)
        print(f"Loaded {len(self.major_chords)} major keys and {len(self.minor_chords)} minor keys")

    def find_possible_keys(self, chord_progression):
        """
        Find all possible keys for a given chord progression.
        
        Args:
            chord_progression (list): List of chords in the progression
            
        Returns:
            dict: Dictionary containing possible keys and their progressions
        """
        # Normalize the input progression
        normalized_progression = [normalize_chord(chord) for chord in chord_progression]
        print(f"Normalized progression: {normalized_progression}")
        
        possible_keys = {}
        
        # Check major keys
        for key, progressions in self.major_chords.items():
            matches = self._check_progression(normalized_progression, progressions)
            if matches:
                possible_keys[f"Key of {key} (Major)"] = matches

        # Check minor keys
        for key, progressions in self.minor_chords.items():
            matches = self._check_progression(normalized_progression, progressions)
            if matches:
                possible_keys[f"Key of {key} (Minor)"] = matches

        return possible_keys

    def _check_progression(self, chord_progression, key_progressions):
        """
        Check if a chord progression matches any combination of chords in a key.
        
        Args:
            chord_progression (list): List of chords to check
            key_progressions (dict): Dictionary of progressions for a key
            
        Returns:
            dict: Dictionary of matching progressions and their positions
        """
        # Create a mapping of chords to their roman numerals in this key
        chord_to_roman = {chord: roman for roman, chord in key_progressions.items()}
        
        # Check if all chords in the progression exist in this key
        matches = {}
        for chord in chord_progression:
            if chord in chord_to_roman:
                matches[chord] = chord_to_roman[chord]
            else:
                return None
        
        # If we found matches for all chords, return them
        if len(matches) == len(chord_progression):
            return matches
        
        return None

def main():
    detector = KeyDetector()
    
    print("Welcome to the Music Key Detector!")
    print("Enter your chord progression (e.g., 'C Em G'):")
    
    while True:
        try:
            user_input = input("> ").strip()
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
                
            # Split the input into individual chords and clean them
            chord_progression = []
            for chord in user_input.split():
                # Remove quotes, commas, and extra whitespace
                clean_chord = chord.strip().replace(',', '').replace("'", '').replace('"', '')
                if clean_chord:  # Only add non-empty chords
                    chord_progression.append(clean_chord)
            
            print(f"Processing chords: {chord_progression}")
            
            # Find possible keys
            possible_keys = detector.find_possible_keys(chord_progression)
            
            if possible_keys:
                print("\nPossible keys found:")
                for key, progression in possible_keys.items():
                    print(f"\n{key}:")
                    for chord, roman_numeral in progression.items():
                        print(f"  {chord} → {roman_numeral}")
            else:
                print("\nNo matching keys found for this progression.")
                
        except Exception as e:
            print(f"Error: {str(e)}")
            print("Please try again with a valid chord progression.")

if __name__ == "__main__":
    main() 