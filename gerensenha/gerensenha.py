import clipboard as cb
import pathlib


def gerar_senha(tamanho: int, car_esp=False) -> str:
    # Tenho que melhorar a parte de caracteres especiais (forçar a presença deles,
    # caso a flag esteja ativa). Uma ideia é dividir em 20% de caracteres especiais
    # e 80% para o resto.

    import random

    minusculas = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    maiusculas = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    numeros = [str(x) for x in range(0, 10)]
    possibilidades = minusculas + maiusculas + numeros

    if car_esp:
        possibilidades += ['@', '#', '$', '%', '&', '*', '(', ')']

    senha = ""
    for i in range(tamanho):
        senha += random.choice(possibilidades)

    return senha


def main():
    print(gerar_senha(10, car_esp=True))


if __name__ == "__main__":
    main()
