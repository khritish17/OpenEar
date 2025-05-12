import pyaudio

def check_headset_properties():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    headset_found = False

    print("Available Audio Input Devices:")
    print(info)
    for i in range(0, numdevices):
        device_info = p.get_device_info_by_host_api_device_index(0, i)
        print(device_info)
        if (device_info.get('maxInputChannels')) > 0:
            print(f"-------------------- Device ID: {i} --------------------")
            print(f"Device Name: {device_info.get('name')}")
            print(f"Max Input Channels: {device_info.get('maxInputChannels')}")
            print(f"Default Sample Rate: {device_info.get('defaultSampleRate')}")

            # You might want to add more specific checks to identify your headset
            # based on its name or other properties. This is system-dependent.
            # For example, you could check if 'headset' or a part of its name is present:
            if 'headset' in device_info.get('name').lower():
                print("^^^ Likely your connected headset ^^^")
                headset_found = True
            elif 'microphone' in device_info.get('name').lower():
                print("^^^ Potentially your connected headset microphone ^^^")

    if not headset_found:
        print("\nNo device explicitly identified as 'headset' found. "
              "Check the list above to identify your headset or microphone.")

    p.terminate()

if __name__ == "__main__":
    check_headset_properties()