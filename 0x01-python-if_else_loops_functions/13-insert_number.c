#include "list.h"
/**
 *
 *
 *
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *headcopy = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return(NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		new->next = NULL;
		return (new);
	}
	headcopy = *head;
	while (headcopy)
	{
		if ((number <= headcopy->n))
		{
			new->next = headcopy;
			*head = new;
			return (new);
		}
		if ((number >= headcopy->n) && (current->next == NULL))
		{
			new->next = NULL;
			headcopy->next = new;
			return (new);
		}
		if ((number >= headcopy->n) && (number <= headcopy->next->n))
		{
			new->next = headcopy->next;
			headcopy->next = new;
			return (new);
		}
		headcopy = headcopy->next;
	}
	return (NULL);
}
