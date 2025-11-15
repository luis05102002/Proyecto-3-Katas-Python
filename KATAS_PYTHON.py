# -*- coding: utf-8 -*-
"""
40 KATAS DE PYTHON - MODO INTERACTIVO
Autor: Don Luis Gómez Del Moral

"""

# ===================================================================
# IMPORTS
# ===================================================================
import math
from functools import reduce


# ===================================================================
# KATAS (1 a 40)
# ===================================================================

# ------------------- KATA 1 -------------------
def contar_frecuencias_letras(texto):
    """Cuenta frecuencia de caracteres (sin espacios)."""
    texto = texto.replace(" ", "")
    frec = {}
    for c in texto:
        frec[c] = frec.get(c, 0) + 1
    return frec


# ------------------- KATA 2 -------------------
def duplicar_lista(lista):
    """Duplica cada número usando map()."""
    return list(map(lambda x: x * 2, lista))


# ------------------- KATA 3 -------------------
def palabras_con_objetivo(lista_palabras, objetivo):
    """Filtra palabras que contienen objetivo."""
    return [p for p in lista_palabras if objetivo in p]


# ------------------- KATA 4 -------------------
def diferencia_listas(l1, l2):
    """Resta elementos de l2 a l1."""
    if len(l1) != len(l2): raise ValueError("Misma longitud")
    return list(map(lambda a, b: a - b, l1, l2))


# ------------------- KATA 5 -------------------
def evaluar_media(notas, aprob=5):
    """Calcula media y estado."""
    media = 0 if not notas else sum(notas)/len(notas)
    return (media, "aprobado" if media >= aprob else "suspenso")


# ------------------- KATA 6 -------------------
def factorial_recursivo(n):
    """Factorial recursivo."""
    return 1 if n in (0,1) else n * factorial_recursivo(n-1)


# ------------------- KATA 7 -------------------
def tuplas_a_strings(tuplas):
    """Convierte tuplas a strings."""
    return list(map(lambda t: ''.join(map(str, t)), tuplas))


# ------------------- KATA 8 -------------------
def division_segura():
    """División con entrada interactiva."""
    try:
        a = float(input("   Número 1: "))
        b = float(input("   Número 2: "))
        print(f"   → {a/b}")
        return True
    except (ValueError, ZeroDivisionError):
        print("   Error: Entrada inválida o división por cero")
        return False


# ------------------- KATA 9 -------------------
def filtrar_mascotas_prohibidas(mascotas):
    """Excluye mascotas prohibidas."""
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, mascotas))


# ------------------- KATA 10 -------------------
class ListaVaciaError(Exception): pass
def promedio_lista(lst):
    """Promedio con excepción si vacía."""
    try:
        if not lst: raise ListaVaciaError("Lista vacía")
        return sum(lst)/len(lst)
    except ListaVaciaError as e: print(f"   {e}"); return None


# ------------------- KATA 11 -------------------
def validar_edad():
    """Valida edad interactiva."""
    try:
        e = int(input("   Edad: "))
        if not 0<=e<=120: raise ValueError("Fuera de rango")
        print(f"   → Edad válida: {e}")
    except ValueError:
        print("   Error: Número entero entre 0 y 120")


# ------------------- KATA 12 -------------------
def longitudes_palabras(frase):
    """Longitud de palabras."""
    return list(map(len, frase.split()))


# ------------------- KATA 13 -------------------
def mayus_minus_unicas(cad):
    """Tuplas (MAY, min) de letras únicas."""
    unicas = {c.lower() for c in cad if c.isalpha()}
    return [(c.upper(), c.lower()) for c in unicas]


# ------------------- KATA 14 -------------------
def palabras_con_inicio(palabras, letra):
    """Palabras que empiezan con letra."""
    return list(filter(lambda p: p.startswith(letra), palabras))


# ------------------- KATA 15 -------------------
sumar_tres = lambda lst: list(map(lambda x: x+3, lst))


