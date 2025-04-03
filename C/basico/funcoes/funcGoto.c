#include <stdio.h>
#include <stdlib.h>
#include "lib/clear.h"

int main()
{
    int numero;

    // Pedir para o usuário inserir um número
    printf("Digite um número: ");
    scanf("%d", &numero);

    // Limpar a tela após a inserção do número
    clear();

    // Condicional para verificar se o número é negativo, positivo ou zero
    if (numero < 0)
    {
        goto NEGATIVO;
    }
    else if (numero > 0)
    {
        goto POSITIVO;
    }
    else
    {
        goto ZERO;
    }

NEGATIVO:
    // Mensagem para número negativo
    printf("O número [%d] é negativo.\n", numero);
    goto FIM;

POSITIVO:
    // Mensagem para número positivo
    printf("O número [%d] é positivo.\n", numero);
    goto FIM;

ZERO:
    // Mensagem para número zero
    printf("Você inseriu o número ZERO.\n");
    goto FIM;

FIM:
    // Fim do programa
    printf("Fim do programa.\n");

    return 0;
}
