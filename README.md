# Mosquito Sound Generator by w01f

The Mosquito Sound Generator is a Python script designed to generate and play a high-frequency tone that resembles the buzzing sound of a mosquito. This script allows users to specify the frequency and duration of the sound via command-line arguments, making it highly customizable for different use cases, including testing hearing range, deterring pests, or just for fun.

## Features

- Generate a sine wave sound at a specified frequency.
- Play the sound for a specified duration.
- Customizable frequency range from 15 kHz to 20 kHz, which is typical for mosquito sounds.
- Command-line interface for easy use and customization.

## Requirements

To run this script, you need Python and the following Python packages:

- `numpy`: For generating the sine wave.
- `sounddevice`: For playing the sound.

You also need the PortAudio library, which is a dependency of the `sounddevice` package.

## Installation

1. **Install Python Packages**: Install the required Python packages using `pip`. It's recommended to do this in a virtual environment.

    ```bash
    pip install numpy sounddevice
    ```

2. **Install PortAudio**:

    - **Linux** (Debian/Ubuntu):
        ```bash
        sudo apt-get update
        sudo apt-get install portaudio19-dev
        ```
    - **macOS**:
        ```bash
        brew update
        brew install portaudio
        ```
    - **Windows**: The `sounddevice` package should include the necessary PortAudio binaries. If you encounter issues, try reinstalling `sounddevice` or consult the `sounddevice` documentation.

3. **Reinstall `sounddevice`** (Optional): If you installed PortAudio after `sounddevice`, you might need to reinstall `sounddevice` to ensure it detects PortAudio.

    ```bash
    pip install sounddevice --force-reinstall
    ```

## Usage

Run the script from the command line, specifying the desired frequency and duration for the sound. Both parameters are optional and have defaults.

```bash
python mosquito.py [-f FREQUENCY] [-d DURATION]
```

- `-f`, `--frequency`: Specify the frequency of the sound in Hertz (default: 17000 Hz).
- `-d`, `--duration`: Specify the duration to play the sound in seconds (default: 5 seconds).

### Example

To play a sound at 18,000 Hz for 10 seconds:

```bash
python mosquito.py -f 18000 -d 10
```

## Caution

- Be cautious when playing high-frequency sounds, especially at high volumes or for extended periods, as they can be irritating or potentially harmful to hearing.
- Start at a low volume and increase gradually to a comfortable level.

## License

This project is open-source and available under the MIT License. See the LICENSE file for more details.