# ------------------- KATA 16 -------------------
def palabras_largas(texto, n):
    """Palabras más largas que n."""
    return list(filter(lambda p: len(p)>n, texto.split()))


# ------------------- KATA 17 -------------------
def digitos_a_numero(digs):
    """Dígitos a número."""
    return reduce(lambda a,d: a*10+d, digs, 0)


# ------------------- KATA 18 -------------------
def estudiantes_excelentes():
    """Estudiantes con calificación ≥90."""
    est = [{"nombre":"Ana","calificacion":95},{"nombre":"Luis","calificacion":88},{"nombre":"Marta","calificacion":92}]
    return list(filter(lambda e: e["calificacion"]>=90, est))


# ------------------- KATA 19 -------------------
filtrar_impares = lambda lst: list(filter(lambda x: x%2!=0, lst))


# ------------------- KATA 20 -------------------
def solo_enteros(lst):
    """Filtra enteros."""
    return list(filter(lambda x: isinstance(x,int), lst))


# ------------------- KATA 21 -------------------
cubo = lambda x: x**3


# ------------------- KATA 22 -------------------
def producto_total(lst):
    """Producto de elementos."""
    return reduce(lambda a,x: a*x, lst, 1)


# ------------------- KATA 23 -------------------
def concatenar_palabras(lst):
    """Concatena palabras."""
    return reduce(lambda a,p: a+p, lst, "")


# ------------------- KATA 24 -------------------
def diferencia_total(lst):
    """Resta acumulativa."""
    return 0 if not lst else reduce(lambda a,x: a-x, lst, lst[0])


# ------------------- KATA 25 -------------------
def contar_caracteres(texto):
    """Longitud de texto."""
    return len(texto)


# ------------------- KATA 26 -------------------
resto_division = lambda a,b: a%b


# ------------------- KATA 27 -------------------
def promedio_numeros(lst):
    """Promedio o 0 si vacía."""
    return 0 if not lst else sum(lst)/len(lst)


# ------------------- KATA 28 -------------------
def primer_duplicado(lst):
    """Primer elemento repetido."""
    s = set()
    for x in lst:
        if x in s: return x
        s.add(x)
    return None


# ------------------- KATA 29 -------------------
def enmascarar_cadena(val):
    """Enmascara todo menos últimos 4."""
    s = str(val)
    return s if len(s)<=4 else '#'*(len(s)-4) + s[-4:]


# ------------------- KATA 30 -------------------
def son_anagramas(p1,p2):
    """Compara letras ordenadas."""
    return sorted(p1.lower()) == sorted(p2.lower())


# ------------------- KATA 31 -------------------
class NombreNoEncontrado(Exception): pass
def buscar_nombre():
    """Busca nombre en lista interactiva."""
    try:
        noms = [n.strip() for n in input("   Nombres (separados por coma): ").split(',')]
        bus = input("   Buscar: ").strip()
        if bus in noms:
            print(f"   → {bus} encontrado")
        else:
            raise NombreNoEncontrado(f"{bus} no está")
    except NombreNoEncontrado as e:
        print(f"   {e}")


# ------------------- KATA 32 -------------------
def buscar_puesto(nombre, empleados):
    """Busca puesto de empleado."""
    for e in empleados:
        if e["nombre"] == nombre: return e["puesto"]
    return "No trabaja aquí"


# ------------------- KATA 33 -------------------
sumar_listas = lambda l1,l2: list(map(lambda a,b: a+b, l1, l2))


# ------------------- KATA 34 -------------------
class Arbol:
    def __init__(self): self.tronco,self.ramas=1,[]
    def crecer_tronco(self): self.tronco+=1
    def nueva_rama(self): self.ramas.append(1)
    def crecer_ramas(self): self.ramas=[r+1 for r in self.ramas]
    def quitar_rama(self,i): self.ramas.pop(i) if 0<=i<len(self.ramas) else None
    def info_arbol(self): return {"tronco":self.tronco,"ramas":len(self.ramas),"long":self.ramas[:]}


