import hashlib
import os
import sys
import pyfiglet
from colorama import Fore, Style, init


init(autoreset=True)

def print_header():
 
    os.system('cls' if os.name == 'nt' else 'clear')
    
   
    title = pyfiglet.figlet_format("Xhash v 1.0", font="varsity")
    

    print(Fore.CYAN + title)
    
   
    print(Fore.YELLOW + "by Rodolfo Hernandez Baz aKa Pr@FesOr X")
    print("-" * 60)

def print_menu():
  
    print(Fore.LIGHTBLACK_EX + "\n[ MENÚ PRINCIPAL ]")
    print(Fore.GREEN + "1." + Fore.WHITE + " Detectar Hash")
    print(Fore.GREEN + "2." + Fore.WHITE + " Generar Hash")
    print(Fore.GREEN + "3." + Fore.WHITE + " Comparar Archivos")
    print(Fore.GREEN + "4." + Fore.WHITE + " Crackear Hash")
    print(Fore.GREEN + "5." + Fore.WHITE + " About")
    print(Fore.RED + "6." + Fore.WHITE + " Salir")
    print("-" * 60)

def is_hex(s):
   
    try:
        int(s, 16)
        return True
    except ValueError:
        return False

def detect_hash():
  
    print(Fore.CYAN + "\n[ DETECTOR DE HASH ]")
    input_hash = input(Fore.WHITE + "Ingresa el hash a analizar: ").strip()
    
    if not input_hash:
        print(Fore.RED + "Error: No se ingresó ningún valor.")
        return

    length = len(input_hash)
    is_hex_str = is_hex(input_hash)
    
    result = {
        "type": "Desconocido",
        "bits": "N/A",
        "desc": "No se pudo identificar el patrón."
    }

    
    if input_hash.startswith("$2a$") or input_hash.startswith("$2b$") or input_hash.startswith("$2y$"):
        result = {"type": "Bcrypt", "bits": "184 bits", "desc": "Algoritmo basado en Blowfish."}
    elif input_hash.startswith("$6$"):
        result = {"type": "SHA-512 Crypt", "bits": "512 bits", "desc": "SHA-512 con Salt de Linux."}
    elif input_hash.startswith("$5$"):
        result = {"type": "SHA-256 Crypt", "bits": "256 bits", "desc": "SHA-256 con Salt de Linux."}
    elif length == 32 and is_hex_str:
        result = {"type": "MD5", "bits": "128 bits", "desc": "Común para checksums y legacy."}
    elif length == 40 and is_hex_str:
        result = {"type": "SHA-1", "bits": "160 bits", "desc": "Estándar antiguo, inseguro."}
    elif length == 56 and is_hex_str:
        result = {"type": "SHA-224", "bits": "224 bits", "desc": "Variante truncada de SHA-256."}
    elif length == 64 and is_hex_str:
        result = {"type": "SHA-256", "bits": "256 bits", "desc": "Estándar actual (Bitcoin, SSL)."}
    elif length == 96 and is_hex_str:
        result = {"type": "SHA-384", "bits": "384 bits", "desc": "Variante intermedia SHA-2."}
    elif length == 128 and is_hex_str:
        result = {"type": "SHA-512", "bits": "512 bits", "desc": "Robusta para arquitecturas 64 bits."}
    
    print(Fore.MAGENTA + "\n--- RESULTADO ---")
    print(Fore.YELLOW + f"Tipo:     {Fore.WHITE}{result['type']}")
    print(Fore.YELLOW + f"Bits:     {Fore.WHITE}{result['bits']}")
    print(Fore.YELLOW + f"Longitud: {Fore.WHITE}{length} caracteres")
    print(Fore.YELLOW + f"Info:     {Fore.LIGHTBLACK_EX}{result['desc']}")
    input(Fore.LIGHTBLACK_EX + "\nPresiona Enter para continuar...")

def generate_hash():
 
    print(Fore.CYAN + "\n[ GENERADOR DE HASHES ]")
    print("1. Ingresar Texto")
    print("2. Seleccionar Archivo")
    opt = input("Opción: ").strip()

    data = None
    source_name = ""

    if opt == '1':
        text = input("Ingresa el texto: ")
        if not text: return
        data = text.encode('utf-8')
        source_name = "Texto ingresado"
    elif opt == '2':
        path = input("Ruta del archivo: ").strip()
        if not os.path.exists(path):
            print(Fore.RED + "Archivo no encontrado.")
            return
        with open(path, 'rb') as f:
            data = f.read()
        source_name = os.path.basename(path)
    else:
        print(Fore.RED + "Opción inválida.")
        return

    print(Fore.MAGENTA + f"\n--- HASHES PARA: {source_name} ---")
    
  
    algorithms = [
        ('MD5', hashlib.md5),
        ('SHA-1', hashlib.sha1),
        ('SHA-224', hashlib.sha224),
        ('SHA-256', hashlib.sha256),
        ('SHA-384', hashlib.sha384),
        ('SHA-512', hashlib.sha512),
        ('SHA3-224', lambda: hashlib.sha3_224()),
        ('SHA3-256', lambda: hashlib.sha3_256()),
        ('SHA3-384', lambda: hashlib.sha3_384()),
        ('SHA3-512', lambda: hashlib.sha3_512()),
    ]

    for name, func in algorithms:
        try:
            if callable(func) and not isinstance(func, type):
                h = func().update(data) # Caso lambda
                # Corrección: lambdas requieren instancia directa
                h_obj = func()
                h_obj.update(data)
                print(f"{Fore.YELLOW}{name}:{Fore.WHITE} {h_obj.hexdigest()}")
            else:
                h_obj = func(data)
                print(f"{Fore.YELLOW}{name}:{Fore.WHITE} {h_obj.hexdigest()}")
        except Exception:
            pass 

    input(Fore.LIGHTBLACK_EX + "\nPresiona Enter para continuar...")

