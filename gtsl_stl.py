
keywords = ['note', 'notes', 'chord', 'tempo', 'tuning', 'capo', 'stream', 'add_stream', 'compose']        # 'compose' has to be the last word in this list for the parser to wprk properly ¯\_(ツ)_/¯



#          0     1      2      3     4      5      6     7     8       9    10     11     12    13     14     15    16
notes = [ 'C' , 'C#' , 'Db' , 'D' , 'D#' , 'Eb' , 'E' , 'F' , 'F#' , 'Gb' , 'G' , 'G#' , 'Ab' , 'A' , 'A#' , 'Bb' , 'B' ]



tunings = {

    'standard' : {
        1 : {'midipitch': 64,},     # e
        2 : {'midipitch': 59,},     # b
        3 : {'midipitch': 55,},     # g
        4 : {'midipitch': 50,},     # d
        5 : {'midipitch': 45,},     # A
        6 : {'midipitch': 40,},     # E
    },

    'ebgdae' : {
        1 : {'midipitch': 64,},
        2 : {'midipitch': 59,},
        3 : {'midipitch': 55,},
        4 : {'midipitch': 50,},
        5 : {'midipitch': 45,},
        6 : {'midipitch': 40,},
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