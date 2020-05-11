
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
        'midipitch': 64,
    },
    2 : {
        'note': 16,
        'midipitch': 59,
    },
    3 : {
        'note': 10,
        'midipitch': 64,
    },
    4 : {
        'note': 3,
        'midipitch': 64,
    },
    5 : {
        'note': 13,
        'midipitch': 64,
    },
    6 : {
        'note': 6,
        'midipitch': 64,
    }
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