def compare_files():
   
    print(Fore.CYAN + "\n[ COMPARADOR DE ARCHIVOS ]")
    path_a = input("Ruta Archivo A: ").strip()
    path_b = input("Ruta Archivo B: ").strip()

    if not os.path.exists(path_a) or not os.path.exists(path_b):
        print(Fore.RED + "Uno o ambos archivos no existen.")
        return

    print(Fore.YELLOW + "\nCalculando hashes...")
    
    try:
        with open(path_a, 'rb') as f: hash_a = hashlib.sha256(f.read()).hexdigest()
        with open(path_b, 'rb') as f: hash_b = hashlib.sha256(f.read()).hexdigest()

        print(f"{Fore.WHITE}Archivo A: {hash_a}")
        print(f"{Fore.WHITE}Archivo B: {hash_b}")

        if hash_a == hash_b:
            print(Fore.GREEN + "\nRESULTADO: LOS ARCHIVOS SON IDÉNTICOS")
        else:
            print(Fore.RED + "\nRESULTADO: LOS ARCHIVOS SON DIFERENTES")
    except Exception as e:
        print(Fore.RED + f"Error: {e}")

    input(Fore.LIGHTBLACK_EX + "\nPresiona Enter para continuar...")

def crack_hash():
   
    print(Fore.CYAN + "\n[ CRACKING DE HASH ]")
    target = input("Hash objetivo: ").strip().lower()
    dict_path = input("Ruta del diccionario (.txt): ").strip()

    if not os.path.exists(dict_path):
        print(Fore.RED + "Diccionario no encontrado.")
        return


    algo = None
    if len(target) == 32: algo = hashlib.md5
    elif len(target) == 40: algo = hashlib.sha1
    elif len(target) == 64: algo = hashlib.sha256
    elif len(target) == 128: algo = hashlib.sha512
    
    if not algo:
        print(Fore.RED + "Tipo de hash no soportado para cracking (MD5, SHA1, SHA256, SHA512).")
        return

    print(Fore.YELLOW + f"\nIniciando ataque con diccionario: {os.path.basename(dict_path)}")
    
    try:
        found = False
        count = 0
        with open(dict_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                word = line.strip()
                count += 1
            
                if count % 1000 == 0:
                    print(f"\r{Fore.LIGHTBLACK_EX}Intentos: {count}...", end="")

                hashed_word = algo(word.encode('utf-8')).hexdigest()
                if hashed_word == target:
                    print(Fore.GREEN + f"\n\n¡PASSWORD ENCONTRADO!")
                    print(Fore.YELLOW + f"Password: {Fore.WHITE}{word}")
                    print(Fore.YELLOW + f"Intentos: {count}")
                    found = True
                    break
        
        if not found:
            print(Fore.RED + f"\n\nNo encontrado en {count} intentos.")
            
    except Exception as e:
        print(Fore.RED + f"\nError leyendo diccionario: {e}")

    input(Fore.LIGHTBLACK_EX + "\nPresiona Enter para continuar...")

def show_about():
   
    print(Fore.CYAN + "\n[ ABOUT ]")
    print(Fore.WHITE + "Programador: " + Fore.YELLOW + "Rodolfo Hernandez Baz aKa Pr@FesOr X")
    print("\n" + Fore.WHITE + Style.BRIGHT + "Características y Funcionamiento:")
    print(Fore.LIGHTBLACK_EX + 
    """
    XHash Analizer v 1.0 es una herramienta CLI diseñada 
    para el análisis criptográfico y la ciberseguridad.
    
    - Detección de Hash: Identificación automática de algoritmos.
    - Generación de Hash: Soporte para múltiples algoritmos simultáneos.
    - Comparación de Archivos: Verificación de integridad SHA-256.
    - Cracking de Hashes: Ataque de diccionario offline.
    
    Recursos:
    Se recomienda usar diccionarios como 'Rockyou.txt' para pruebas.
    """)
    input(Fore.LIGHTBLACK_EX + "\nPresiona Enter para continuar...")

def main():

    while True:
        print_header()
        print_menu()
        
        choice = input(Fore.LIGHTGREEN_EX + "\nRhino > " + Fore.WHITE)
        
        if choice == '1':
            detect_hash()
        elif choice == '2':
            generate_hash()
        elif choice == '3':
            compare_files()
        elif choice == '4':
            crack_hash()
        elif choice == '5':
            show_about()
        elif choice == '6':
            print(Fore.RED + "Saliendo...")
            sys.exit()
        else:
            print(Fore.RED + "Opción no válida.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()