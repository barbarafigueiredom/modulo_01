print('Boas vindas ao nosso glorioso jogo de MADLIB')
dia_semana = input("Digite um dia da semana: ")
estado = input("Digite o nome de um estado brasileiro: ")
nome1 = input("Digite um nome masculino: ")
nome2 = input("Digite um nome feminino: ")
verbo = input("Digite um verbo (ex: dançar, conversar, caminhar): ")
tema = input("Digite um tema aleatório (ex: música, viagens, filmes): ")




print(' Título: "A GRANDE HISTÓRIA DE AMOR"')


historia = f"""
Em uma bela noite de {dia_semana}, aconteceu uma grande festa em uma pequena cidade,
localizada no interior do {estado}. As luzes brilhavam, a música tocava alto e todos
pareciam animados.

No salão, {nome1} observava tudo com curiosidade. Do outro lado, {nome2} conversava 
animadamente com seus amigos.

Então, seus olhares se cruzaram pela primeira vez. {nome1} sorriu e caminhou até ela.

— Oi… você gostaria de {verbo} comigo?
— Claro! — respondeu {nome2}, com um brilho especial nos olhos.

Eles passaram a noite inteira conversando sobre {tema}, rindo e descobrindo coincidências
que pareciam obra do destino.

E assim começou uma linda história de amor — iniciada naquela pequena cidade do interior,
naquela bela noite de {dia_semana}.
"""

print("\n=== SUA HISTÓRIA GERADA ===")
print(historia)