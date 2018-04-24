////
////  hackerrank_day15.c
////
////  Created by Chorwon Kim on 2018. 4. 19..
////  Copyright © 2018년 Chorwon Kim. All rights reserved.
////
//
//#include <stdio.h>
//#include <stdlib.h>
//
//typedef struct Node {
//    int data;
//    struct Node *next;
//} Node;
//
//Node *insert(Node *head, int data) {
//    Node *newnode = (Node *)malloc(sizeof(Node *));
//    newnode->data = data;
//    newnode->next = NULL;
//    
//    if(head == NULL) {
//        head = newnode;
//    }
//    else {
//        Node *cur = (Node *)malloc(sizeof(Node *));
//        cur = head;
//        while(cur->next != NULL) {
//            cur = cur->next;
//        }
//        cur->next = newnode;
//    }
//    
//    return head;
//}
//
//// xcode에서는 printf 함수에다가 \n 안 넣어주면 출력 안해줌... 이유는 확인중.
//void display(Node *head) {
//    Node *start = head;
//    while(start) {
//        printf("%d \n", start->data);
//        start = start->next;
//    }
//}
//
//int main() {
//    int T, data;
//    scanf("%d", &T);
//    
//    Node *head = NULL;
//    
//    while(T-->0) {
//        scanf("%d", &data);
//        head = insert(head, data);
//    }
//    
//    display(head);
//    
//    return 0;
//}
