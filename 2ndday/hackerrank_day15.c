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
//// 해당 부분 코드 실행 안 됨.. 왜 그런지는 모르겠지만..
//void display(Node *head) {
//    Node *start = head;
//    while(start) {
//        printf("%d ", start->data);
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
