#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>

#include "../lib/livros.h"
#include "../lib/menu.h"

int main() {
    setlocale(LC_ALL, "pt_BR.UTF-8");

    // Inicia o controle principal do sistema (menu)
    iniciar_menu();

    return 0;
}
