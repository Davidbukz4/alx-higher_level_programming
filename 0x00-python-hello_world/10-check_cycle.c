#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: list head
 * Return: 0 if it does not have a cycle, 1 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_s *slow = list, *fast = list;

	if (!list || !list->next)
		return (0);
	while (slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
