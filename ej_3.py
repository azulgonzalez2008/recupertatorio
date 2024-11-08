import requests

def buscar_en_posts(usuario_id, palabra_clave):
    # Verificar que el usuario_id esté en el rango permitido
    if usuario_id < 1 or usuario_id > 10:
        print("Error: El ID de usuario no es válido. Debe estar entre 1 y 10.")
        return

    # Obtener los posts desde JSONPlaceholder
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Verificar que la solicitud fue exitosa
    if response.status_code != 200:
        print("Error al obtener los posts.")
        return

    # Filtrar los posts por usuario
    posts = response.json()
    posts_usuario = [post for post in posts if post["userId"] == usuario_id]

    # Realizar la búsqueda de la palabra clave en cada post
    ocurrencias_totales = 0
    resultados = []

    for post in posts_usuario:
        conteo_palabra = (
            post["title"].lower().count(palabra_clave.lower()) +
            post["body"].lower().count(palabra_clave.lower())
        )

        if conteo_palabra > 0:
            resultados.append({"post_id": post["id"], "ocurrencias": conteo_palabra})
            ocurrencias_totales += conteo_palabra

    # Mostrar los resultados
    if resultados:
        print(f"\nPost ID  Ocurrencias de '{palabra_clave}'")
        for resultado in resultados:
            print(f"{resultado['post_id']}       {resultado['ocurrencias']}")
        print(f"\nTotal de ocurrencias de '{palabra_clave}': {ocurrencias_totales} veces")
    else:
        print(f"No se encontraron coincidencias de '{palabra_clave}' en los posts del usuario {usuario_id}.")

# Solicitar el ID de usuario y la palabra clave al usuario
try:
    usuario_id = int(input("Ingresa el ID de usuario (1-10): "))
    palabra_clave = input("Ingresa una palabra clave para buscar: ").strip()
    buscar_en_posts(usuario_id, palabra_clave)
except ValueError:
    print("Error: Debes ingresar un número para el ID de usuario.")
