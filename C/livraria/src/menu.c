#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "../lib/menu.h"
#include "../lib/livros.h"
#include "../lib/clear.h"

void exibir_menu() {
    printf("\nMenu de Operações:\n");
    printf("1. Adicionar Livro\n");
    printf("2. Emprestar Livro\n");
    printf("3. Devolver Livro\n");
    printf("4. Buscar Livro por Título\n");
    printf("5. Buscar Livro por Autor\n");
    printf("6. Listar Todos os Livros\n");
    printf("7. Sair\n");
}

int iniciar_menu() {
    No *lista = NULL;  // Inicializa a lista encadeada

    // Adiciona livros padrão
    Livro livro1;
    if (alocar_memoria_livro(&livro1, 1) == 0) {
        strcpy(livro1.titulo, "Harry Potter e a Pedra Filosofal");
        strcpy(livro1.autores[0].nome, "J.K. Rowling");
        livro1.total_emprestimos = 0;
        livro1.status = DISPONIVEL;
        adicionar_livro(&lista, livro1);
    }

    Livro livro2;
    if (alocar_memoria_livro(&livro2, 1) == 0) {
        strcpy(livro2.titulo, "O Senhor dos Anéis");
        strcpy(livro2.autores[0].nome, "J.R.R. Tolkien");
        livro2.total_emprestimos = 0;
        livro2.status = DISPONIVEL;
        adicionar_livro(&lista, livro2);
    }

    int opcao;
    char titulo[MAX_STR];
    char autor_nome[MAX_STR];

    do {
        exibir_menu();
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);
        getchar();  // Consumir o \n deixado pelo scanf

        switch (opcao) {
            case 1: {
                int num_autores;
                printf("Quantos autores? ");
                scanf("%d", &num_autores);
                getchar();

                Livro livro;
                if (alocar_memoria_livro(&livro, num_autores) != 0) {
                    break;
                }

                printf("Digite o título do livro: ");
                fgets(livro.titulo, MAX_STR, stdin);
                livro.titulo[strcspn(livro.titulo, "\n")] = '\0';

                for (int i = 0; i < num_autores; i++) {
                    printf("Digite o nome do autor %d: ", i + 1);
                    fgets(livro.autores[i].nome, MAX_STR, stdin);
                    livro.autores[i].nome[strcspn(livro.autores[i].nome, "\n")] = '\0';
                }

                adicionar_livro(&lista, livro);
                printf("Livro '%s' adicionado com sucesso!\n", livro.titulo);
                clear();
                break;
            }

            case 2:
                printf("Digite o título do livro para empréstimo: ");
                fgets(titulo, MAX_STR, stdin);
                titulo[strcspn(titulo, "\n")] = '\0';
                emprestar_livro(lista, titulo);
                clear();
                break;

            case 3:
                printf("Digite o título do livro para devolução: ");
                fgets(titulo, MAX_STR, stdin);
                titulo[strcspn(titulo, "\n")] = '\0';
                devolver_livro(lista, titulo);
                clear();
                break;

            case 4:
                printf("Digite o título do livro: ");
                fgets(titulo, MAX_STR, stdin);
                titulo[strcspn(titulo, "\n")] = '\0';
                {
                    Livro *livro = buscar_por_titulo(lista, titulo);
                    if (livro) {
                        imprimir_livro(livro);
                    } else {
                        printf("Livro não encontrado!\n");
                    }
                }
                clear();
                break;

            case 5:
                printf("Digite o nome do autor: ");
                fgets(autor_nome, MAX_STR, stdin);
                autor_nome[strcspn(autor_nome, "\n")] = '\0';
                buscar_por_autor(lista, autor_nome);
                clear();
                break;

            case 6:
                listar_livros(lista);
                clear();
                break;

            case 7:
                printf("Saindo...\n");
                liberar_memoria(lista);
                break;

            default:
                printf("Opção inválida! Tente novamente.\n");
                clear();
                break;
        }
    } while (opcao != 7);

    return 0;
}
