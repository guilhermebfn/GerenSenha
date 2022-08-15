#!/usr/bin/env python3

import clipboard as cb
import pathlib
import argparse

def gerar_senha(tamanho: int, car_esp: bool = False) -> str:
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--especiais", action="store_true", help="adiciona caracteres especiais")
    parser.add_argument("-t", "--tamanho", type=int, default=10, help="tamanho da senha gerada")
    parser.add_argument("-a", "--transferencia", action="store_true", help="manda a senha gerada para a área de transferência")

    args = parser.parse_args()

    senha = gerar_senha(args.tamanho, car_esp=args.especiais)

    if args.transferencia:
        cb.copy(senha)
    else:
        print(senha)


if __name__ == "__main__":
    main()
