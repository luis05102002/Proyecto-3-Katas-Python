# -*- coding: utf-8 -*-
"""
40 KATAS DE PYTHON - MODO INTERACTIVO ÉPICO
Autor: Don Luis Gómez Del Moral
"""

# ===================================================================
# IMPORTS
# ===================================================================
import math
from functools import reduce


# ===================================================================
# KATAS (1 a 40) - Funciones originales
# ===================================================================

# ------------------- KATA 1 -------------------
def contar_frecuencias_letras(texto):
    texto = texto.replace(" ", "")
    frec = {}
    for c in texto:
        frec[c] = frec.get(c, 0) + 1
    return frec

# ------------------- KATA 2 -------------------
def duplicar_lista(lista):
    return list(map(lambda x: x * 2, lista))

# ------------------- KATA 3 -------------------
def palabras_con_objetivo(lista_palabras, objetivo):
    return [p for p in lista_palabras if objetivo in p]

# ------------------- KATA 4 -------------------
def diferencia_listas(l1, l2):
    if len(l1) != len(l2): raise ValueError("Misma longitud")
    return list(map(lambda a, b: a - b, l1, l2))

# ------------------- KATA 5 -------------------
def evaluar_media(notas, aprob=5):
    media = 0 if not notas else sum(notas)/len(notas)
    return (media, "aprobado" if media >= aprob else "suspenso")

# ------------------- KATA 6 -------------------
def factorial_recursivo(n):
    return 1 if n in (0,1) else n * factorial_recursivo(n-1)

# ------------------- KATA 7 -------------------
def tuplas_a_strings(tuplas):
    return list(map(lambda t: ''.join(map(str, t)), tuplas))

# ------------------- KATA 8 -------------------
def division_segura():
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
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, mascotas))

# ------------------- KATA 10 -------------------
class ListaVaciaError(Exception): pass
def promedio_lista(lst):
    try:
        if not lst: raise ListaVaciaError("Lista vacía")
        return sum(lst)/len(lst)
    except ListaVaciaError as e: print(f"   {e}"); return None

# ------------------- KATA 11 -------------------
def validar_edad():
    try:
        e = int(input("   Edad: "))
        if not 0<=e<=120: raise ValueError("Fuera de rango")
        print(f"   → Edad válida: {e}")
    except ValueError:
        print("   Error: Número entero entre 0 y 120")

# ------------------- KATA 12 -------------------
def longitudes_palabras(frase):
    return list(map(len, frase.split()))

# ------------------- KATA 13 -------------------
def mayus_minus_unicas(cad):
    unicas = {c.lower() for c in cad if c.isalpha()}
    return [(c.upper(), c.lower()) for c in unicas]

# ------------------- KATA 14 -------------------
def palabras_con_inicio(palabras, letra):
    return list(filter(lambda p: p.startswith(letra), palabras))

# ------------------- KATA 15 -------------------
sumar_tres = lambda lst: list(map(lambda x: x+3, lst))

# ------------------- KATA 16 -------------------
def palabras_largas(texto, n):
    return list(filter(lambda p: len(p)>n, texto.split()))

# ------------------- KATA 17 -------------------
def digitos_a_numero(digs):
    return reduce(lambda a,d: a*10+d, digs, 0)

# ------------------- KATA 18 -------------------
def estudiantes_excelentes():
    est = [{"nombre":"Ana","calificacion":95},{"nombre":"Luis","calificacion":88},{"nombre":"Marta","calificacion":92}]
    return list(filter(lambda e: e["calificacion"]>=90, est))

# ------------------- KATA 19 -------------------
filtrar_impares = lambda lst: list(filter(lambda x: x%2!=0, lst))

# ------------------- KATA 20 -------------------
def solo_enteros(lst):
    return list(filter(lambda x: isinstance(x,int), lst))

# ------------------- KATA 21 -------------------
cubo = lambda x: x**3

# ------------------- KATA 22 -------------------
def producto_total(lst):
    return reduce(lambda a,x: a*x, lst, 1)

# ------------------- KATA 23 -------------------
def concatenar_palabras(lst):
    return reduce(lambda a,p: a+p, lst, "")

# ------------------- KATA 24 -------------------
def diferencia_total(lst):
    return 0 if not lst else reduce(lambda a,x: a-x, lst, lst[0])

# ------------------- KATA 25 -------------------
def contar_caracteres(texto):
    return len(texto)

