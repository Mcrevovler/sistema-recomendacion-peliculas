from src.logica import y, o, no

# Proposiciones: a = acción, c = ciencia ficción, t = tolera terror, m = mayor de 18
CATALOGO = {
    "Matrix":       lambda a, c, t, m: y(o(a, c), m),
    "Toy Story":    lambda a, c, t, m: y(no(t), no(m)),
    "El Conjuro":   lambda a, c, t, m: y(t, m),
    "Avengers":     lambda a, c, t, m: y(a, c),
    "John Wick":    lambda a, c, t, m: y(a, m),
    "Alien":        lambda a, c, t, m: y(y(c, t), m),
    "Interstellar": lambda a, c, t, m: c,
    "Coco":         lambda a, c, t, m: no(t),
}
