# Iris: Your Voice-Controlled Virtual Assistant

**Iris** is a Python-based virtual assistant that uses voice commands to perform various tasks. Whether you need to open websites, play music, fetch the latest news, or simply interact with a virtual assistant, Iris is here to help.

## Features

- **Website Navigation:** Open popular websites like Google, YouTube, LinkedIn, and Gmail directly from voice commands.
- **Music Playback:** Play songs from a custom library by specifying the song name.
- **News Updates:** Retrieve and read out the latest news headlines from NewsAPI.
- **Voice Activation:** Activate the assistant using a wake word and execute commands based on voice input.
- **Stop Listening:** Deactivate the assistant with a voice command to stop listening for further input.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <https://github.com/bhavukus/Iris-Virtual-Assistant>
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd Iris-Virtual-Assistant
   ```

3. **Install Dependencies:**

   Make sure you have Python installed. Then, install the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   - Obtain an API key from NewsAPI and set it as an environment variable named `NEWS_API_KEY`.

     On Windows:
     ```bash
     setx NEWS_API_KEY "your_api_key_here"
     ```

     On macOS/Linux:
     ```bash
     export NEWS_API_KEY="your_api_key_here"
     ```

## Usage

1. **Run the Assistant:**

   Execute the main script to start the virtual assistant:

   ```bash
   python main.py
   ```

2. **Interact with Iris:**

   - **Wake Word:** Start by saying "Iris" to activate the assistant.
   - **Commands:** Issue commands like "open Google," "play [song name]," or "news."
   - **Stop Listening:** Say "stop listening" to deactivate Iris.

## Code Overview

- **`main.py`:** Main script for running the virtual assistant. Contains the core functionality and command processing logic.
- **`myMusic.py`:** Custom module with song links used for playing music.
- **Dependencies:**
  - `speech_recognition`: For converting speech to text.
  - `pyttsx3`: For text-to-speech conversion.
  - `requests`: For making HTTP requests to NewsAPI.
  - `webbrowser`: For opening URLs in a web browser.
  - `os`: For accessing environment variables.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or further information, you can contact me at [bhavukus@gmail.com](bhavukus@gmail.com).