# ------------------- KATA 26 -------------------
resto_division = lambda a,b: a%b

# ------------------- KATA 27 -------------------
def promedio_numeros(lst):
    return 0 if not lst else sum(lst)/len(lst)

# ------------------- KATA 28 -------------------
def primer_duplicado(lst):
    s = set()
    for x in lst:
        if x in s: return x
        s.add(x)
    return None

# ------------------- KATA 29 -------------------
def enmascarar_cadena(val):
    s = str(val)
    return s if len(s)<=4 else '#'*(len(s)-4) + s[-4:]

# ------------------- KATA 30 -------------------
def son_anagramas(p1,p2):
    return sorted(p1.lower()) == sorted(p2.lower())

# ------------------- KATA 31 -------------------
class NombreNoEncontrado(Exception): pass
def buscar_nombre():
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
    try:
        h = int(input("   Hora (0-23): "))
        if 0<=h<6 or h>=18: print("   → Noche")
        elif h<12: print("   → Mañana")
        else: print("   → Tarde")
    except ValueError:
        print("   Error: Ingresa 0-23")

# ------------------- KATA 38 -------------------
def calificacion_texto():
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
    if figura=="rectangulo": return datos[0]*datos[1]
    if figura=="circulo": return math.pi*datos[0]**2
    if figura=="triangulo": return 0.5*datos[0]*datos[1]
    raise ValueError("Figura no soportada")

# ------------------- KATA 40 -------------------
def compra_con_descuento():
    try:
        p = float(input("   Precio: "))
        c = input("   ¿Cupón? (sí/no): ").lower() in ["sí","si"]
        d = float(input("   Descuento: ")) if c else 0
        print(f"   → Final: {p-d if d>0 else p}")
    except ValueError:
        print("   Error: Entrada inválida")


# ===================================================================
# ENVOLTURAS DE KATAS PARA MENÚ (SIN TÍTULOS DUPLICADOS)
# ===================================================================

def kata_1():
    texto = input("   Texto: ") or "hola mundo"
    print(f"   → {contar_frecuencias_letras(texto)}")

def kata_2():
    nums = input("   Números (1,2,3): ") or "1,2,3"
    nums = [int(x) for x in nums.split(",")]
    print(f"   → {duplicar_lista(nums)}")

def kata_3():
    palabras_input = input("   Palabras (separadas por coma): ") or "hola,mundo,python"
    obj = input("   Buscar subcadena: ") or "on"
    palabras = [p.strip() for p in palabras_input.split(",")]
    print(f"   → {palabras_con_objetivo(palabras, obj)}")

def kata_4():
    l1 = input("   Lista 1 (5,3,1): ") or "5,3,1"
    l2 = input("   Lista 2 (2,1,4): ") or "2,1,4"
    l1 = [int(x) for x in l1.split(",")]
    l2 = [int(x) for x in l2.split(",")]
    try:
        print(f"   → {diferencia_listas(l1, l2)}")
    except ValueError as e:
        print(f"   Error: {e}")

def kata_5():
    notas = input("   Notas (6,7,4): ") or "6,7,4"
    notas = [float(x) for x in notas.split(",")]
    print(f"   → {evaluar_media(notas)}")

def kata_6():
    n = input("   Número: ") or "5"
    try:
        n = int(n)
        print(f"   → {factorial_recursivo(n)}")
    except ValueError:
        print("   Error: Número entero")

def kata_7():
    tuplas = [(1,2), (3,'a')]
    print(f"   → {tuplas_a_strings(tuplas)}")

def kata_8():
    division_segura()

def kata_9():
    mascotas = input("   Mascotas (Perro,Tigre): ") or "Perro,Tigre,Gato"
    print(f"   → {filtrar_mascotas_prohibidas(mascotas.split(','))}")

def kata_10():
    lst = input("   Números (1,2,3): ") or ""
    lst = [float(x) for x in lst.split(",")] if lst else []
    print(f"   → {promedio_lista(lst)}")

def kata_11():
    validar_edad()

def kata_12():
    frase = input("   Frase: ") or "hola mundo"
    print(f"   → {longitudes_palabras(frase)}")

def kata_13():
    cad = input("   Texto: ") or "aAbBc"
    print(f"   → {mayus_minus_unicas(cad)}")

