def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def verificar_aprovacao(media):
    return "Aprovado" if media >= 7 else "Reprovado"

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
media = calcular_media(nota1, nota2)
print(f"Status: {verificar_aprovacao(media)} Média: {media}")

nota3 = int(input('Digite a terceira nota: '))
nota4 =    int(input('Digite a quarta nota: '))
media2 = calcular_media(nota3, nota4)
print(f"Status: {verificar_aprovacao(media2)} Média {media2}")





