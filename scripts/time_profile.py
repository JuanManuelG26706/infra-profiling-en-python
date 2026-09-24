"""Pendiente: medir suma_primos(10000) e imprimir el tiempo en milisegundos."""

"""def cuatro(nombre, trabajo, veces=20):
    print(nombre)
    # 1. time: una sola muestra del reloj de alta resolución.
    inicio = time.perf_counter()
    trabajo()
    print(f"  time         {(time.perf_counter() - inicio) * 1000:8.3f} ms")"""

from src.suma_primos import es_primo

def suma_primos(n):
    #return sum(i for i in range(2, n) if es_primo(i))
    listica = [i for i in range(2,n) if es_primo(i)]
    suma = sum(listica)
    print(suma)



if __name__ == '__main__':
    suma_primos
