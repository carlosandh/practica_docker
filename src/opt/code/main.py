from gettext import find
import pandas as pd
import numpy as np


def get_fractions(valor):
    """

    Parameters
    ----------
    valor :Es el string que sera transformado a flotante.


    Returns
    ----------
    Regresa el valor en su forma decimal flotante.

    """
    if "/" in valor:
        d = valor.find("/")
        l = len(valor)
        decimal = int(valor[0:d]) / int(valor[d + 1 : l])
        return decimal
    else:
        return float(valor)


def suma(a, b):
    """

    Parameters
    ----------
    a : int, float, string.
    Primer valor definido para la operación.

    b : int, float, string.
    Segundo valor definifo para la operación.


    Returns
    -------
    float
    Valor obtenido por la suma de los parámetros.


    """
    sumando_a = float(a)
    sumando_b = float(b)
    return sumando_a + sumando_b


def resta(a, b):
    """

    Parameters
    ----------
    a : int, float, string.
    Primer valor definido para la operación.

    b : int, float, string.
    Segundo valor definifo para la operación.

    Returns
    -------
    Valor obtenido por la resta de los parámetros.

    """
    minuendo = float(a)
    sustraendo = float(b)
    return minuendo - sustraendo


def multiplicacion(a, b):
    """

    Parameters
    ----------
    a : int, float, string.
    Primer valor definido para la operación.

    b : int, float, string.
    Segundo valor definido para la operación.


    Returns
    -------
    Valor obtenido por la multiplicación de los parámetros.

    """
    multiplicando = float(a)
    multiplicador = float(b)
    return multiplicando * multiplicador


def division(a, b):
    """

    Parameters
    ----------
    a : int, float, string.
    Primer valor definido para la operación.

    b : int, float, string.
    Segundo valor definido para la operación.


    Returns
    -------
    Valor obtenido por la división de los parámetros.

    """
    dividendo = float(a)
    divisor = float(b)
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        return "Division entre cero"


if __name__ == "__main__":

    data = pd.read_csv("src/opt/input/numeros.csv", header=0)
    res_data = (
        data.assign(res_suma=data.numero1 + data.numero2)
        .assign(res_resta=data.numero1 - data.numero2)
        .assign(res_mult=data.numero1 * data.numero2)
        .assign(res_div=data.numero1 / data.numero2)
    )

    res_data.to_csv("src/opt/local_output/numeros_salida.csv")
