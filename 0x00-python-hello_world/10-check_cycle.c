#include "lists.h"

/**
 * check_cycle - Entry point-> which checks for a cycle in the list.
 * @list: input list to be checked
 * Return: 1 (Found), OR 0 (Not Found)
*/
int check_cycle(listint_t *list)
{
	listint_t *point_a;
	listint_t *point_b;

	if (list == NULL)
		return (0);
	point_a = list;
	point_b = list->next;

	while (point_a && point_b && point_b->next)
	{
		if (point_a == point_b)
			return (1);
		point_a = point_a->next;
		point_b = point_b->next->next;
	}

	return (0);
}
