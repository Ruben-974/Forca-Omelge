palavras = ['PAPEL', 'OMELGLE', 'NADA', 'SUJEIRA', 'GOVERNO', 'COMPUTADOR', 'PAISAGEM']

chances = 5

escolhida = [c for c in palavras[-2]]
censura = ['_'] * len(escolhida)

print(escolhida, censura)

while True: 

    if chances == 0:
        print(f'Vocẽ perdeu :(\nA palavra era: {"".join(escolhida)}')
        break

    print('Forca:', ' '.join(censura), f'| {chances} Chances (Sem dica!)')

    if '_' not in censura:
        print('Favela venceu :)')
        break

    resp = input(str('Digite uma letra: ')).upper()

    if resp in escolhida and len(resp) == 1:

        for c in range(len(escolhida)): 
            if resp == escolhida[c]:
                censura[c] = resp

    elif resp == ''.join(escolhida):
        print(f'Parabens vocẽ acertou :D')
        break

    else:
        chances -= 1

    