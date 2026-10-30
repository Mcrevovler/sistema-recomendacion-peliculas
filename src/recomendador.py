from src.peliculas import CATALOGO


def recomendar(a, c, t, m):
    return [nombre for nombre, regla in CATALOGO.items()
            if regla(a=a, c=c, t=t, m=m)]
