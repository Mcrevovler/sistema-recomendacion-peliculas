from src.recomendador import recomendar


def test_mayor_con_ciencia_ficcion_recibe_matrix():
    assert "Matrix" in recomendar(a=False, c=True, t=False, m=True)


def test_menor_no_recibe_terror():
    assert "El Conjuro" not in recomendar(a=True, c=True, t=True, m=False)
