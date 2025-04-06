#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

#include "lib/livros.h"
#include "lib/clear.h"

// Função para alocar memória para um livro
int alocar_memoria_livro(Livro *livro, int num_autores) {
    livro->titulo = (char *)malloc(MAX_STR * sizeof(char));
    if (livro->titulo == NULL) {
        printf("Erro ao alocar memória para o título do livro.\n");
        return 1;
    }

    livro->num_autores = num_autores;  // Definindo o número de autores
    livro->autores = (autor *)malloc(num_autores * sizeof(autor));  // Alocando espaço para os autores
    if (livro->autores == NULL) {
        printf("Erro ao alocar memória para os autores.\n");
        return 1;
    }

    for (int i = 0; i < num_autores; i++) {
        livro->autores[i].nome = (char *)malloc(MAX_STR * sizeof(char));  // Alocando memória para o nome de cada autor
        if (livro->autores[i].nome == NULL) {
            printf("Erro ao alocar memória para o nome do autor %d.\n", i + 1);
            return 1;
        }
    }

    livro->total_emprestimos = 0;  // Inicializando o total de empréstimos com 0
    livro->status = DISPONIVEL;     // Inicializando o status como DISPONÍVEL

    return 0;
}

// Função para adicionar um livro à lista encadeada
void adicionar_livro(No **inicio, Livro livro) {
    No *novo_no = (No *)malloc(sizeof(No));
    if (novo_no == NULL) {
        printf("Erro ao alocar memória para o novo nó.\n");
        exit(1);
    }

    novo_no->livro = livro;
    novo_no->proximo = *inicio;
    *inicio = novo_no;
}

// Função para buscar livro por título
Livro* buscar_por_titulo(No *inicio, const char *titulo) {
    No *atual = inicio;
    while (atual != NULL) {
        if (strcmp(atual->livro.titulo, titulo) == 0) {
            return &atual->livro;
        }
        atual = atual->proximo;
    }
    return NULL;
}

// Função para buscar livros por autor
void buscar_por_autor(No *inicio, const char *autor_nome) {
    No *atual = inicio;
    int encontrados = 0;
    while (atual != NULL) {
        for (int i = 0; i < atual->livro.num_autores; i++) {  // Itera pelo número de autores do livro
            if (atual->livro.autores[i].nome != NULL && strcmp(atual->livro.autores[i].nome, autor_nome) == 0) {
                printf("Livro encontrado: %s\n", atual->livro.titulo);
                encontrados = 1;
                break;
            }
        }
        atual = atual->proximo;
    }

    if (!encontrados) {
        printf("Nenhum livro encontrado para o autor %s.\n", autor_nome);
    }
}

// Função para listar todos os livros na lista
void listar_livros(No *inicio) {
    No *atual = inicio;
    printf("\nListando todos os livros:\n");
    while (atual != NULL) {
        imprimir_livro(&atual->livro);
        atual = atual->proximo;
    }
}

// Função para liberar a memória da lista encadeada
void liberar_memoria(No *inicio) {
    No *atual = inicio;
    while (atual != NULL) {
        No *temp = atual;
        free(atual->livro.titulo);
        for (int i = 0; i < atual->livro.num_autores; i++) {
            free(atual->livro.autores[i].nome);
        }
        free(atual->livro.autores);
        atual = atual->proximo;
        free(temp);
    }
}

// Função de empréstimo
void emprestar_livro(No *inicio, const char *titulo) {
    Livro *livro = buscar_por_titulo(inicio, titulo);
    if (livro == NULL) {
        printf("Livro não encontrado!\n");
        return;
    }

    if (livro->status == EMPRESTADO) {
        printf("O livro '%s' já está emprestado.\n", titulo);
    } else if (livro->total_emprestimos >= 3) {
        livro->status = INDISPONIVEL;  // Quando atingir o limite de 3 empréstimos, o livro se torna INDISPONÍVEL
        printf("O livro '%s' atingiu o limite máximo de 3 empréstimos e está agora INDISPONÍVEL.\n", titulo);
    } else {
        livro->status = EMPRESTADO;
        livro->total_emprestimos++;
        printf("Empréstimo realizado com sucesso para o livro '%s'. Total de empréstimos: %d\n", titulo, livro->total_emprestimos);
    }
}

// Função de devolução
void devolver_livro(No *inicio, const char *titulo) {
    Livro *livro = buscar_por_titulo(inicio, titulo);
    if (livro == NULL) {
        printf("Livro não encontrado!\n");
        return;
    }

    if (livro->status == DISPONIVEL) {
        printf("O livro '%s' já está disponível.\n", titulo);
    } else {
        livro->status = DISPONIVEL;
        livro->total_emprestimos--;
        printf("Devolução realizada com sucesso para o livro '%s'.\n", titulo);
    }
}

