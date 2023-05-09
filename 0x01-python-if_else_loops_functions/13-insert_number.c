#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inset node to list accord
 * to it's number to be sorted
 * @head: pointer to pointer of list
 * @number: number inserted to list
 * Return: pointer to new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *ptr = *head, *temp;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);
	node->n = number;
	if (*head == NULL)
	{
		node->next = NULL;
		*head = node;
	}
	while (ptr != NULL)
	{
		temp = ptr->next;
		if (number > ptr->n && temp != NULL  && number < temp->n)
		{
			node->next = temp;
			ptr->next = node;
			return (node);
		}
		if (number > ptr->n && temp == NULL)
		{
			ptr->next = node;
			node->next = NULL;
			return (node);
		}
		if (number < ptr->n)
		{
			node->next = *head;
			*head = node;
			return (node);
		}
		if (number == ptr->n)
		{
			node->next = temp;
			ptr->next = node;
			return (node);
		}
		ptr = temp;
	}
	return (node);
}
