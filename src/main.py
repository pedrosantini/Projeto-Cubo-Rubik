import verificador_cores
import cube_solver

if __name__ == '__main__':
    cubo = 'YWGBYWBRRWGROGROBWWYBYRWYRYBBGGWORWOGYOYBOYOOWBRGOGGRB'
    gerada = verificador_cores.verificador_cores()
    print(gerada)
    if len(gerada) == 54:
        print(gerada)
        cuboC = cube_solver.convert_color_to_position(gerada)
        print(cuboC)
        solution = cube_solver.solve(cuboC)
        print(solution)
