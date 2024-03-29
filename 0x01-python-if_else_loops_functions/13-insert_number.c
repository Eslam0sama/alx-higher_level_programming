#include "lists.h"
/**
 * insert_node - A function that insert node in sorted list
 * @head: The head of the list
 * @number: The new number to be added
 * Return: the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *temp, *new_node;

	current = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}
	else if (current->next == NULL && current->n < number)
	{
		current->next = new_node;
		return (current->next);
	}
	else if (current->next == NULL && current->n > number)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}
	else
	{
		while (current->n < number)
		{
			temp = current;
			current = current->next;
		}
		temp->next = new_node;
		new_node->next = current;
		return (temp->next);
	}
}
