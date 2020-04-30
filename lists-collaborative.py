# César López Grupo: 201

# La escuela Justo Sierra está contratando developers para 
# que desarrollen una aplicación que les permita administrar
# listas de alumnos para sus distintos grupos.
# Sus necesidades son las siguientes:




# Listas Justo Sierra

# Lista201 
# Grupo   Nombre          Matrícula
# 201     Alexandra Olea  198736455
# 201     Osvaldo Pulido  198374638
# 201     Julian Robal    195325635

# Lista202 
# Grupo   Nombre            Matrícula
# 202     Eduardo Olivares  196353265
# 202     Daniel Salado     198273645
# 202     Estrella Terrazas 197364632

# .
# .
# .
# listasGenerales = [
#   [
#     201, 
#     ["Alexandra Olea", 1928373726, 2019], 
#     ["Osvaldo Pulido", 1928732832, 2019], 
#     ["Julian Robal", 1928236626, 2019]
#   ],

#   [
#     202, 
#     ["Eduardo Olivares", 192837263, 2019],     
#     ["Estrella Terrazas", 19823762, 2019]
#   ],

#   [
#     203,
#     ["Daniel Salado", 192837263, 2019],
#   ]
# ]

# Mostrar el índice del dato 201
# for lista in listasGenerales:
#   #print(primerNivel)
#   if 203 in lista:
#     print(lista)
#     break
    

listasGenerales = []

# - Registrar nombre completo y matrícula de los alumnos. --> OK
# - Llevar registro de a qué grupo pertenece cada alumno. --> OK
# - Registrar el año de ingreso por alumno. --> OK
def agregaLista(listaGrupo):
  listasGenerales.append(listaGrupo)
  return
  

def capturaInfo():
  lista = []
  grupo = int(input('Escribe el grupo: '))
  lista.append(grupo)
  while True:
    nombre = input('Escribe el nombre completo del alumno: ')
    matricula = int(input('Escribe la matrícula del alumno: '))
    anioIngreso = int(input('Escribe el año de ingreso del alumno: '))
    lista.append([nombre, matricula, anioIngreso])
    opc = input('Deseas agregar más alumnos? (s/n): ')
    if(opc == 'n' or opc == 'N'):
      # Llamamos a la función agregaLista con la nueva lista capturada
      agregaLista(lista)
      break
  return

# capturaInfo()
# print(listasGenerales)
# capturaInfo()
# print(listasGenerales)
# capturaInfo()
# print(listasGenerales)


# - Elaborar listas de alumnos por grupo. -->OK

# Grupo: 201
# Matrícula       Nombres
# 19384756        Gilberto López
# 19827364        Alexandra Olea

def buscarGrupo(grupo):
  for lista in listasGenerales:
    if grupo in lista:
      return lista

def mostrarLista(grupo):
  lista = buscarGrupo(grupo)
  print('Grupo:',lista[0])
  print('Matrícula\t Nombres')
  for alumno in range(len(lista)):
    if alumno != 0:
      print(lista[alumno][1],'\t',lista[alumno][0])

# mostrarLista(202)

# - Agregar y eliminar alumnos de un grupo. 
def agregaAlumno():
  grupo = int(input('A qué grupo se va a agregar el alumno: '))
  lista = buscarGrupo(grupo)
  nombre = input('Nombre del alumno: ')
  matricula = int(input('Matrícula del alumno: '))
  anioIngreso = int(input('Año de ingreso: '))
  # alumno = [nombre, matricula, anioIngreso]
  # lista.append(alumno)
  lista.append([nombre, matricula, anioIngreso])
  return

# agregaAlumno()
# mostrarLista(203)

def eliminaAlumno():
  grupo = int(input('En qué grupo está el alumno a dar de baja: '))
  lista = buscarGrupo(grupo)
  matricula = int(input('Escribe la matrícula del alumno: '))
  for alumno in range(len(lista)):
    if alumno != 0:
      if matricula in lista[alumno]:
        lista.pop(alumno)
        return

# - Cambio de alumno a otro grupo.
def cambioAlumno(matricula, grupoSale, grupoEntra):
  datosAlumno = []
  listaActual = buscarGrupo(grupoSale)
  listaNueva = buscarGrupo(grupoEntra)
  for alumno in range(len(listaActual)):
    if alumno != 0:
      if matricula in listaActual[alumno]:
        datosAlumno = listaActual[alumno].copy()
        listaActual.pop(alumno)
        listaNueva.append(datosAlumno)
        return

def cambiaAlumno():
  grupoActual = int(input('Escribe el grupo donde se encuentra el alumno:'))
  grupoNuevo = int(input('Escribe el grupo a donde se va a cambiar el alumno:'))
  matricula = int(input('Escribe la matrícula del alumno:'))
  listaActual = buscarGrupo(grupoActual)
  listaNueva = buscarGrupo(grupoNuevo)
  for alumno in range(len(listaActual)):
    if alumno != 0:
      if matricula in listaActual[alumno]:
        # datosAlumno = listaActual[alumno].copy()
        datosAlumno = listaActual[alumno][0:3]
        print("datosAlumno:",datosAlumno) 
        listaActual.pop(alumno)
        listaNueva.append(datosAlumno)
        return

# Agregar la función de unir 2 grupos con las siguientes consideraciones:
# - Pedir el número del grupo al cual se le van a agregar los demás estudiantes
# - Borrar la lista de los estudiantes que se unieron al primer grupo
# - Mostrar la nueva lista con todos los integrantes

# capturaInfo()
# capturaInfo()
# mostrarLista(201)
# mostrarLista(202)
# # agregaAlumno()
# # mostrarLista(202)
# # eliminaAlumno()
# # mostrarLista(201)
# # cambioAlumno(19123, 201, 202)
# cambiaAlumno()
# mostrarLista(201)
# mostrarLista(202)

# Crear una lista con valores iniciales
miLista = [1,2,3]
miOtraLista = list((1,2,3))
print(miLista)
print(miOtraLista)
dato = '1'
print('dato',dato+'2')
print('datoInt',int(dato)+2)
print('datoLista',list((dato)))