
keywords = ['note', 'notes', 'chord', 'skip', 'tempo', 'tuning', 'capo', 'stream', 'add_stream', 'compose']        # 'compose' has to be the last word in this list for the parser to wprk properly ¯\_(ツ)_/¯



#          0     1      2      3     4      5      6     7     8       9    10     11     12    13     14     15    16
notes = [ 'C' , 'C#' , 'Db' , 'D' , 'D#' , 'Eb' , 'E' , 'F' , 'F#' , 'Gb' , 'G' , 'G#' , 'Ab' , 'A' , 'A#' , 'Bb' , 'B' ]



tunings = {

    'standard' : {
        1 : 64,     # e
        2 : 59,     # b
        3 : 55,     # g
        4 : 50,     # d
        5 : 45,     # A
        6 : 40,     # E
    },

    'ebgdae' : {
        1 : 64,     # string : midipitch
        2 : 59,
        3 : 55,
        4 : 50,
        5 : 45,
        6 : 40,
    },
}



chords = {
    'C' : {
        'major' : [],
        'minor' : [],
    },
    'D' : {
        'major' : [],
        'minor' : [],
    },
    'E' : {
        'major' : [],
        'minor' : [],
    },
    'F' : {
        'major' : [],
        'minor' : [],
    },
    'G' : {
        'major' : [],
        'minor' : [],
    },
    'A' : {
        'major' : [],
        'minor' : [],
    },
    'B' : {
        'major' : [],
        'minor' : [],
    },
}