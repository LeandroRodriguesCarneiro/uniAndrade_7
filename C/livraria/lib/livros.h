#ifndef LIVROS_H
#define LIVROS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STR 255  // Tamanho máximo para strings

// Enum para o status do livro
enum status_livro {
    DISPONIVEL,
    EMPRESTADO,
    INDISPONIVEL
};

// Definição da estrutura Autor
typedef struct {
    char *nome;
} autor;

// Definição da estrutura Livro
typedef struct {
    autor *autores;      // Ponteiro para os autores (agora dinâmico)
    char *titulo;
    int total_emprestimos;
    enum status_livro status;
    int num_autores;     // Número de autores (dinâmico)
} Livro;

// Definição da estrutura Nó (para a lista encadeada)
typedef struct No {
    Livro livro;
    struct No *proximo;
} No;

// Funções principais
int alocar_memoria_livro(Livro *livro, int num_autores);
void adicionar_livro(No **inicio, Livro livro);
Livro* buscar_por_titulo(No *inicio, const char *titulo);
void buscar_por_autor(No *inicio, const char *autor_nome);
void listar_livros(No *inicio);
void liberar_memoria(No *inicio);

// Funções extras (Bônus)
void emprestar_livro(No *inicio, const char *titulo);
void devolver_livro(No *inicio, const char *titulo);

// Funções para formatar a impressão
void imprimir_livro(Livro *livro);
void formatar_impressao(const char *mensagem);

#endif