# ------------------- KATA 35 -------------------
class UsuarioBanco:
    def __init__(self,n,s,cc): self.nombre,self.saldo,self.cuenta_corriente=n,s,cc
    def retirar_dinero(self,c): 
        if c>self.saldo: raise ValueError("Saldo insuficiente")
        self.saldo-=c
    def transferir_dinero(self,c,d): self.retirar_dinero(c); d.agregar_dinero(c)
    def agregar_dinero(self,c): self.saldo+=c


# ------------------- KATA 36 -------------------
def procesar_texto(texto, opcion, *args):
    """Procesa texto según opción."""
    if opcion=="contar": 
        p = texto.lower().split()
        return {w: p.count(w) for w in set(p)}
    if opcion=="reemplazar": 
        if len(args)!=2: raise ValueError("2 argumentos")
        return texto.replace(args[0], args[1])
    if opcion=="eliminar": 
        if len(args)!=1: raise ValueError("1 argumento")
        return ' '.join([w for w in texto.split() if w!=args[0]])
    raise ValueError("Opción inválida")


# ------------------- KATA 37 -------------------
def momento_del_dia():
    """Determina momento del día."""
    try:
        h = int(input("   Hora (0-23): "))
        if 0<=h<6 or h>=18: print("   → Noche")
        elif h<12: print("   → Mañana")
        else: print("   → Tarde")
    except ValueError:
        print("   Error: Ingresa 0-23")


# ------------------- KATA 38 -------------------
def calificacion_texto():
    """Convierte nota numérica a texto."""
    try:
        n = int(input("   Nota (0-100): "))
        if not 0<=n<=100: print("   → Fuera de rango")
        elif n<=69: print("   → Insuficiente")
        elif n<=79: print("   → Bien")
        elif n<=89: print("   → Muy bien")
        else: print("   → Excelente")
    except ValueError:
        print("   Error: Número entero")


# ------------------- KATA 39 -------------------
def calcular_area(figura, datos):
    """Calcula área de figura."""
    if figura=="rectangulo": return datos[0]*datos[1]
    if figura=="circulo": return math.pi*datos[0]**2
    if figura=="triangulo": return 0.5*datos[0]*datos[1]
    raise ValueError("Figura no soportada")


# ------------------- KATA 40 -------------------
def compra_con_descuento():
    """Calcula precio con descuento interactivo."""
    try:
        p = float(input("   Precio: "))
        c = input("   ¿Cupón? (sí/no): ").lower() in ["sí","si"]
        d = float(input("   Descuento: ")) if c else 0
        print(f"   → Final: {p-d if d>0 else p}")
    except ValueError:
        print("   Error: Entrada inválida")


