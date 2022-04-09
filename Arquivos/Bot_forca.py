from random import randrange

def forca(escolhida, censura, chances, resp):

    if chances == 0: print(f'Vocẽ perdeu :(\nA palavra era: {"".join(escolhida)}'); return False, chances

    if resp in escolhida and len(resp) == 1:

        for c in range(len(escolhida)): 
            if resp == escolhida[c]: censura[c] = resp
        if '_' not in censura:

            print(f'Forca: {" ".join(censura)} | {chances} Chances (Sem dica!)')
            print(f'Parabens vocẽ acertou :D')
            return False, chances

        else: 
            return True, chances

    if resp == ''.join(escolhida) or '_' not in censura: print(f'Parabens vocẽ acertou :D'); return False, chances

    else: 
        chances -= 1 
        return True, chances


palavras, chances, continuar = ['PAPEL', 'OMEGLE', 'NADA', 'SUJEIRA', 'GOVERNO', 'COMPUTADOR', 'PAISAGEM'], 5, True

escolhida = [c for c in palavras[randrange(len(palavras))]]
censura = ['_'] * len(escolhida)

print('Olá, sou o bot da forca, vamos jogar?\nEscreva uma letra ou uma palavra desejada, mas tenha cuidado! Suas chances diminuem a cada erro!\nBOA SORTE!')

while continuar:

    print(f'Forca: {" ".join(censura)} | {chances} Chances (Sem dica!)')

    resp = input(str('Digite uma letra: ')).upper()

    continuar, chances = forca(escolhida, censura, chances, resp)

print('Se vocẽ quiser incentivar/ajudar meu desenvolvedor o chave pix dele é: e0b2c13a-8b11-4871-9a93-cda231725a1e\nOBRIGADO POR JOGAR :D')
