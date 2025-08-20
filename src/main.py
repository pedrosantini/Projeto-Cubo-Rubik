import kociemba


'''

c = cube.Cube("""GBB
                WYY
                WOR
            RBO GGW GGY OOY
            YBB RRG RGW GOR
            YOB RRW OYO GYB
                WWB
                WWO
                RBY""")

print(c)

s = solve.Solver(c)

s.solve()

print(len(s.moves))

optimize.optimize_moves(s.moves)

print(s.moves)
print(len(s.moves))

'''
cube_solved_sample = 'YYYYYYYYYGGGGGGGGGRRRRRRRRRWWWWWWWWWBBBBBBBBBOOOOOOOOO'
cube_solved_decoded = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'

cube = 'YYYYYYYYYGGGGGGGGGRORRRRRORWWWWWWWWWBBBBBBBBBOROOOOORO'
print(cube)

decoded = ''

for a in cube:
    if a == 'Y':
        decoded += 'U'
    if a == 'R':
        decoded += 'F'
    if a == 'W':
        decoded += 'D'
    if a == 'G':
        decoded += 'R'
    if a == 'B':
        decoded += 'L'
    if a == 'O':
        decoded += 'B'

print(decoded)

print("-------------- RESULTADO _______")
print(kociemba.solve(decoded))


