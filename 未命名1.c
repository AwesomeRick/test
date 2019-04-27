#include<stdio.h>
#include<stdlib.h>

typedef struct node* List;
//定义结构体变量 
struct node
{
    int data;
    struct node *next;
};

int Input();
void Print_list(List s);

int main(void)
{
	List a;
	a = Input;
	Print_list(a);
}


int Input()
{
	List head,temp,end;
	int x;
	head = (List)malloc(sizeof(struct node));
	end = head;
	scanf("%d",&x);
	while(x != -1)
	{
		temp = (List)malloc(sizeof(struct node));
		temp->data = x;
		end->next = temp;
		end = temp;
		scanf("%d",&x);
	}
	end->next = NULL;
	return head;
}


void Print_list(List s)
{
	s = s->next;
	while(s != NULL)
	{
		if (s->next != NULL)
			printf("%d->",s->data);
		else
			printf("%d",s->data);
		s = s->next;
	}
	return;
}

