#include <stdio.h>
#include <stdlib.h>
#include "../lib/clear.h"

// Função clear que limpa a tela e faz uma pausa para o usuário pressionar Enter
void clear() {
    printf("Pressione Enter para continuar...\n");
    getchar();
    system(CLEAR_CMD);
}