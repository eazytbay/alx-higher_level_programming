#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - A function that inserts a number into a sorted
 * singly linked list
 * @head: the address
 * @number: The number to be inserted
 * Return: The address of the new node on success or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node;
listint_t *current = *head;
listint_t *prev = NULL;
new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
{
return (NULL);
new_node->n = number;
new_node->next = NULL;
new_node->next = *head;
}
while (current != NULL && current->n < number)
{
prev = current;
current = current->next;
}
if (prev == NULL)
{
*head = new_node;
}
else
{
prev->next = new_node;
new_node->next = current;
}
return (new_node);
}
