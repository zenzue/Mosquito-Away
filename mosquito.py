import numpy as np
import sounddevice as sd
import argparse

def play_mosquito_sound(frequency, duration):
    """
    Play a sound at the given frequency (Hz) for the specified duration (seconds).

    :param frequency: Frequency of the sound in Hertz.
    :param duration: Duration to play the sound in seconds.
    """
    fs = 44100  
    t = np.linspace(0, duration, int(fs * duration), False)
    tone = np.sin(frequency * t * 2 * np.pi)
    sd.play(tone, samplerate=fs)  
    sd.wait()  

def main():
    parser = argparse.ArgumentParser(description="Generate a high-frequency tone resembling a mosquito sound. By w01f")
    parser.add_argument("-f", "--frequency", type=int, default=17000, help="Frequency of the sound in Hertz. Default is 17000 Hz.")
    parser.add_argument("-d", "--duration", type=int, default=5, help="Duration to play the sound in seconds. Default is 5 seconds.")

    args = parser.parse_args()

    if args.frequency < 15000 or args.frequency > 20000:
        print("Frequency should be between 15000 Hz and 20000 Hz.")
    else:
        play_mosquito_sound(frequency=args.frequency, duration=args.duration)

if __name__ == "__main__":
    main()

# sudo apt-get update
# sudo apt-get install portaudio19-dev
# pip install sounddevice numpy
