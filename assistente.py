print('Olá, eu sou sua assistente, pythrina. O que posso fazer por você hoje?')

comando = input('Digite um comando: ')

match comando:
    case 'oi':
        print('Oi, como você vai?')
    case 'Tchau':
        print('tchau, foi bom conversar com você!')
match comando:   
    case 'piada':
        print('Sabe qual é o padroeiro das pessoas que trabalham com TI? O São Login')
match comando:
    case 'clima':
        print('Tá muuuuuuito quente!! Deve ter passado de 40ºC!🥵')
    case _:
        print('Desculpe, nào entendi o comando.')