from midiutil import MIDIFile
import pprint

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


print( parse_data['streams']['gt1'] )
raise Exception('gg')





# degrees  = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number


duration = 1                                                    # In beats , for each of the notes
channel  = 0                                                    # map 1 channel to 1 instrument each ?
volume = 100                                                    # 0-127, 127 being full volume, as per the MIDI standard

# time = 0                                                      # In beats  ( quarter notes )

# create midi object
number_of_tracks = parse_data['number_of_tracks']
MyMIDI = MIDIFile( number_of_tracks )                           # One track, defaults to format 1 (tempo track is created automatically)

track = 0                                                       # channel can have multiple tracks

for stream in list(parse_data['streams'].keys()):
    time = 0                                                    # In beats  ( quarter notes )

    # add track name
    MyMIDI.addTrackName(track, time, stream)

    # add tempo
    tempo = symbol_table['tempo']                               # In BPM
    MyMIDI.addTempo( track, time, tempo )
    
    # add notes and chords
    for note_chord in parse_data['streams'][stream]:
        if note_chord[0] == 'note':
            # note
            pass
        elif note_chord[0] == 'chord':
            # chord
            pass

        time += duration

    track += 1



# for i, pitch in enumerate(degrees):
#     MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)



pitch = 60  # MIDI note number
MyMIDI.addNote( track, channel, pitch, time, duration, volume )

time  = 1
pitch = 61
MyMIDI.addNote( track, channel, pitch, time, duration, volume )



with open("mymidifile.midi", 'wb') as output_file:
    MyMIDI.writeFile(output_file)