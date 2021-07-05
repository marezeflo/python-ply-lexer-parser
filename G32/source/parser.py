import ply.yacc as yacc

import os
import re
import codecs

from tkinter.filedialog import  askopenfilename
import time

from lexer import lexing, tokens

precedence = (
  ('right','COMA'),
  ('right','HACER','ENTONCES','PUNTO_Y_COMA'),
  ('right','IDENTIFICADOR','PROCESO','AMBIENTE','SI','MIENTRAS','REPETIR','PARA','HASTA'),
  ('left','CONJUNCION','DISYUNCION'),
  ('right','ASIGNACION'),
  ('right','IGUAL'),
  ('left','DISTINTO'),
  ('left','MENOR','MENOR_IGUAL','MAYOR','MAYOR_IGUAL'),
  ('left','SUMA','RESTA'),
  ('left','MULTIPLICACION','DIVISION','DIVISION_ENTERA'),
  ('right','MODULO','POTENCIA'),
  ('left','PARENTESIS_IZQUIERDA','PARENTESIS_DERECHA'),
)

# https://docs.google.com/document/d/1lprNCmoiR7_feu5g-xZ-OLEJWR81U9Q2KG25eiajNp0/edit?usp=sharing

def p_sigma(p):
  '''
    sigma : program
  '''
  print ("<sigma>")
  print ("\n Código sintácticamente correcto.\n")

def p_program(p):
  '''
    program : ACCION IDENTIFICADOR ES environment process FIN_ACCION
            | comment ACCION IDENTIFICADOR ES environment process FIN_ACCION
            | ACCION IDENTIFICADOR ES process FIN_ACCION
            | comment ACCION IDENTIFICADOR ES process FIN_ACCION
  '''
  print ("<program>")

def p_process(p):
  '''
    process : PROCESO sentence
    process : PROCESO
  '''
  print ("<process>")

def p_comment(p):
  '''
    comment : COMENTARIO_ENCABEZADO
            | COMENTARIO_BLOQUE
            | COMENTARIO_LINEA
  '''
  print ("<comment>")

def p_environment(p):
  '''
    environment : AMBIENTE environmentsentence
    environment : AMBIENTE
  '''
  print ("<environment>")


def p_environmentsentence(p):
  '''
    environmentsentence : IDENTIFICADOR DOS_PUNTOS type PUNTO_Y_COMA environmentsentence
                        | comment IDENTIFICADOR DOS_PUNTOS type PUNTO_Y_COMA environmentsentence
                        | IDENTIFICADOR DOS_PUNTOS type PUNTO_Y_COMA
                        | comment IDENTIFICADOR DOS_PUNTOS type PUNTO_Y_COMA
                        | IDENTIFICADOR IGUAL CADENA PUNTO_Y_COMA environmentsentence
                        | comment IDENTIFICADOR IGUAL CADENA PUNTO_Y_COMA environmentsentence
                        | IDENTIFICADOR IGUAL DATO PUNTO_Y_COMA environmentsentence
                        | comment IDENTIFICADOR IGUAL DATO PUNTO_Y_COMA environmentsentence
                        | IDENTIFICADOR IGUAL CADENA PUNTO_Y_COMA
                        | comment IDENTIFICADOR IGUAL CADENA PUNTO_Y_COMA
                        | IDENTIFICADOR IGUAL DATO PUNTO_Y_COMA
                        | comment IDENTIFICADOR IGUAL DATO PUNTO_Y_COMA
                        | IDENTIFICADOR IGUAL NUMERO_ENTERO PUNTO_Y_COMA environmentsentence
                        | comment IDENTIFICADOR IGUAL NUMERO_ENTERO PUNTO_Y_COMA environmentsentence
                        | IDENTIFICADOR IGUAL NUMERO_ENTERO PUNTO_Y_COMA
                        | comment IDENTIFICADOR IGUAL NUMERO_ENTERO PUNTO_Y_COMA
                        | IDENTIFICADOR IGUAL NUMERO_REAL PUNTO_Y_COMA environmentsentence
                        | comment IDENTIFICADOR IGUAL NUMERO_REAL PUNTO_Y_COMA environmentsentence
                        | IDENTIFICADOR IGUAL NUMERO_REAL PUNTO_Y_COMA
                        | comment IDENTIFICADOR IGUAL NUMERO_REAL PUNTO_Y_COMA                        
                        | function PUNTO_Y_COMA environmentsentence
                        | comment function PUNTO_Y_COMA environmentsentence
                        | function PUNTO_Y_COMA
                        | comment function PUNTO_Y_COMA
                        | procedure PUNTO_Y_COMA environmentsentence
                        | comment procedure PUNTO_Y_COMA environmentsentence
                        | procedure PUNTO_Y_COMA
                        | comment procedure PUNTO_Y_COMA

  '''
  print ("<environmentsentence>")

def p_type(p):
  '''
  type  : DATO
  '''
  print ("<type>")