def kata_14():
    palabras = input("   Palabras (ana,bob): ") or "ana,bob,carl"
    letra = input("   Letra: ") or "a"
    print(f"   → {palabras_con_inicio(palabras.split(','), letra)}")

def kata_15():
    lst = input("   Números (1,2,3): ") or "1,2,3"
    lst = [int(x) for x in lst.split(",")]
    print(f"   → {sumar_tres(lst)}")

def kata_16():
    texto = input("   Texto: ") or "hola mundo python"
    n = int(input("   Mínimo: ") or 4)
    print(f"   → {palabras_largas(texto, n)}")

def kata_17():
    digs = input("   Dígitos (5,7,2): ") or "5,7,2"
    digs = [int(x) for x in digs.split(",")]
    print(f"   → {digitos_a_numero(digs)}")

def kata_18():
    print(f"   → {estudiantes_excelentes()}")

def kata_19():
    lst = input("   Números (1,2,3,4): ") or "1,2,3,4"
    lst = [int(x) for x in lst.split(",")]
    print(f"   → {filtrar_impares(lst)}")

def kata_20():
    lst = input("   Lista (1,a,3): ") or "1,a,3"
    lst = [int(x) if x.isdigit() else x for x in lst.split(",")]
    print(f"   → {solo_enteros(lst)}")

def kata_21():
    x = input("   Número: ") or "3"
    try:
        x = int(x)
        print(f"   → {cubo(x)}")
    except ValueError:
        print("   Error: Número entero")

def kata_22():
    lst = input("   Números (2,3,4): ") or "2,3,4"
    lst = [int(x) for x in lst.split(",")]
    print(f"   → {producto_total(lst)}")

def kata_23():
    palabras = input("   Palabras (hola,mundo): ") or "hola,mundo"
    print(f"   → {concatenar_palabras(palabras.split(','))}")

def kata_24():
    lst = input("   Números (10,3,2): ") or "10,3,2"
    lst = [int(x) for x in lst.split(",")]
    print(f"   → {diferencia_total(lst)}")

def kata_25():
    texto = input("   Texto: ") or "python"
    print(f"   → {contar_caracteres(texto)} caracteres")

def kata_26():
    a = input("   Dividendo: ") or "10"
    b = input("   Divisor: ") or "3"
    try:
        a, b = int(a), int(b)
        print(f"   → {resto_division(a, b)}")
    except ValueError:
        print("   Error: Números enteros")

def kata_27():
    lst = input("   Números (1,2,3): ") or "1,2,3"
    lst = [float(x) for x in lst.split(",")]
    print(f"   → {promedio_numeros(lst)}")

def kata_28():
    lst = input("   Lista (1,2,3,2): ") or "1,2,3,2"
    lst = [int(x) if x.isdigit() else x for x in lst.split(",")]
    print(f"   → {primer_duplicado(lst)}")

def kata_29():
    val = input("   Valor: ") or "123456789"
    print(f"   → {enmascarar_cadena(val)}")

def kata_30():
    p1 = input("   Palabra 1: ") or "roma"
    p2 = input("   Palabra 2: ") or "mora"
    print(f"   → {son_anagramas(p1, p2)}")

def kata_31():
    buscar_nombre()

def kata_32():
    empleados = [{"nombre":"Ana","puesto":"Dev"},{"nombre":"Luis","puesto":"PM"}]
    nombre = input("   Nombre: ") or "Ana"
    print(f"   → {buscar_puesto(nombre, empleados)}")

def kata_33():
    l1 = input("   Lista 1 (1,2): ") or "1,2"
    l2 = input("   Lista 2 (3,4): ") or "3,4"
    l1 = [int(x) for x in l1.split(",")]
    l2 = [int(x) for x in l2.split(",")]
    if len(l1) != len(l2):
        print("   Error: Listas deben tener misma longitud")
    else:
        print(f"   → {sumar_listas(l1, l2)}")

def kata_34():
    a = Arbol()
    a.crecer_tronco()
    a.nueva_rama()
    a.crecer_ramas()
    print(f"   → {a.info_arbol()}")

def kata_35():
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    try:
        c = float(input("   Cantidad a transferir: ") or "20")
        alicia.transferir_dinero(c, bob)
        print(f"   → Alicia: {alicia.saldo}, Bob: {bob.saldo}")
    except ValueError as e:
        print(f"   Error: {e}")

