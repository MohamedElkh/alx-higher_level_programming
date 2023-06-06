#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - function to insert num into linked list
 * @head: the top of data stored in linked list
 * @number: the number to be checked
 *
 * Return: new number add.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *now = NULL;
	listint_t *new = NULL;
	listint_t *tmp = NULL;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;

	if (*head)
	{
		now = *head;

		if (number <= now->n)
		{
			new->next = now;
			*head = new;
		}
		else
		{
			while (now->next)
			{
				if (number <= now->next->n)
				{
					tmp = now->next;
					now->next = new;
					new->next = tmp;
					return (*head)
				}
				now = now->next;
			}
			tmp = now->next;
			now->next = new;
			new->next = tmp;
		}
		return (*head);
	}
	new->next = NULL;
	*head = new;
	return (*head);
}
