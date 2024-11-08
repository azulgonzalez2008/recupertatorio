import request
import json

def amount_users():    
     while True:
        try:
      n = int(input("Ingresa la cantidad de usuarios (n) que deseas obtener (1 <= n <= 10): "))
            if 1 <= n <= 10:
                return n
                   else:
                print("Error: El valor debe estar entre 1 y 10.")
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")

def get_users(n):       
       url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

      if response.status_code == 200:
        users = response.json()
        return users[:n]
        
     else:
      print("Error: No se pudo obtener la lista de usuarios.")
       return []               

def divide_name(user):
    vowels = ['a', 'e', 'i', 'o', 'u']
    users_vowels = []
    users_consonants = []

 for usuario in usuarios:
        nombre = user['name']
        if nombre[0].lower() in 'aeiou':
            users_vowels.append(user)

 else:
            users_consonants.append(user)
    
    return users_vowels, users_consonants

def save_to_file(users, name_file):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(usuarios, archivo, indent=4)    

def main():
    n = obtener_cantidad_usuarios()
    usuarios = obtener_usuarios(n)
    
    if users:
       users_vowels,users_consonants = divide_users(users)
        save_to_file(users_vowels, "UsersData/usersVowels.json")
        save_to_file(users_consonants, "UsersData/usersConsonants.json")
        
        print("Los datos de los usuarios se han guardado en los archivos JSON correspondientes.")

main()        