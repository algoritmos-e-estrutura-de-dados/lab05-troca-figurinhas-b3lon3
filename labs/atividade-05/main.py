def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):


    if len(figurinhas_do_joao) >= len(figurinhas_da_maria):
        maior = figurinhas_do_joao
        menor = figurinhas_da_maria

    else:
        menor = figurinhas_do_joao
        maior = figurinhas_da_maria

    maior2 = maior.copy()
    menor2 = menor.copy()

#----------------------------------------------------------------------------

    for i in range(len(menor)):
        for j in range(len(maior)):

            if maior[j] == menor[i]:
                for k in range(len(maior2)):

                    if int(menor2[k]) == int(maior[j]):
                        menor2.pop(k)

                        if len(maior2) == 0:
                            print(0)

                        else:
                            print(len(menor2))


                        break

            elif maior[j] is not menor[i]:
                print(len(menor2))
                break


if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_do_joao = input().split(' ')

    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao)
