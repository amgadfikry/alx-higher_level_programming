#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - check if it singl link list
 * or it circle linked list
 * @list: input linked list checked
 * Return: 0 if no cycle or 1 if there is cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (temp != NULL)
	{
		temp = temp->next;
		if (temp == list)
			return (1);
	}

	return (0);
}
