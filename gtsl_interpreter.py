from midiutil import MIDIFile
# from midi2audio import FluidSynth
import pprint
import pygame
# import subprocess

import gtsl_scanner
import gtsl_parser
import gtsl_stl





# SCANNER

token_list = gtsl_scanner.get_tokens( input_string=gtsl_scanner.read_file('example.gtsl') )
# print( token_list )



# PARSER        ( make sure the structure of the program is valid before doing anything related to midi )

[symbol_table, parsed_tokens, parse_data] = gtsl_parser.parse_tokens( token_list )
pprint.pprint( parse_data )
# print( symbol_table )
# print( parsed_tokens )
pprint.pprint(gtsl_stl.tunings[parse_data['tuning']])

if parse_data['number_of_tracks'] == 0: raise Exception ('no streams/tracks. not going to create midi file.')





# MIDI

duration = 1                                                    # In beats , for each of the notes
channel  = 0                                                    # map 1 channel to 1 instrument each ?
volume = 100                                                    # 0-127, 127 being full volume, as per the MIDI standard
tempo = parse_data['tempo']                                     # In BPM
strings = gtsl_stl.tunings[parse_data['tuning']]
capo = parse_data['capo']

# create midi object
number_of_tracks = parse_data['number_of_tracks']
MyMIDI = MIDIFile( number_of_tracks )                           # One track, defaults to format 1 (tempo track is created automatically)

track = 0                                                       # channel can have multiple tracks

# for each stream/track
for stream in list(parse_data['streams'].keys()):
    time = 0                                                    # In beats  ( quarter notes )

    # add track name
    MyMIDI.addTrackName( track, time, stream )

    # add tempo
    MyMIDI.addTempo( track, time, tempo )
    
    # add notes and chords
    for note_chord in parse_data['streams'][stream]:

        if note_chord[0] == 'note':
            string = note_chord[1]
            fret = note_chord[2]
            pitch = strings[string]['midipitch'] + capo + fret

            MyMIDI.addNote( track, channel, pitch, time, duration, volume)

        elif note_chord[0] == 'chord':
            chord = note_chord[1]
            chord_type = note_chord[2]
            pass

        time += duration

    track += 1



midi_file_name = 'mymidifile.midi'

# write to midi file

with open(midi_file_name, 'wb') as output_file:
    MyMIDI.writeFile(output_file)



# play midi file
pygame.init()
pygame.mixer.music.load(midi_file_name)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():    # wait for midi file to finish playing
    pygame.time.wait(1000)





# # synthesize midi to audio

# output_path = ''
# audio_file_name = 'midioutput.wav'

# # fs = FluidSynth()
# # fs.midi_to_audio(midi_file_name, audio_file_name)

# command = 'timidity\\timidity ' + midi_file_name + ' -Ow -o ' + audio_file_name
# subprocess.Popen(command)