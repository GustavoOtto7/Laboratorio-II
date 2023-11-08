def check(tri_values):    
    try:
        side_a = float(input("Digite o tamanho do lado A: "))
        tri_values.append(side_a)
        side_b = float(input("Digite o tamanho do lado B: "))
        tri_values.append(side_b)
        side_c = float(input("Digite o tamanho do lado C: "))
        tri_values.append(side_c)
        print(tri_values)
        tri_values.sort()
        print(tri_values)
        if tri_values[2] > (tri_values[0] + tri_values[1]):
            raise ValueError("ValueError")
        else:
            if side_a == side_b and side_b == side_c:
                print("Seu triângulo é equilátero!")
            elif side_a != side_b and side_a != side_c and side_b != side_c:
                print("Seu triângulo é escaleno!")
            else:
                print("Seu triângulo é isósceles!")
    except ValueError as error:
        print(f"[Erro] - O triângulo informado não é válido! Erro: ({error})")
    except BaseException as error:
        print(f"[Erro] - Ocorreu um erro! Erro: ({error})")

def main():
    tri_values = []
    check(tri_values)
main()