def p_function(p):
  '''
  function  : FUNCION IDENTIFICADOR PARENTESIS_IZQUIERDA arguments PARENTESIS_DERECHA DOS_PUNTOS type ES environment process FIN_FUNCION PUNTO_Y_COMA
            | FUNCION IDENTIFICADOR PARENTESIS_IZQUIERDA arguments PARENTESIS_DERECHA DOS_PUNTOS type ES process FIN_FUNCION PUNTO_Y_COMA

  '''
  print ("<function>")

def p_procedure(p):
  '''
  procedure : PROCEDIMIENTO PARENTESIS_IZQUIERDA arguments PARENTESIS_DERECHA ES environment process FIN_PROCEDIMIENTO PUNTO_Y_COMA
            | PROCEDIMIENTO PARENTESIS_IZQUIERDA arguments PARENTESIS_DERECHA ES process FIN_PROCEDIMIENTO PUNTO_Y_COMA

  '''
  print ("<procedure>")

def p_sentence(p):
  '''
  sentence  : write PUNTO_Y_COMA sentence
            | comment write PUNTO_Y_COMA sentence
            | write PUNTO_Y_COMA
            | comment write PUNTO_Y_COMA
            | read PUNTO_Y_COMA sentence
            | comment read PUNTO_Y_COMA sentence
            | read PUNTO_Y_COMA
            | comment read PUNTO_Y_COMA
            | while PUNTO_Y_COMA sentence
            | comment while PUNTO_Y_COMA sentence
            | while PUNTO_Y_COMA
            | comment while PUNTO_Y_COMA
            | for PUNTO_Y_COMA sentence
            | comment for PUNTO_Y_COMA sentence
            | for PUNTO_Y_COMA
            | comment for PUNTO_Y_COMA
            | if PUNTO_Y_COMA sentence
            | comment if PUNTO_Y_COMA sentence
            | if PUNTO_Y_COMA
            | comment if PUNTO_Y_COMA
            | case PUNTO_Y_COMA sentence
            | comment case PUNTO_Y_COMA sentence
            | case PUNTO_Y_COMA
            | comment case PUNTO_Y_COMA
            | repeat PUNTO_Y_COMA sentence
            | comment repeat PUNTO_Y_COMA sentence
            | repeat PUNTO_Y_COMA
            | comment repeat PUNTO_Y_COMA
            | assign PUNTO_Y_COMA sentence
            | comment assign PUNTO_Y_COMA sentence
            | assign PUNTO_Y_COMA
            | comment assign PUNTO_Y_COMA

  '''
  print ("<sentence>")

def p_write(p):
  '''
  write : ESCRIBIR PARENTESIS_IZQUIERDA string PARENTESIS_DERECHA PUNTO_Y_COMA

  '''
  print ("<write>")

def p_read(p):
  '''
  read  : LEER PARENTESIS_IZQUIERDA var PARENTESIS_DERECHA 

  '''
  print ("<read>")

def p_while(p):
  '''
  while : MIENTRAS condition HACER sentence FIN_MIENTRAS

  '''
  print ("<while>")

def p_for(p):
  '''
  for : PARA PARENTESIS_IZQUIERDA IDENTIFICADOR ASIGNACION NUMERO_ENTERO PARENTESIS_DERECHA HASTA NUMERO_ENTERO COMA IDENTIFICADOR ASIGNACION IDENTIFICADOR SUMA NUMERO_ENTERO HACER sentence FIN_PARA
      | PARA PARENTESIS_IZQUIERDA IDENTIFICADOR ASIGNACION NUMERO_ENTERO PARENTESIS_DERECHA HASTA NUMERO_ENTERO HACER sentence FIN_PARA
  '''
  print ("<for>")

def p_if(p):
  '''
  if  : SI condition ENTONCES sentence FIN_SI
      | SI condition ENTONCES sentence SINO sentence FIN_SI
  '''
  print ("<if>")

def p_case(p):
  '''
  case  : SEGUN PARENTESIS_IZQUIERDA IDENTIFICADOR PARENTESIS_DERECHA HACER casesentence FIN_SEGUN
  '''
  print ("<case>")

def p_casesentence(p):
  '''
  casesentence  : IGUAL NUMERO_ENTERO DOS_PUNTOS sentence PUNTO_Y_COMA casesentence
                | IGUAL NUMERO_ENTERO DOS_PUNTOS sentence PUNTO_Y_COMA
                | IGUAL NUMERO_ENTERO DOS_PUNTOS sentence PUNTO_Y_COMA default
                | IGUAL NUMERO_REAL DOS_PUNTOS sentence PUNTO_Y_COMA casesentence
                | IGUAL NUMERO_REAL DOS_PUNTOS sentence PUNTO_Y_COMA 
                | IGUAL NUMERO_REAL DOS_PUNTOS sentence PUNTO_Y_COMA default
                | IGUAL IDENTIFICADOR DOS_PUNTOS sentence PUNTO_Y_COMA casesentence
                | IGUAL IDENTIFICADOR DOS_PUNTOS sentence PUNTO_Y_COMA
                | IGUAL IDENTIFICADOR DOS_PUNTOS sentence PUNTO_Y_COMA default
  '''
  print ("<casesentence>")

