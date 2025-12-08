notas = [9, 9.5, 10, 9.8]

media = 0
for nota in notas:
    media += nota

media /= len(notas);

print(f'A média é {media}')