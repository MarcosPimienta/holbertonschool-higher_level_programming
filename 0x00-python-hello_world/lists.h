#ifndef lists
#define lists
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct list_s
{
	char *str;
	unsigned int len;
	struct list_s *next;
} list_t;

list_t *add_node(list_t **head, const char *str);
void free_list(list_t *head);

#endif