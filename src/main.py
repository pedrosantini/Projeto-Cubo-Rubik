from rubik import cube
from rubik import solve
from rubik import optimize
from rubik_solver import utils


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

cube = """GBB
                WYY
                WOR
            RBO GGW GGY OOY
            YBB RRG RGW GOR
            YOB RRW OYO GYB
                WWB
                WWO
                RBY""".strip

print(cube)


