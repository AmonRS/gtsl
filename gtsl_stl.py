
keywords = ['note', 'notes', 'chord', 'tempo', 'tuning', 'capo', 'stream', 'add_stream', 'compose']        # 'compose' has to be the last word in this list for the parser to wprk properly ¯\_(ツ)_/¯


#          0     1      2      3     4      5      6     7     8       9    10     11     12    13     14     15    16
notes = [ 'C' , 'C#' , 'Db' , 'D' , 'D#' , 'Eb' , 'E' , 'F' , 'F#' , 'Gb' , 'G' , 'G#' , 'Ab' , 'A' , 'A#' , 'Bb' , 'B' ]


tunings = {
    'standard' : '',
    'ebgdae' : '',
}


strings = {
    1 : {
        'note': 6,
        'midipitch': '',
    },
    2 : 16,
    3 : 10,
    4 : 3,
    5 : 13,
    6 : 6,
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