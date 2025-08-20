import kociemba

# Dictionary used to decode the 
COLOR_TO_POSITION = {
    'Y':'U',
    'R':'F',
    'W':'D',
    'G':'R',
    'B':'L',
    'O':'B'
}

CUBE_SOLVED_SAMPLE = 'YYYYYYYYYGGGGGGGGGRRRRRRRRRWWWWWWWWWBBBBBBBBBOOOOOOOOO' # Example of a cube solved

CUBE_SOLVED_FORMAT_DECODED = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB' # Example of pattern format

test_cube = 'YYYYYYYYYGGGGGGGGGRORRRRRORWWWWWWWWWBBBBBBBBBOROOOOORO'
print(test_cube)

decoded = "".join(COLOR_TO_POSITION[l] for l in test_cube)

print(decoded)

print("-"*10+"RESULT"+"-"*10)

solution = kociemba.solve(decoded)
print(solution)
with open('results.txt', 'w+', encoding='utf-8') as f:
    f.write(solution)