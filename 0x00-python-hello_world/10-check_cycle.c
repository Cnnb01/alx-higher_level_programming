#include "lists.h"
/**
* check_cycle - Checks if a linked list has a cycle.
* @list: A pointer to the head of the linked list.
*
* Return: 1 if a cycle is detected, 0 otherwise.
*/
int check_cycle(listint_t *list)
{
listint_t *pslow;
listint_t *pfast;
pslow = list;
pfast = list->next;

while (pslow != pfast)
{
if (pslow == NULL || pfast == NULL || pfast->next == NULL)
{
return (0);
}
else
{
pslow = pslow->next;
pfast = pfast->next->next;
}
}
return (1);
}
