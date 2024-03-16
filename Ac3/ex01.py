#EX01: IDENTIFICAÇÃO DE TRIÂNGULOS

def determina_tipo_triangulo():
    l1=float(input("Digite o primeiro lado:"))
    l2=float(input("Digite o segundo lado:"))
    l3=float(input("Digite o terceiro lado:"))
    if l1==l2==l3:
            print("O Triângulo é Equilátero")
    elif l1!=l2!=l3!=l1:
            print("O Triângulo é  Escaleno")
    elif l1==l2 and l2!=l3:
            print(("O Triângulo é Isósceles"))
    else:
            print("Não é um Triângulo")

determina_tipo_triangulo()

#EX02: DIAS DA SEMANA

def dia_semana(dias):
    match dias:
        case 1:
            return "DOMINGO"
        case 2:
            return "SEGUNDA-FEIRA"
        case 3:
            return "TERÇA-FEIRA"
        case 4:
            return "QUARTA-FEIRA"
        case 5:
            return "QUINTA-FEIRA"
        case 6:
            return "SEXTA-FEIRA"
        case 7:
            return "SÁBADO"
        case _:
            return ""
         
#CALCULADORA SIMPLES:
def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def mult(a,b):
    return a*b

def divisao(a,b):
    return a/b


def calculo():
    n1=float(input("Informe o primeiro número: "))
    n2=float(input("Informe o segundo número:  "))
    op=str(input("Informe a operação:soma,subtracao,multi,divisao:  "))

    if op=="soma":
        resultado= soma(n1,n2)
    elif op=="subtraçao":
        resultado=subtracao(n1,n2)
    elif op=="mult":
        resultado=mult(n1,n2)
    elif op=="divisao":
        resultado=divisao(n1,n2)
    else:
        print("Operação Inválida")
        return
    return f"Resultado:{resultado}"
    
print(calculo())