def kata_36():
    texto = input("   Texto: ") or "hola hola mundo"
    opcion = input("   Opción (contar/reemplazar/eliminar): ").strip().lower() or "contar"
    try:
        if opcion == "reemplazar":
            a, b = input("   Original: "), input("   Nueva: ")
            print(f"   → {procesar_texto(texto, opcion, a, b)}")
        elif opcion == "eliminar":
            a = input("   Palabra a eliminar: ")
            print(f"   → {procesar_texto(texto, opcion, a)}")
        else:
            print(f"   → {procesar_texto(texto, opcion)}")
    except ValueError as e:
        print(f"   Error: {e}")

def kata_37():
    momento_del_dia()

def kata_38():
    calificacion_texto()

def kata_39():
    figura = input("   Figura (rectangulo/circulo/triangulo): ").strip().lower() or "circulo"
    try:
        if figura == "circulo":
            r = float(input("   Radio: ") or 5)
            datos = (r,)
        else:
            b = float(input("   Base: ") or 4)
            h = float(input("   Altura: ") or 3)
            datos = (b,h)
        print(f"   → {calcular_area(figura, datos):.2f}")
    except ValueError as e:
        print(f"   Error: {e}")

def kata_40():
    compra_con_descuento()


# ===================================================================
# MENÚ PRINCIPAL ÉPICO
# ===================================================================
def menu_epico():
    katas = {
        "1": ("Frecuencia de letras", kata_1),
        "2": ("Duplicar lista", kata_2),
        "3": ("Palabras con objetivo", kata_3),
        "4": ("Diferencia listas", kata_4),
        "5": ("Evaluar media", kata_5),
        "6": ("Factorial", kata_6),
        "7": ("Tuplas a strings", kata_7),
        "8": ("División segura", kata_8),
        "9": ("Mascotas", kata_9),
        "10": ("Promedio", kata_10),
        "11": ("Validar edad", kata_11),
        "12": ("Longitud palabras", kata_12),
        "13": ("Mayús/min", kata_13),
        "14": ("Palabras inicio", kata_14),
        "15": ("Sumar 3", kata_15),
        "16": ("Palabras largas", kata_16),
        "17": ("Dígitos a número", kata_17),
        "18": ("Estudiantes", kata_18),
        "19": ("Impares", kata_19),
        "20": ("Solo enteros", kata_20),
        "21": ("Cubo", kata_21),
        "22": ("Producto", kata_22),
        "23": ("Concatenar", kata_23),
        "24": ("Diferencia total", kata_24),
        "25": ("Caracteres", kata_25),
        "26": ("Resto", kata_26),
        "27": ("Promedio", kata_27),
        "28": ("Duplicado", kata_28),
        "29": ("Enmascarar", kata_29),
        "30": ("Anagramas", kata_30),
        "31": ("Buscar nombre", kata_31),
        "32": ("Buscar puesto", kata_32),
        "33": ("Sumar listas", kata_33),
        "34": ("Árbol", kata_34),
        "35": ("Banco", kata_35),
        "36": ("Procesar texto", kata_36),
        "37": ("Momento día", kata_37),
        "38": ("Calificación", kata_38),
        "39": ("Área", kata_39),
        "40": ("Compra", kata_40),
    }

    while True:
        print("\n" + "═" * 80)
        print(" " * 25 + "LAS AVENTURAS DE PYTHON")
        print(" " * 20 + "Elige tu kata (1-40) | 'todas' | 'salir'")
        print("═" * 80)

        opcion = input("\n  TU ELECCIÓN → ").strip().lower()

        if opcion == "salir":
            print("\n" + "═" * 80)
            print(" " * 28 + "¡SIIIIUUUUU! NOS VEMOS")
            print("═" * 80 + "\n")
            break

        if opcion == "todas":
            print("\nEJECUTANDO TODAS LAS KATAS...\n")
            for num, (nombre, func) in katas.items():
                print(f"KATA {num} → {nombre}")
                try:
                    func()
                except Exception as e:
                    print(f"   Error: {e}")
                print("-" * 50)
            continue

        if opcion in katas:
            nombre, func = katas[opcion]
            print(f"\nKATA {opcion} → {nombre}")
            try:
                func()
            except Exception as e:
                print(f"   Error: {e}")
            print("-" * 50)
        else:
            print("   Opción inválida. Usa 1-40, 'todas' o 'salir'")


# ===================================================================
# EJECUCIÓN
# ===================================================================
if __name__ == "__main__":
    menu_epico()