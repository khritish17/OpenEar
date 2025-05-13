import wave
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import os

def perform_fft_on_wav(wav_file):
    """
    Performs a Fast Fourier Transform (FFT) on a WAV audio file
    """
    try:
        with wave.open(wav_file, 'rb') as wf:
            num_channels = wf.getnchannels()
            sample_rate = wf.getframerate()
            sample_width = wf.getsampwidth()
            num_frames = wf.getnframes()
            audio_data = wf.readframes(num_frames)

        # Convert byte data to a NumPy array
        audio_array = np.frombuffer(audio_data, dtype=np.int16)

        # If stereo, take only one channel (e.g., the first one)
        if num_channels > 1:
            print("Stereo audio detected. Using only the first channel for FFT.")
            audio_array = audio_array[::num_channels]

        # Perform FFT
        yf = scipy.fftpack.fft(audio_array)

        # Calculate the corresponding frequencies
        xf = np.fft.fftfreq(len(audio_array), 1 / sample_rate)

        # Only consider the positive frequencies (and the magnitude)
        positive_frequencies = xf[:len(xf)//2]
        magnitude = np.abs(yf[:len(yf)//2])
        return positive_frequencies, magnitude
        
    except FileNotFoundError:
        print(f"Error: WAV file '{wav_file}' not found.")
    except wave.Error as e:
        print(f"Error reading WAV file '{wav_file}': {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    audio_files = [r"D:\Codes\Projects\OpenEars\Experiment Sounds\50cm 5000 Hz.wav",
                   r"D:\Codes\Projects\OpenEars\Experiment Sounds\100cm 5000 Hz.wav",
                   r"D:\Codes\Projects\OpenEars\Experiment Sounds\150cm 5000 Hz.wav",
                   r"D:\Codes\Projects\OpenEars\Experiment Sounds\200cm 5000 Hz.wav",]
    fig, ax = plt.subplots(figsize = (12, 6))
    for audio_file in audio_files:
        dist = os.path.basename(audio_file).split(" ")[0]
        x, y = perform_fft_on_wav(audio_file)
        ax.plot(x, y, label = dist)
        
    ax.set_title('FFT of 5K Hz at different distances')
    ax.set_xlabel('Frequencies')
    ax.set_ylabel('Amplitude/Magnitude')
    ax.legend()
    ax.grid(True)
    plt.show()