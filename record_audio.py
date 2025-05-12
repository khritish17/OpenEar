import pyaudio
import wave

def record_continuous():
    pass

def record_duration(time_duration = 5, output_file = "output.wav",channels = 1, audio_buffer = 1024, sampling_rate = 44100):
    CHUNK = audio_buffer
    FORMAT = pyaudio.paInt16
    CHANNELS = channels  # Or 2 for stereo, depending on your headset mic
    RATE = sampling_rate
    RECORD_SECONDS = time_duration
    WAVE_OUTPUT_FILENAME = output_file

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()

    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

record_duration()