nome = input("digite seu nome: ")

nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
nota4 = float(input("digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7.0:
    print("você foi aprovado✅")

else:
    print("você foi reprovado❌")

