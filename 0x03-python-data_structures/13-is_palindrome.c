#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * linkedlist_len - function to count the number of elements
 * @heads: the linked list to count
 *
 * Return: the count of lists in linked list
 */

size_t linkedlist_len(const listint_t *heads)
{
	int le = 0;

	while (heads != NULL)
	{
		++le;
		heads = heads->next;
	}

	return (le);
}

/**
 * get_node - function to get node from linked list
 * @h: the head of the linked list
 * @i: the index to find it
 *
 * Return: find the node.
 */

listint_t *get_node(listint_t *h, unsigned int i)
{
	unsigned int the_times = 0;
	listint_t *now = h;

	if (h)
	{
		while (now != NULL)
		{
			if (the_times == i)
			{
				return (now);
			}
			now = now->next;
			++the_times;
		}
	}
	return (NULL);
}

/**
 * is_palindrome - func to check if linked list is palindrome
 * @head: the head of linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *st = NULL;
	listint_t *final = NULL;
	unsigned int x = 0, length = 0;
	unsigned int len_c = 0, len_lis = 0;

	if (head == NULL)
	{
		return (0);
	}
	if (*head == NULL)
	{
		return (1);
	}

	st = *head;
	length = linkedlist_len(st);
	len_c = length * 2;
	len_lis = len_c - 2;
	final = *head;

	for (; x < len_c; x = x + 2)
	{
		if (st[x].n != final[len_lis].n)
		{
			return (0);
		}
		len_lis = len_lis - 2;
	}
	return (1);
}
