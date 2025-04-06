#ifndef CLEAR_H
#define CLEAR_H

#ifdef _WIN32
    #define CLEAR_CMD "cls"
#else
    #define CLEAR_CMD "clear"
#endif

// Função para limpar a tela e fazer uma pausa
void clear();

#endif // CLEAR_H
