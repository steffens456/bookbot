def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        num = counting(file_contents)
        print(num)

        dict1 = lower_string(file_contents)

        print(dict1)
        
        

        

def counting(file_contents):
    words = file_contents.split()

    return len(words)

def lower_string(file_contents):
    lower = file_contents.lower()

    book_dict = {'a': 0, 'b': 0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0,'i': 0,
                 'j': 0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0,'q': 0, 'r': 0,
                 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0,'y': 0,'z': 0,' ':0, '.':0
    }

    
    for char in lower:
        if char == 'a':
            book_dict['a'] += 1
        if char == 'b':
            book_dict['b'] += 1
        if char == 'c':
            book_dict['c'] += 1
        if char == 'd':
            book_dict['d'] += 1
        if char == 'e':
            book_dict['e'] += 1
        if char == 'f':
            book_dict['f'] += 1
        if char == 'g':
            book_dict['g'] += 1
        if char == 'h':
            book_dict['h'] += 1
        if char == 'i':
            book_dict['i'] += 1
        if char == 'j':
            book_dict['j'] += 1
        if char == 'k':
            book_dict['k'] += 1
        if char == 'l':
            book_dict['l'] += 1
        if char == 'm':
            book_dict['m'] += 1
        if char == 'n':
            book_dict['n'] += 1
        if char == 'o':
            book_dict['o'] += 1
        if char == 'p':
            book_dict['p'] += 1
        if char == 'q':
            book_dict['q'] += 1
        if char == 'r':
            book_dict['r'] += 1
        if char == 's':
            book_dict['s'] += 1
        if char == 't':
            book_dict['t'] += 1
        if char == 'u':
            book_dict['u'] += 1
        if char == 'v':
            book_dict['v'] += 1
        if char == 'w':
            book_dict['w'] += 1
        if char == 'x':
            book_dict['x'] += 1
        if char == 'y':
            book_dict['y'] += 1
        if char == 'z':
            book_dict['z'] += 1
        if char == ' ':
            book_dict[' '] += 1
        if char == '.':
            book_dict['.'] += 1
    
    return book_dict

    




main()
