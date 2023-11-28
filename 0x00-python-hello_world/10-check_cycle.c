#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - A function that confirms if a singly linked list has a cycle
 * @list: The singly linked list
 * Return: 0 in a case where there is no cycle and 1 if there is
 */

int check_cycle(listint_t *list)
{
listint_t *slow = list, *fast = list;
while (fast != NULL && fast->next != NULL)
{
slow = slow->next;
fast = fast->next->next;
if (slow == fast)
return (1);
}
return (0);
}
