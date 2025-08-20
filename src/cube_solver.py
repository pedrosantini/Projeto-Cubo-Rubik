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

# Traduzir cores registradas no verificador
COLOR_TRANSLATED = {
    'Amarelo':'Y',
    'Vermelho':'R',
    'Branco':'W',
    'Verde': 'G',
    'Azul':'B',
    'Laranja':'O'
}

def convert_color_to_position(cubo: str) -> str:
    for chave, valor in COLOR_TO_POSITION.items():
        cubo = cubo.replace(chave, valor)
    return cubo

def solve(cubo: str) -> str:
    return kociemba.solve(cubo)

def test():
    with open('cores_capturadas.txt', 'r', encoding='utf-8') as f:
        cuboT = f.readline()
        for chave, valor in COLOR_TRANSLATED.items():
            cuboT = cuboT.replace(chave, valor)

    print(f"_{cuboT}_")


    CUBE_SOLVED_SAMPLE = 'YYYYYYYYYGGGGGGGGGRRRRRRRRRWWWWWWWWWBBBBBBBBBOOOOOOOOO' # Example of a cube solved

    CUBE_SOLVED_FORMAT_DECODED = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB' # Example of pattern format

    test_cube = 'YBOOYYOYYGGGGGGOBRBRRYROGRBWWYRWWBRBOWWBBORBRWYGWOOWGY'
    print(test_cube)

    decoded = "".join(COLOR_TO_POSITION[l] for l in cuboT)

    print(decoded)

    print("-"*10+"RESULT"+"-"*10)

    solution = kociemba.solve(decoded)
    print(solution)

    with open('results.txt', 'w+', encoding='utf-8') as f:
        f.write(solution)