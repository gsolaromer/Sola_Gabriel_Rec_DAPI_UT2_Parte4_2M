import csv

ruta = "C:\\Users\\gabri\\Escritorio\\GIT_gsolaromerEduca\\Sola_Gabriel_Rec_DAPI_UT2_Parte4_2M\\class.csv"

def process_class(ruta):
   
    """Tras leer los datos, se deberá llamar a las dos funciones creadas 
    en las partes 2 y 3 para obtener los nuevos datos de cada 
    alumno/a (email, nota final y aprobado/suspendido). 
    Los nuevos datos se deberán almacenar en una lista de diccionarios 
    según el formato indicado más adelante, y se deberá guardar esa lista 
    de diccionarios en un nuevo fichero CSV.

    Parámetros:

    - Fichero class.csv
    - Funciones de las partes 1, 2 y 3.
    - Lista de diccionarios
    - Fichero grades.csv
    
    Salida:

    - Fichero grades.csv con la lista de diccionarios guardada."""

    alumnado = []
    resultados = []
    correos = []

    with open(ruta, "r", encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for fila in reader:

            nombre = fila['Nombre']

            apellido = fila['Apellido']

            primera_letra_nombre = nombre[0].lower()

            cinco_letras_apellido = apellido[:5].lower()

            correo = primera_letra_nombre + cinco_letras_apellido + "@educacion.navarra.es"

            Practica01 = float(fila['Practica01'].replace(",", "."))

            Practica02 = float(fila['Practica02'].replace(",", "."))

            Practica03 = float(fila['Practica03'].replace(",", "."))

            Examen = float(fila['Examen'].replace(",", "."))

            Recuperacion = float(fila['Recuperacion'].replace(",", "."))

            Actitud = float(fila['Actitud'].replace(",", "."))

            NotaFinal = (Practica01 + Practica02 + Practica03) / 3 * 0.3 + max(Examen, Recuperacion) * 0.6 + Actitud * 0.1

            NotaFinal = round(NotaFinal, 2)

            aprobado = NotaFinal >= 5

            datos_alumno = {

                'Nombre': nombre,

                'Apellido': apellido,

                'Email': correo,

                'Nota Final': NotaFinal,

                'Aprobado/suspendido': 'Aprobado' if aprobado else 'Suspendido'

            }

            alumnado.append(datos_alumno)

            correos.append(correo)

            resultados.append((NotaFinal, aprobado))

    with open('grades.csv', 'w', newline='', encoding="UTF-8") as csvfile:
        fieldnames = ['Nombre', 'Apellido', 'Email', 'Nota Final', 'Aprobado/suspendido']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for alumno in alumnado:
            writer.writerow(alumno)

process_class(ruta)