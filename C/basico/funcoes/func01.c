#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TAMANHO_LINHA 30
#define MAX_STR 50

// int main()
// {
//     printf("Sem args\n");
//     return 0;
// }

// int main(void)
// {
//     printf("Sem args\n");
//     return 0;
// }

// int main(int argc, char const *argv[])
// {
//     for (int i = 0; i < argc; i++){
//         printf("Arg[%i] - %s\n", i, argv[i]);
//     }
//     return 0;
// }

// float intToFloat(int n){
//     return n;
// }

// void halfConvert(int n){
//     float half = intToFloat(n)*0.5;
//     printf("Metade: %.2f\n", half);

// }

// void menu(){
//     printf("%.*sMenu%.*s\n", (TAMANHO_LINHA - 4) / 2, "==============================", (TAMANHO_LINHA - 4) / 2, "==============================");
//     halfConvert(10);
//     // Exibe o final com a mesma largura da linha superior
//     printf("%.*s------------%.*s\n", (TAMANHO_LINHA - 12) / 2, "==============================", (TAMANHO_LINHA - 12) / 2, "==============================");
// }

// int main()
// {
//     menu();
//     return 0;
// }

typedef struct
{
    char name[MAX_STR];
    float power;
    int lives;
    bool alive;
} Player;

void imprimePlayer(Player *p){
    printf("%.*sGAME OVER%.*s\n", (TAMANHO_LINHA - 4) / 2, "==============================", (TAMANHO_LINHA - 4) / 2, "==============================");
    printf("Player: %s\n", p->name);
    printf("Power: %.4f\n", p->power);
    printf("Lives: %i\n", p->lives);
    printf("Alive: %i\n", p->alive);
    printf("%.*s------------%.*s\n", (TAMANHO_LINHA - 7) / 2, "=================================", (TAMANHO_LINHA - 6) / 2, "================================");
}

int main(int argc, char const *argv[])
{   
    Player players[5]; 
    Player p1 = {
        .name = "Brunao",
        .power = 1500,
        .lives = 5,
        .alive = true,
    };
    Player p2 = {
        .name = "Jhonny",
        .power = 1500,
        .lives = 5,
        .alive = true,
    };
    players[0] = p1;
    players[1] = p2;

    for (int i = 0; i < 2; i++) {
        imprimePlayer(&players[i]);
    }


    return 0;
}
