import time
from rtmidi.midiutil import open_midiinput, list_available_ports, list_input_ports
from multiprocessing import Process


def handle_MIDI(data):
    print(f'{data}')


def call(event, data=None):
    handle_MIDI(event)

list_input_ports()


port = "1"

midiin, port_name = open_midiinput(port=port, interactive=False)
midiin.set_callback(call)
print(port_name)
while True:
    time.sleep(2)
