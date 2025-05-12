# import pyaudio
# import numpy as np

# CHUNK = 1024  # Number of audio frames to read at a time
# FORMAT = pyaudio.paInt16  # Audio format (16-bit integers)
# CHANNELS = 1  # Mono audio
# RATE = 44100  # Sample rate (samples per second)

# def audio_callback(in_data, frame_count, time_info, status):
#     """
#     Callback function called for each audio chunk.
#     'in_data' contains the audio data as bytes.
#     """
#     if in_data is not None:
#         # Convert the byte data to a NumPy array for processing
#         audio_array = np.frombuffer(in_data, dtype=np.int16)

#         # --- Your audio processing logic goes here ---
#         # For example, you could calculate the RMS energy:
#         rms = np.sqrt(np.mean(audio_array**2))
#         print(f"RMS Energy: {rms}")

#         # Or perform more complex analysis...

#     return (in_data, pyaudio.paContinue)  # Return the processed data (or original) and continue streaming

# p = pyaudio.PyAudio()

# try:
#     stream = p.open(format=FORMAT,
#                     channels=CHANNELS,
#                     rate=RATE,
#                     input=True,
#                     frames_per_buffer=CHUNK,
#                     stream_callback=audio_callback)

#     print("* Streaming audio... Press Ctrl+C to stop")

#     # Keep the stream active until interrupted
#     while stream.is_active():
#         import time
#         time.sleep(0.1)

# except KeyboardInterrupt:
#     print("* Stopping audio stream")
# finally:
#     if 'stream' in locals() and stream.is_active():
#         stream.stop_stream()
#         stream.close()
#     p.terminate()