# ===================================================================
# EJECUCIÓN INTERACTIVA DE LAS 40 KATAS
# ===================================================================
if __name__ == "__main__":
    print("\n" + "="*80)
    print(" " * 20 + "40 KATAS DE PYTHON - MODO INTERACTIVO")
    print("="*80 + "\n")

    # KATA 1
    print("KATA 1 → Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados")
    texto = input("   Ingresa un texto: ") or "hola mundo"
    print(f"   → {contar_frecuencias_letras(texto)}")
    print("-"*50)

    # KATA 2
    print("KATA 2 → Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().")
    nums = input("   Ingresa números (ej: 1,2,3): ")
    nums = [int(x) for x in nums.split(",")] if nums else [1,2,3]
    print(f"   → {duplicar_lista(nums)}")
    print("-"*50)

    # KATA 3
    print("KATA 3 → Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.")
    palabras = input("   Ingresa palabras (ej: hola,mundo): ") or "hola,mundo,python"
    objetivo = input("   Buscar subcadena: ") or "on"
    palabras = palabras.split(",")
    print(f"   → {palabras_con_objetivo(palabras, objetivo)}")
    print("-"*50)

    # KATA 4
    print("KATA 4 → Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().")
    l1 = input("   Lista 1 (ej: 5,3,1): ") or "5,3,1"
    l2 = input("   Lista 2 (ej: 2,1,4): ") or "2,1,4"
    l1 = [int(x) for x in l1.split(",")]
    l2 = [int(x) for x in l2.split(",")]
    try:
        print(f"   → {diferencia_listas(l1, l2)}")
    except ValueError as e:
        print(f"   Error: {e}")
    print("-"*50)

    # KATA 5
    print("KATA 5 → Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota_aprobado. Si es así, el estado será aprobado; de lo contrario, suspenso. La función debe devolver una tupla que contenga la media y el estado.")

    notas = input("   Notas (ej: 6,7,4): ") or "6,7,4"
    notas = [float(x) for x in notas.split(",")]
    print(f"   → {evaluar_media(notas)}")
    print("-"*50)

    # KATA 6
    print("KATA 6 → Escribe una función que calcule el factorial de un número de manera recursiva.")
    n = input("   Ingresa un número: ") or "5"
    try:
        n = int(n)
        print(f"   → {factorial_recursivo(n)}")
    except ValueError:
        print("   Error: Número entero")
    print("-"*50)

    # KATA 7
    print("KATA 7 → Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()")
    tuplas = [(1,2), (3,'a')]  # No interactivo
    print(f"   → {tuplas_a_strings(tuplas)}")
    print("-"*50)

    # KATA 8
    print("KATA 8 → Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada y muestra un mensaje indicando si la división fue exitosa o no.")
    division_segura()
    print("-"*50)

    # KATA 9
    print("KATA 9 → Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es [Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso]. Usa la función filter().")
    mascotas = input("   Mascotas (ej: Perro,Tigre,Gato): ") or "Perro,Tigre,Gato"
    mascotas = mascotas.split(",")
    print(f"   → {filtrar_mascotas_prohibidas(mascotas)}")
    print("-"*50)

    # KATA 10
    print("KATA 10 → Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente")
    lst = input("   Números (ej: 1,2,3): ") or ""
    lst = [float(x) for x in lst.split(",")] if lst else []
    print(f"   → {promedio_lista(lst)}")
    print("-"*50)

    # KATA 11
    print("KATA 11 → Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente")
    validar_edad()
    print("-"*50)

    # KATA 12
    print("KATA 12 → Genera una función que, al recibir una frase, devuelva una lista con la longitud de cada palabra. Usa la función map()")
    frase = input("   Ingresa frase: ") or "hola mundo"
    print(f"   → {longitudes_palabras(frase)}")
    print("-"*50)

    # KATA 13
    print("KATA 13 → Genera una función que, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas. Usa la función map()")
    cad = input("   Ingresa texto: ") or "aAbBc"
    print(f"   → {mayus_minus_unicas(cad)}")
    print("-"*50)

    # KATA 14
    print("KATA 14 → Crea una función que retorne las palabras de una lista que comiencen con una letra en específico. Usa la función filter()")
    palabras = input("   Palabras (ej: ana,bob,carl): ") or "ana,bob,carl"
    letra = input("   Letra inicial: ") or "a"
    palabras = palabras.split(",")
    print(f"   → {palabras_con_inicio(palabras, letra)}")
    print("-"*50)

    # KATA 15
    print("KATA 15 → Crea una función lambda que sume 3 a cada número de una lista dada.")
    lst = input("   Números (ej: 1,2,3): ") or "1,2,3"
    lst = [int(x) for x in lst.split(",")]
    print(f"   → {sumar_tres(lst)}")
    print("-"*50)

    # KATA 16
    print("KATA 16 →Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función filter()")
    texto = input("   Texto: ") or "hola mundo python"
    n = int(input("   Longitud mínima: ") or 4)
    print(f"   → {palabras_largas(texto, n)}")
    print("-"*50)

    # KATA 17
    print("KATA 17 → Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa la función reduce().")
    digs = input("   Dígitos (ej: 5,7,2): ") or "5,7,2"
    digs = [int(x) for x in digs.split(",")]
    print(f"   → {digitos_a_numero(digs)}")
    print("-"*50)

    # KATA 18
    print("KATA 18 → Escribe un programa en Python que cree una lista de diccionarios con información de estudiantes (nombre, edad, calificación) y use filter para extraer a los estudiantes con una calificación mayor o igual a 90")
    print(f"   → {estudiantes_excelentes()}")
    print("-"*50)

    # KATA 19
    print("KATA 19 → Crea una función lambda que filtre los números impares de una lista dada.")
    lst = input("   Números (ej: 1,2,3,4): ") or "1,2,3,4"
    lst = [int(x) for x in lst.split(",")]
    print(f"   → {filtrar_impares(lst)}")
    print("-"*50)

    # KATA 20
    print("KATA 20 → Para una lista con elementos de tipo integer y string, obtén una nueva lista solo con los valores int. Usa la función filter().")
    lst = input("   Lista mixta (ej: 1,a,3): ") or "1,a,3"
    lst = [int(x) if x.isdigit() else x for x in lst.split(",")]
    print(f"   → {solo_enteros(lst)}")
    print("-"*50)

    # KATA 21
    print("KATA 21 → Crea una función que calcule el cubo de un número dado mediante una función lambda")
    x = input("   Número: ") or "3"
    try:
        x = int(x)
        print(f"   → {cubo(x)}")
    except ValueError:
        print("   Error: Número entero")
    print("-"*50)

    # KATA 22
    print("KATA 22 → Dada una lista numérica, obtén el producto total de los valores. Usa la función reduce()")
    lst = input("   Números (ej: 2,3,4): ") or "2,3,4"
    lst = [int(x) for x in lst.split(",")]
    print(f"   → {producto_total(lst)}")
    print("-"*50)

    # KATA 23
    print("KATA 23 → Concatena una lista de palabras. Usa la función reduce().")
    palabras = input("   Palabras (ej: hola,mundo): ") or "hola,mundo"
    palabras = palabras.split(",")
    print(f"   → {concatenar_palabras(palabras)}")
    print("-"*50)

    # KATA 24
    print("KATA 24 → Calcula la diferencia total en los valores de una lista. Usa la función reduce().")
    lst = input("   Números (ej: 10,3,2): ") or "10,3,2"
    lst = [int(x) for x in lst.split(",")]
    print(f"   → {diferencia_total(lst)}")
    print("-"*50)

    # KATA 25
    print("KATA 25 → Crea una función que cuente el número de caracteres en una cadena de texto dada.")
    texto = input("   Texto: ") or "python"
    print(f"   → {contar_caracteres(texto)} caracteres")
    print("-"*50)

    # KATA 26
    print("KATA 26 → Crea una función lambda que calcule el resto de la división entre dos números dados.")
    a = input("   Dividendo: ") or "10"
    b = input("   Divisor: ") or "3"
    try:
        a, b = int(a), int(b)
        print(f"   → {resto_division(a, b)}")
    except ValueError:
        print("   Error: Números enteros")
    print("-"*50)

    # KATA 27
    print("KATA 27 → Crea una función que calcule el promedio de una lista de números.")
    lst = input("   Números (ej: 1,2,3): ") or "1,2,3"
    lst = [float(x) for x in lst.split(",")]
    print(f"   → {promedio_numeros(lst)}")
    print("-"*50)

    # KATA 28
    print("KATA 28 → Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.")
    lst = input("   Lista (ej: 1,2,3,2): ") or "1,2,3,2"
    lst = [int(x) if x.isdigit() else x for x in lst.split(",")]
    print(f"   → {primer_duplicado(lst)}")
    print("-"*50)

    # KATA 29
    print("KATA 29 → Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#' excepto los últimos cuatro.")
    val = input("   Valor: ") or "123456789"
    print(f"   → {enmascarar_cadena(val)}")
    print("-"*50)

    # KATA 30
    print("KATA 30 → Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.")
    p1 = input("   Palabra 1: ") or "roma"
    p2 = input("   Palabra 2: ") or "mora"
    print(f"   → {son_anagramas(p1, p2)}")
    print("-"*50)

    # KATA 31
    print("KATA 31 → Crea una función que solicite al usuario ingresar una lista de nombres y luego un nombre para buscar en esa lista. Si el nombre está en la lista, imprime un mensaje indicando que fue encontrado; de lo contrario, lanza una excepción")
    buscar_nombre()
    print("-"*50)

    # KATA 32
    print("KATA 32 → Crea una función que tome un nombre completo y una lista de empleados, busque el nombre en la lista y devuelva el puesto del empleado si se encuentra; de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.")
    empleados = [{"nombre":"Ana","puesto":"Dev"},{"nombre":"Luis","puesto":"PM"}]
    nombre = input("   Nombre: ") or "Ana"
    print(f"   → {buscar_puesto(nombre, empleados)}")
    print("-"*50)

    # KATA 33
    print("KATA 33 → Crea una función lambda que sume elementos correspondientes de dos listas dadas")
    l1 = input("   Lista 1 (ej: 1,2): ") or "1,2"
    l2 = input("   Lista 2 (ej: 3,4): ") or "3,4"
    l1 = [int(x) for x in l1.split(",")]
    l2 = [int(x) for x in l2.split(",")]
    try:
        print(f"   → {sumar_listas(l1, l2)}")
    except ValueError:
        print("   Error: Listas deben tener misma longitud")
    print("-"*50)

    # KATA 34
    print("KATA 34 → Árbol simulado")
    a = Arbol()
    a.crecer_tronco()
    a.nueva_rama()
    a.crecer_ramas()
    print(f"   → {a.info_arbol()}")
    print("-"*50)

    # KATA 35
    print("KATA 35 → Banco simulado")
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    try:
        c = float(input("   Cantidad a transferir: ") or "20")
        alicia.transferir_dinero(c, bob)
        print(f"   → Alicia: {alicia.saldo}, Bob: {bob.saldo}")
    except ValueError as e:
        print(f"   Error: {e}")
    print("-"*50)

    # KATA 36
    print("KATA 36 → Procesar texto")
    texto = input("   Texto: ") or "hola hola mundo"
    opcion = input("   Opción (contar/reemplazar/eliminar): ") or "contar"
    if opcion == "reemplazar":
        a, b = input("   Original: "), input("   Nueva: ")
        print(f"   → {procesar_texto(texto, opcion, a, b)}")
    elif opcion == "eliminar":
        a = input("   Palabra a eliminar: ")
        print(f"   → {procesar_texto(texto, opcion, a)}")
    else:
        print(f"   → {procesar_texto(texto, opcion)}")
    print("-"*50)

    # KATA 37
    print("KATA 37 → Genera un programa que nos indique si es de noche, de día o de tarde según la hora proporcionada por el usuario.")
    momento_del_dia()
    print("-"*50)

    # KATA 38
    print("KATA 38 →Escribe un programa que determine qué calificación en texto tiene un alumno según su calificación numérica")
    calificacion_texto()
    print("-"*50)

    # KATA 39
    print("KATA 39 → Área de figura")
    figura = input("   Figura (rectangulo/circulo/triangulo): ") or "circulo"
    if figura == "circulo":
        r = float(input("   Radio: ") or 5)
        datos = (r,)
    else:
        b = float(input("   Base: ") or 4)
        h = float(input("   Altura: ") or 3)
        datos = (b,h)
    try:
        print(f"   → {calcular_area(figura, datos):.2f}")
    except ValueError as e:
        print(f"   Error: {e}")
    print("-"*50)

    # KATA 40
    print("KATA 40 → Compra con descuento")
    compra_con_descuento()
    print("-"*50)

    print("="*80)
    print(" " * 28 + "¡fin siuuuu!")
    print("="*80 + "\n")