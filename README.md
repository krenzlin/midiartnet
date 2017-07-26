# midiartnet
triggering configured scenes and send Artnet UDP by incoming MIDI events

# Idea

* rtmidi provides callback functionality.
* add a MIDI dispatcher
* if a MIDI note is received decide which scene/cue to load
* -> send Artnet packages per UDP

# needs

* python-rtmidi
* loopMIDI running and configured in DAW (e.g. Ableton)

# Windows usage

* install miniconda
* let it add itself to PATH
* open cmd
    * python should be the continuum one
* then pip install 'python-rtmidi'

* run 'python callback_multiprocessing.py'

# Problems

windows and multiprocessing seem to have problems with file descriptors and other stuff (under linux fork is used which behaves somewhat differently)

so for now just don't use it.


