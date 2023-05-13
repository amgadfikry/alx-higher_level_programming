#include "lists.h"
/**
 * is_palindrome - check if list is palindrome or not
 * @head: pointer to link list
 * Return: 1 if true or 0 if false
 */
int is_palindrome(listint_t **head)
{
	listint_t *li = *head;
	int *ptr = NULL, i = 0, x = 0;

	if (head == NULL)
		return (1);
	while (li != NULL)
	{
		i++;
		ptr = realloc(ptr, i * sizeof(int));
		ptr[i - 1] = li->n;
		li = li->next;
	}
	while (i != 0)
	{
		if (ptr[x++] != ptr[--i])
		{
			free(ptr);
			return (0);
		}
	}
	free(ptr);
	return (1);
}
