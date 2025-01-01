# Flash Card App

## Overview
Flash Card App is an interactive Python-based application designed to help users learn French vocabulary through flashcards. It features a graphical user interface (GUI) built with the Tkinter module and supports word flipping with translations. The application also includes functionality for tracking known words and playing sounds on button clicks.

---

## Features
- **Interactive Flashcards**: Learn French words with flashcards showing both French and English translations.
- **GUI Design**: User-friendly interface using Tkinter and images for visual appeal.
- **Sound Effects**: Audio feedback on button clicks (requires sound files in the `sounds/` directory).
- **Tracking Progress**: Keeps track of known words.
- **Randomized Words**: Presents words randomly for efficient learning.

---

## Installation
### Prerequisites
- Python 3.x
- Required Python libraries:
  - `tkinter`
  - `pandas`
  - `Pillow`
  - `pygame`

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/flash-card-app.git
   cd flash-card-app
   ```
2. Install required libraries:
   ```bash
   pip install pandas Pillow pygame
   ```
3. Place the required files:
   - CSV file with French and English words: `data/french_words.csv`
   - Images for flashcards: `images/card_front.png`, `images/card_back.png`
   - Images for buttons: `images/right.png`, `images/wrong.png`
   - Optional sound files: `sounds/right.mp3`, `sounds/wrong.mp3`

4. Run the application:
   ```bash
   python main.py
   ```

---

## Usage
1. Launch the app by running the `main.py` file.
2. Use the **Right** button to mark a word as known.
3. Use the **Wrong** button to see the translation in English.
4. The flashcards will flip back to French after a short delay.

---

## File Structure
```
flash-card-app/
|-- main.py          # Main application script
|-- data/
|   |-- french_words.csv    # Vocabulary file
|-- images/
|   |-- card_front.png      # Front of the flashcard
|   |-- card_back.png       # Back of the flashcard
|   |-- right.png           # Right button image
|   |-- wrong.png           # Wrong button image
|-- sounds/
    |-- right.mp3           # Optional sound for right button
    |-- wrong.mp3           # Optional sound for wrong button
```

---

## Contribution
Feel free to fork this repository and submit pull requests for any feature enhancements or bug fixes.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments
- **Pandas**: For handling the CSV file.
- **Pillow**: For image resizing and manipulation.
- **Pygame**: For playing sound effects.

---

## Screenshots
_Add screenshots of your application here to showcase its UI and functionality._

