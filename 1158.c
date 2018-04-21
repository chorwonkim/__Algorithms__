////
////  1158.c
////  Baekjoon
////
////  Created by Chorwon Kim on 2018. 4. 19..
////  Copyright © 2018년 Chorwon Kim. All rights reserved.
////
//

#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *next;
} Node;

Node *head;

Node * init(int N) {
    int i;
    
    Node *temp = (Node *)malloc(sizeof(Node));
    
    temp->data = 1;
    head = temp;
    
    for(i=2;i<=N;i++) {
        temp->next = (Node *)malloc(sizeof(Node));
        temp = temp->next;
        temp->data = i;
    }
    
    temp->next = head;  // 마지막은 처음으로(환형)
    
    return temp;
}

void pop(Node **start, int M) {
    int i;
    Node *s;
    
    for(i=0;i<M-1;i++) {
        *start = (*start)->next;
    }
    
    printf("%d\n", (*start)->next->data);
    
    s = (*start)->next;
    (*start)->next = (*start)->next->next;
    
    free(s);
}

// Need to delete \n in printf. (Xcode Bug I think)
int main() {
    
    int N, M;
    
    scanf("%d %d", &N, &M);
    
    Node *p = init(N);
    
    printf("<\n");
    
    while(p != p->next) {
        pop(&p, M);
        if(N!=0) {
            printf(", \n");
        }
    }
    printf("%d\n", p->data);
    printf(">\n");
    
    return 0;
}
