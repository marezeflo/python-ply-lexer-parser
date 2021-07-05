import ply.lex as lex
import os
import re
import codecs

from tkinter.filedialog import  askopenfilename
import time

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
      
screen_clear

reservadas = {
  'accion':'ACCION',
  'fin_accion':'FIN_ACCION',

  'ambiente':'AMBIENTE',
  'proceso':'PROCESO',

  'funcion':'FUNCION',
  'fin_funcion':'FIN_FUNCION',

  'procedimiento':'PROCEDIMIENTO',
  'fin_procedimiento':'FIN_PROCEDIMIENTO',

  'segun':'SEGUN',
  'otro':'SEGUN_DEFECTO',
  'fin_segun':'FIN_SEGUN',

  'para':'PARA', 
  'hasta':'HASTA',
  'fin_para':'FIN_PARA',

  'repetir':'REPETIR',
  'hasta_que':'HASTA_QUE',

  'mientras':'MIENTRAS',
  'hacer':'HACER',
  'fin_mientras':'FIN_MIENTRAS',

  'si':'SI',
  'entonces':'ENTONCES',
  'sino':'SINO',
  'fin_si':'FIN_SI',

  'escribir':'ESCRIBIR',
  'leer': 'LEER'
}

# tokens = ['ES','DATO','NEG','CADENA','NUMERO','IDENTIFICADOR','C','PYC','DP','IG','DPIG','PI','PD','SDL','OPA','OPR','OPL','COMENTARIO_ENCABEZADO','COMENTARIO_BLOQUE','COMENTARIO_LINEA','ILEGAL']
# Decidimos separar los distintos operadores (tanto aritméticos como lógicos) en tokens distintos, para trabajar de mejor manera al momento de realizar el parser y trabajar la presedencia

# También extendimos la abreviatura para que sea más fácil la comprensión del código y no haya que estar adivinando según la definición del token el significado.

tokens = [
  'ES',
  'DATO','CADENA','NUMERO_ENTERO','NUMERO_REAL','IDENTIFICADOR',
  'COMA','PUNTO_Y_COMA','DOS_PUNTOS','PARENTESIS_IZQUIERDA','PARENTESIS_DERECHA','SALTO_DE_LINEA', 
  'ASIGNACION',
  'COMENTARIO_ENCABEZADO','COMENTARIO_BLOQUE','COMENTARIO_LINEA',
  'CONJUNCION','DISYUNCION','NEGACION',
  'SUMA','RESTA','DIVISION','MULTIPLICACION','POTENCIA','MODULO','DIVISION_ENTERA',
  'IGUAL','MAYOR','MENOR','DISTINTO','MAYOR_IGUAL','MENOR_IGUAL',
  #'ILEGAL',
  ]

# https://cheatography.com/davechild/cheat-sheets/regular-expressions/pdf/

tokens = tokens+list(reservadas.values())

t_ignore = ' \t'
# t_ILEGAL = '[_][_]'   No es usado en el parser
t_ES = r'[_][eE][sS]'

t_COMA = r','
t_PUNTO_Y_COMA =r';'
t_DOS_PUNTOS = r':'

t_PARENTESIS_IZQUIERDA = r'\('
t_PARENTESIS_DERECHA = r'\)'

t_ASIGNACION = r'\:\='

t_IGUAL = r'='
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_MENOR_IGUAL = r'\<='
t_MAYOR_IGUAL = r'\>='
t_DISTINTO = r'\<\>'

t_CONJUNCION = r'[_][yY]'
t_DISYUNCION = r'[_][oO]'
t_NEGACION = r'[_][nN][oO]'

t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_POTENCIA = r'\*\*'
t_MODULO = r'[_][mM][oO][dD]'
t_DIVISION_ENTERA = r'[_][dD][iI][vV]'

def t_COMENTARIO_ENCABEZADO(t):
  r'(/\*\*(.|\n)*?\*/)'
  return t

def t_COMENTARIO_BLOQUE(t):
  r'(/\*(.|\n)*?\*/)'
  return t

def t_COMENTARIO_LINEA(t):
  r'(// .* | \@ .* )'
  return t

def t_NUMERO_ENTERO(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_NUMERO_REAL(t):
  r'(\d+\,\d+|\d+\.\d+)'
  t.value = float(t.value)
  return t

def t_DATO(t):
  r'([nN][uU][mM][eE][rR][oO]|[eE][nN][tT][eE][rR][oO]|[rR][eE][aA][lL]|[cC][aA][dD][eE][nN][aA]|[nN][uU][mM][eE][rR][iI][cC][oO]|[aA][lL][fF][aA][nN][uU][mM][eE][rR][iI][cC][oO])'
  return t

def t_IDENTIFICADOR(t):
  r'[a-zA-ZñÑ][a-zA-ZñÑ]*([_]?[a-zA-Z0-9ñÑ]*)*'
  t.type = reservadas.get(t.value.lower(),'IDENTIFICADOR')
  return t

def t_CADENA(t):
  r'(["].*["] | [\'].*[\'] | [“].*[”])'
  return t

def t_SALTO_DE_LINEA(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_error(t):
  print("\n Caracter no permitido encontrado: '%s'" % t.value[0])
  t.lexer.skip(1)

lexer = lex.lex()

def lexing(pseudocodigo):
  lexer.lineno = 0
  global nombre_arch
  lexer.input(pseudocodigo)
  while True:
    tok = lexer.token()
    if not tok:
      break
    print(tok.value,"← corresponde al token →", tok.type,"\n")

# rta = 0
# 
# while (rta != 1 and rta != 2):
#       
#   rta = int(input("\n¿Qué desea analizar?\n\n\t1 - Archivo\n\n\t2 - Pseudocódigo ingresado por pantalla\n\nOpción: "))
#   if (rta == 2):
#     print("\n\nEscriba el pseudocódigo a continuación, por favor: \n")
#     pseudocodigo = ""
#     i = 1
#     while True:
#         data = input('{} '.format(i))
#         pseudocodigo = pseudocodigo + data + '\n'
#         if (data == "FIN_ACCION" or data == "fin_accion"):
#           break
#         i += 1
#     lexing(pseudocodigo)  
#   else:
#     if (rta == 1):
#       archivo=askopenfilename(title="Seleccione un archivo, por favor:", filetype=[("txt file",".txt")])
#       nombre_arch=os.path.basename(archivo).replace('.txt','')
#       test = codecs.open(archivo,'r','utf-8')
#       cadena = test.read()
#       cadena = re.sub(r"\r","",cadena)
#       test.close()
#       lexing(cadena)
#     else:
#       print('\nOpción inválida, reiniciando...\n')
# 
# end = str(input("\nPresione enter para finalizar."))
# print('\nGracias por usar nuestro lexer :)\n')
# time.sleep(2)