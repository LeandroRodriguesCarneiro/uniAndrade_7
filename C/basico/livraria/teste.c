#include <stdio.h>
#include <stdlib.h>
#include "lib/clear.h" // Incluir o cabeçalho de clear.h

int main() {
    printf("Este é o primeiro conteúdo do programa.\n");
    
    // Chama a função clear para pausar e limpar a tela
    clear();
    
    printf("Agora a tela foi limpa, e você pode continuar.\n");

    return 0;
}
