#include <stdio.h>
#include <stdlib.h>

void send() {
    char message[32] = {0};
    printf("Entrer le message a envoyer");
    gets(message);
    printf("\This the message to send: \n");
    printf(message);
    printf("Succes to send");
    fflush(stdout);
    return;
}

int main() {
    printf("Hello Mike what you want ?\n");
    send();
    printf("Ok!");
    return 0;
}