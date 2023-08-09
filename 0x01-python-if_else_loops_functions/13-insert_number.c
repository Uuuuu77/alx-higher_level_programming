#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 * insert_node - Entry point-> It inserts node in a list
 * @head: input pointer to the first node
 * @number: input data to be added
 * Return: inserted  node (Success)
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *insert;

	insert = malloc(sizeof(listint_t));
	if (!insert)
		return (NULL);
	insert->n = number;
	temp = *head;
	if (temp == NULL || number < temp->n)
	{
		insert->next = temp;
		*head = insert;
		return (insert);
	}
	while (temp->next != NULL && number > temp->next->n)
		temp = temp->next;

	insert->next = temp->next;
	temp->next = insert;

	return (insert);
}
