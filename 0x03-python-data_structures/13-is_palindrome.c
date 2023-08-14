#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * is_palindrome - Entry point-> It checks if a list is palindrome.
 * @head: input pointer to the first node
 * Return: 1 if (Palindrome) or 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *a, *b, *temp, *prev = NULL;

	a = *head;
	b = *head;

	while (a && a->next)
	{
		a = a->next->next;
		b = b->next;
	}
	while (b)
	{
		temp = b->next;
		b->next = prev;
		prev = b;
		b = temp;
	}
	while (prev)
	{
		if ((*head)->n != prev->n)
			return (0);
		*head = (*head)->next;
		prev = prev->next;
	}
	return (1);
}