// Função para formatar e imprimir um livro
void imprimir_livro(Livro *livro) {
    printf("Título: %s\n", livro->titulo);
    printf("Autores: ");
    for (int i = 0; i < livro->num_autores; i++) {  // Itera por todos os autores
        if (livro->autores[i].nome != NULL) {
            printf("%s ", livro->autores[i].nome);
        }
    }
    printf("\nTotal de empréstimos: %d\n", livro->total_emprestimos);

    // Exibindo o status correto
    if (livro->status == DISPONIVEL) {
        printf("Status: Disponível\n");
    } else if (livro->status == EMPRESTADO) {
        printf("Status: Emprestado\n");
    } else if (livro->status == INDISPONIVEL) {
        printf("Status: Indisponível\n");
    }

    printf("\n");
}

// Função para exibir o menu
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

int main() {
    setlocale(LC_ALL, "pt_BR.UTF-8");

    No *lista = NULL;  // A lista começa vazia

    int opcao;
    char titulo[MAX_STR];
    char autor_nome[MAX_STR];

    // Adicionando livros padrão
    Livro livro1;
    alocar_memoria_livro(&livro1, 1);
    strcpy(livro1.titulo, "Harry Potter e a Pedra Filosofal");
    strcpy(livro1.autores[0].nome, "J.K. Rowling");
    livro1.total_emprestimos = 0;
    livro1.status = DISPONIVEL;
    adicionar_livro(&lista, livro1);

    Livro livro2;
    alocar_memoria_livro(&livro2, 1);
    strcpy(livro2.titulo, "O Senhor dos Anéis");
    strcpy(livro2.autores[0].nome, "J.R.R. Tolkien");
    livro2.total_emprestimos = 0;
    livro2.status = DISPONIVEL;
    adicionar_livro(&lista, livro2);

    // Loop principal para exibir o menu
    do {
        exibir_menu();
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);
        getchar();  // Consumir o caractere de nova linha após o scanf

        switch (opcao) {
            case 1: {
                // Adicionar Livro
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
                livro.titulo[strcspn(livro.titulo, "\n")] = '\0';  // Remover nova linha

                for (int i = 0; i < num_autores; i++) {
                    printf("Digite o nome do autor %d: ", i + 1);
                    fgets(livro.autores[i].nome, MAX_STR, stdin);
                    livro.autores[i].nome[strcspn(livro.autores[i].nome, "\n")] = '\0';  // Remover nova linha
                }

                adicionar_livro(&lista, livro);
                printf("Livro '%s' adicionado com sucesso!\n", livro.titulo);
                break;
            }

            case 2: {
                // Emprestar Livro
                printf("Digite o título do livro para empréstimo: ");
                fgets(titulo, MAX_STR, stdin);
                titulo[strcspn(titulo, "\n")] = '\0';  // Remover nova linha
                emprestar_livro(lista, titulo);
                clear();
                break;
            }

            case 3: {
                // Devolver Livro
                printf("Digite o título do livro para devolução: ");
                fgets(titulo, MAX_STR, stdin);
                titulo[strcspn(titulo, "\n")] = '\0';  // Remover nova linha
                devolver_livro(lista, titulo);
                clear();
                break;
            }

            case 4: {
                // Buscar Livro por Título
                printf("Digite o título do livro: ");
                fgets(titulo, MAX_STR, stdin);
                titulo[strcspn(titulo, "\n")] = '\0';  // Remover nova linha
                Livro *livro = buscar_por_titulo(lista, titulo);
                if (livro != NULL) {
                    imprimir_livro(livro);
                } else {
                    printf("Livro não encontrado!\n");
                }
                clear();
                break;
            }

            case 5: {
                // Buscar Livro por Autor
                printf("Digite o nome do autor: ");
                fgets(autor_nome, MAX_STR, stdin);
                autor_nome[strcspn(autor_nome, "\n")] = '\0';  // Remover nova linha
                buscar_por_autor(lista, autor_nome);
                clear();
                break;
            }

            case 6: {
                // Listar Todos os Livros
                listar_livros(lista);
                clear();
                break;
            }

            case 7:
                // Sair
                printf("Saindo...\n");
                break;

            default:
                printf("Opção inválida! Tente novamente.\n");
                break;
        }

    } while (opcao != 7);

    // Liberando a memória antes de sair
    liberar_memoria(lista);

    return 0;
}