def p_default(p):
  '''
  default : SEGUN_DEFECTO DOS_PUNTOS sentence PUNTO_Y_COMA
  '''
  print ("<default>")

def p_repeat(p):
  '''
  repeat  : REPETIR sentence HASTA_QUE condition
  '''
  print ("<repeat>")

def p_assign(p):
  '''
  assign  : IDENTIFICADOR ASIGNACION operation
          | IDENTIFICADOR ASIGNACION CADENA
  '''
  print ("<assign>")

def p_operation(p):
  '''
  operation : PARENTESIS_IZQUIERDA operation PARENTESIS_DERECHA
            | operated aop operated aop operation
            | operated aop operated
            | operated
  '''
  print ("<operation>")

def p_operated(p):
  '''
  operated  : IDENTIFICADOR
            | NUMERO_REAL
            | NUMERO_ENTERO
  '''
  print ("<operated>")

def p_arguments(p):
  '''
  arguments : IDENTIFICADOR DOS_PUNTOS type COMA arguments
            | IDENTIFICADOR DOS_PUNTOS type
  '''
  print ("<arguments>")

def p_string(p):
  '''
  string  : var COMA string
          | var
          | CADENA COMA string
          | CADENA
  '''
  print ("<string>")

def p_var(p):
  '''
  var : IDENTIFICADOR COMA var
      | IDENTIFICADOR
  '''
  print ("<var>")

def p_condition(p):
  '''
  condition : PARENTESIS_IZQUIERDA IDENTIFICADOR rop IDENTIFICADOR PARENTESIS_DERECHA 
            | NEGACION PARENTESIS_IZQUIERDA IDENTIFICADOR rop IDENTIFICADOR PARENTESIS_DERECHA 
            | PARENTESIS_IZQUIERDA CADENA rop CADENA PARENTESIS_DERECHA 
            | NEGACION PARENTESIS_IZQUIERDA CADENA rop CADENA PARENTESIS_DERECHA 
            | PARENTESIS_IZQUIERDA NUMERO_ENTERO rop NUMERO_ENTERO PARENTESIS_DERECHA 
            | NEGACION PARENTESIS_IZQUIERDA NUMERO_ENTERO rop NUMERO_ENTERO PARENTESIS_DERECHA 
            | PARENTESIS_IZQUIERDA NUMERO_REAL rop NUMERO_REAL PARENTESIS_DERECHA 
            | NEGACION PARENTESIS_IZQUIERDA NUMERO_REAL rop NUMERO_REAL PARENTESIS_DERECHA 
            | condition lop condition
  '''
  print ("<condition>")

def p_aop(p):
  '''
  aop : SUMA
		  | RESTA
		  | MULTIPLICACION
		  | DIVISION
		  | MODULO
		  | DIVISION_ENTERA
		  | POTENCIA
  '''
  print ("<aop>")

def p_lop(p):
  '''
  lop : CONJUNCION
      | DISYUNCION
  '''
  print ("<lop>")

def p_rop(p):
  '''
  rop : IGUAL
		  | MAYOR
		  | MENOR
		  | MAYOR_IGUAL
		  | MENOR_IGUAL
		  | DISTINTO
  '''
  print ("<rop>")

def p_error(p):
  print ("\nError de sintaxis en la producción: ",p)
  print ("El error se ubica en la línea N ",p.lineno,"\n")

parser = yacc.yacc('SLR')

rta = 0

while (rta != 1 and rta != 2):
      
  rta = int(input("\n¿Qué desea analizar?\n\n\t1 - Archivo\n\n\t2 - Pseudocódigo ingresado por pantalla\n\nOpción: "))
  print("\n")
  if (rta == 2):
    print ("\nEscriba el pseudocódigo a continuación, por favor: \n")
    pseudocodigo = ""
    i = 1
    while True:
      data = input('{} '.format(i))
      pseudocodigo = pseudocodigo + data + '\n'
      if (data == "FIN_ACCION" or data == "fin_accion"):
        break
      i += 1
    
    print("\n---------")
    print("LEXING...")
    print("---------\n")

    pruebalexer = lexing(pseudocodigo)

    print("\n----------")
    print("PARSING...")
    print("----------\n")

    result = parser.parse(pseudocodigo)

  else:
    if (rta == 1):
      archivo=askopenfilename(title="Seleccione un archivo, por favor:", filetype=[("txt file",".txt")])
      nombre_arch=os.path.basename(archivo).replace('.txt','')
      test = codecs.open(archivo,'r','utf-8')
      pseudocodigo = test.read()
      pseudocodigo = re.sub(r"\r","",pseudocodigo)
      test.close()

      print("\n---------")
      print("LEXING...")
      print("---------\n")

      pruebalexer = lexing(pseudocodigo)

      print("\n----------")
      print("PARSING...")
      print("----------\n")

      result = parser.parse(pseudocodigo)
    else:
      print ('\nOpción inválida, reiniciando...\n')

if (result!=None):
  print (result)
else:
  print ("Programa sintácticamente incorrecto.")

end = str(input("\nPresione enter para finalizar."))
print ('\nGracias por usar nuestro parser :)\n')
time.sleep(2)