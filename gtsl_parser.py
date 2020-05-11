
import string

import gtsl_scanner
import gtsl_stl



i = 0
token_list = []
symbol_table = {}
parsed_tokens = []
parse_data = {}


def initialize_parse_data():
    # no default for tempo , user must define
    parse_data['tuning'] = 'standard'
    parse_data['capo'] = 0
    parse_data['number_of_tracks'] = 0
    parse_data['streams'] = {}



def parse_error(msg=''):
    # https://docs.python.org/3/reference/simple_stmts.html#raise
    global parsed_tokens
    global symbol_table
    print('PARSE ERROR')
    if msg != '':
        print('error: ', msg)
    print('tokens parsed so far:\n', parsed_tokens)
    print('symbol table so far:\n', symbol_table)
    raise Exception('parse error')



def input_token():
    global i
    global token_list
    return token_list[i]

def match(tk):
    global i
    global parsed_tokens

    if tk == input_token():
        parsed_tokens.append(tk)
        i += 1
    else:
        parse_error()



def tempo():
    match('tempo')
    match('=')
    if input_token().isnumeric():   # match the number
        symbol_table['tempo'] = int(input_token())
        parse_data['tempo'] = int(input_token())
        match(input_token())
    else:
        parse_error('invalid tempo')

def tuning():
    match('tuning')
    match('=')
    if input_token() in list(gtsl_stl.tunings.keys()):   # match the word in stl
        symbol_table['tuning'] = input_token()
        parse_data['tuning'] = input_token()
        match(input_token())
    else:
        parse_error('invalid tuning')

def capo():
    match('capo')
    match('=')
    if input_token().isnumeric():   # match the number
        symbol_table['capo'] = int(input_token())
        parse_data['capo'] = int(input_token())
        match(input_token())
    else:
        parse_error('invalid capo')

def note( stream_name ):
    match('note')
    match('(')
    if input_token().isnumeric():   # string
        string = int(input_token())
        match(input_token())
    else:
        parse_error('invalid string entered in note()')
    match(',')
    if input_token().isnumeric():   # fret
        fret = int(input_token())
        match(input_token())
    else:
        parse_error('invalid fret entered in note()')
    match(')')
    # add note as belonging to stream
    parse_data['streams'][stream_name].append(['note',string,fret])

def chord( stream_name ):
    match('chord')
    match('(')
    if input_token() in list(gtsl_stl.chords.keys()):
        chord = input_token()
        match(input_token())
    else:
        parse_error('invalid chord')
    match(',')
    if input_token() in ['major', 'minor']:
        chord_type = input_token()
        match(input_token())
    else:
        parse_error('invalid chord type')
    match(')')
    # add chord as belonging to stream
    parse_data['streams'][stream_name].append(['chord',chord,chord_type])

def notes_chords( stream_name ):
    if input_token() == 'note':
        note( stream_name )
        notes_chords( stream_name )
    elif input_token() == 'chord':
        chord( stream_name )
        notes_chords( stream_name )
    elif input_token() == '}':
        pass
    else:
        parse_error('invalid stream content')

def stream():
    match('stream')
    stream_name = input_token()
    if stream_name not in gtsl_stl.keywords + list(symbol_table.keys()):
        symbol_table[stream_name] = {'type':'stream'}
        parse_data['number_of_tracks'] += 1
        parse_data['streams'][stream_name] = []
        match(stream_name)
    else:
        parse_error('stream name already exists in symbol table')
    match('(')
    match(')')
    match('{')
    notes_chords( stream_name )
    match('}')

def add_stream():
    match('add_stream')
    match('(')
    stream_name = input_token()
    if stream_name in list(symbol_table.keys()):
        if symbol_table[stream_name]['type'] == 'stream':
            match(stream_name)   # stream name
        else:
            parse_error()
    else:
        parse_error('stream name does not exist in symbol table ?')
    match(',')
    if input_token().isnumeric():
        symbol_table[stream_name]['time'] = int(input_token())              # @todo ?????
        match(input_token())   # stream start time
    else:
        parse_error()
    match(')')



def stmt():
    if input_token() == 'tempo':
        tempo()
    elif input_token() == 'tuning':
        tuning()
    elif input_token() == 'capo':
        capo()
    elif input_token() == 'stream':
        stream()
    elif input_token() == 'add_stream':
        add_stream()
    else:
        parse_error()

def stmt_list():
    if input_token() in gtsl_stl.keywords[:-1]:                 # + list(symbol_table.keys()):
        stmt()
        stmt_list()
    elif input_token() in ['compose']:
        pass
    else:
        parse_error()

def compose():
    match('compose')
    match('(')
    match(')')



def program():
    if input_token() in gtsl_stl.keywords:                      # + list(symbol_table.keys()):
        stmt_list()
        compose()
    else:
        parse_error()



def parse_tokens(list_of_tokens):
    global token_list
    token_list = list_of_tokens
    initialize_parse_data()

    program()

    return [symbol_table, parsed_tokens, parse_data]








# def main():
#     program()
#     print('parsed tokens:\n', parsed_tokens)
#     print('symbol table:\n', symbol_table)

# if __name__ == '__main__':
#     main()