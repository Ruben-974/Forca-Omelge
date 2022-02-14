palavras = ['PAPEL', 'OMELGLE', 'NADA', 'SUJEIRA', 'GOVERNO', 'COMPUTADOR', 'PAISAGEM']

chances = 5
escolhida = [c for c in palavras[-2]]
censura = ['_'] * len(escolhida)

print('Olá, sou o bot da forca, vamos jogar?\nEscreva uma letra ou uma palavra desejada, mas tenha cuidado! Suas chances diminuem a cada erro!\nBOA SORTE!')

while True: 

    if chances == 0:
        print(f'Vocẽ perdeu :(\nA palavra era: {"".join(escolhida)}')
        break

    print('Forca:', ' '.join(censura), f'| {chances} Chances (Sem dica!)')

    if '_' not in censura:
        print('Parabens vocẽ acertou :D')
        break

    resp = input(str('Digite uma letra: ')).upper()

    if resp in escolhida and len(resp) == 1:

        for c in range(len(escolhida)): 
            if resp == escolhida[c]:
                censura[c] = resp

    elif resp == ''.join(escolhida) or '_' not in censura:
        print(f'Parabens vocẽ acertou :D')
        break

    else:
        chances -= 1

print('Se vocẽ quiser incentivar/ajudar meu desenvolvedor o pix dele é: e0b2c13a-8b11-4871-9a93-cda231725a1e')
print('OBRIGADO POR JOGAR :D')
