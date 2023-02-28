def minquad(
        xi: list[int | float], yi: list[int | float]
) -> tuple[
    float, float, float
]:

    import math

    n: int = len(xi)

    # Somatórios

    somatorio_xy: float = 0
    somatorio_x: float = 0
    somatorio_y: float = 0
    somatorio_x2: float = 0
    somatorio_y2: float = 0

    for i in range(n):
        somatorio_xy += xi[i]*yi[i]
        somatorio_x += xi[i]
        somatorio_y += yi[i]
        somatorio_x2 += xi[i]**2
        somatorio_y2 += yi[i]**2

    # Termos

    termo_1: int | float = n * somatorio_xy
    termo_2: int | float = somatorio_x * somatorio_y
    termo_3: int | float = n * somatorio_x2
    termo_4: int | float = somatorio_x ** 2
    termo_5: int | float = somatorio_x2 * somatorio_y
    termo_6: int | float = somatorio_x * somatorio_xy
    termo_7: int | float = (n * somatorio_x2) - ((somatorio_x) ** 2)
    termo_8: int | float = (n * somatorio_y2) - ((somatorio_y) ** 2)

    angular: int | float = (termo_1 - termo_2)/(termo_3-termo_4)

    # Calculo de b

    linear: int | float = (termo_5 - termo_6)/(termo_3-termo_4)

    # Calculo do Coeficiente de Correlação Linear

    r2: int | float = (((termo_1 - termo_2)/math.sqrt((termo_7 * termo_8)))**2)

    return angular, linear, r2
