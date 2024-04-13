#include "lists.h"
/**
* insert_node - Inserts a new node in a sorted linked list.
* @head: Pointer to the head of the linked list.
* @number: Value to be inserted in the new node.
*
* Return: Pointer to the new node.
*/
listint_t *insert_node(listint_t **head, int number){
    listint_t *pnewnode;
    listint_t *current = *head;
    pnewnode = malloc(sizeof(listint_t));
    current = malloc(sizeof(listint_t));
    
    if(pnewnode == NULL){
        return NULL;
    }
    pnewnode->n = number;
    pnewnode->next = NULL;
    /*condition for if node enters in the beggining*/
    if(*head == NULL || number < (*head)->n){
        pnewnode->next = *head;
        *head = pnewnode;
        return (pnewnode);
    }
    /*traverse to find  newnode(use temp pointer)*/
    while(current->next != NULL && number > current->next->n){
        current = current->next;
    }
    /*insert node*/
    pnewnode->next = current->next;
    current->next = pnewnode;
    return (pnewnode);
    
    free(pnewnode);
    free(current);
}
