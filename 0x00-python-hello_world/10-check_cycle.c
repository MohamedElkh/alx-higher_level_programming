#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - function to checks if linked list contain cycle
 * @list: singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *cycle = list;
	listint_t *check = list;
	int fd = 0;

	while ((cycle && check) && check->next)
	{
		cycle = cycle->next;

		if (check->next || check->next->next)
		{
			check = check->next->next;
		}
		else
		{
			break;
		}
		if (cycle == check)
		{
			fd = 1;
			break;
		}
	}
	return (fd);

}
