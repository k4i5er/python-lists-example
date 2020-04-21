# La escuela Justo Sierra está contratando developers para 
# que desarrollen una aplicación que les permita administrar
# listas de alumnos para sus distintos grupos.
# Sus necesidades son las siguientes:
# - Registrar el año de ingreso por alumno.
# - Elaborar listas de alumnos por grupo.
# - Agregar y eliminar alumnos de un grupo.
# - Cambio de alumno a otro grupo.


# - Registrar nombre completo y matrícula de los alumnos.
# - Llevar registro de a qué grupo pertenece cada alumno.

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
#     ["Alexandra Olea", 1928373726], 
#     ["Osvaldo Pulido", 1928732832], 
#     ["Julian Robal",   1928236626]
#   ],
#   [
#     202, 
#     ["Eduardo Olivares", 192837263],
#     
#     ["Estrella Terrazas", 19823762]
#   ], 
#   [
#     203,
#     ["Daniel Salado", 192837263],
#   ]
# ]

listasGenerales = []

#def creaLista(listaGrupo):
  

def capturaInfo():
  lista = []
  grupo = input('Escribe el grupo: ')
  lista.append(grupo)
  while True:
    nombre = input('Escribe el nombre completo del alumno: ')
    matricula = input('Escribe la matrícula del alumno: ')
    lista.append([nombre, matricula])
    opc = input('Deseas agregar más alumnos? (s/n): ')
    if(opc == 'n' or opc == 'N'):
      break
  return


capturaInfo()