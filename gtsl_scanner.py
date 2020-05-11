import string

def scan(input_string):
    # print('starting scan')
    
    token_list = []
    i = 0
    while i < len(input_string):
        cur = input_string[i]
        if cur in [' ', '\t', '\n']:
            pass
        elif cur in ['(', ')', '{', '}', ',', ':', '=']:
            token_list.append(cur)
        # elif cur == ':':
        #     if input_string[i+1] == '=':
        #         token_list.append('assign')
        #         i += 1
        #     else:
        #         raise Exception('lexical error')
        elif cur in string.digits:
            num = ''
            while True:
                if input_string[i] in string.digits:
                    num = num + input_string[i]
                    i += 1
                else:
                    i -= 1
                    break
            token_list.append(num)   
        elif cur in string.ascii_letters+'_'+string.digits:
            result_string = ''
            while True:
                if input_string[i] in string.ascii_letters+'_'+string.digits:
                    result_string += input_string[i]
                    i += 1
                else:
                    i -= 1
                    break
            token_list.append(result_string)
        else:
            raise Exception('lexical error')
        i += 1
        # print('tokenlist: ', token_list)

    return token_list

def read_file(filepath="example.gtsl"):
    f = open(filepath)
    input_string = f.read()
    f.close()
    # print('file read')
    return input_string

def get_tokens(input_string=""):
    # print('gonna get tokens')    
    if input_string == "":
        input_string = read_file()
    
    token_list = scan(input_string)
    # token_list.append('end_of_program')
    # print('got tokens')
    return token_list



# def main():
#     token_list = get_tokens()
#     print('input tokens:\n',token_list)

# if __name__ == '__main__':
#     main()
