//
//  11650.c
//  Baekjoon
//
//  Created by Chorwon Kim on 2018. 4. 19..
//  Copyright © 2018년 Chorwon Kim. All rights reserved.
//

#include <stdio.h>

typedef struct coordinate {
    int xpos;
    int ypos;
} Cor;

Cor list[100001];

// 더러워서 퀵소트 씀...ㅅㅂ
void SwapX(int a, int b) {
    Cor temp = list[a];
    list[a] = list[b];
    list[b] = temp;
}


void SwapY(int a, int b) {
    Cor temp = list[a];
    list[a] = list[b];
    list[b] = temp;
}

int PartitionX(int left, int right) {
    Cor pivot = list[left];
    int low = left+1;
    int high = right;
    
    while(low <= high) {
        while(pivot.xpos >= list[low].xpos && low <= right) {
            low++;
        }
        
        while(pivot.xpos <= list[high].xpos && high >= (left + 1)) {
            high--;
        }
        
        if(low <= high) {
            SwapX(low, high);
        }
    }
    SwapX(left, high);
    return high;
}

int PartitionY(int left, int right) {
    Cor pivot = list[left];
    int low = left+1;
    int high = right;
    
    while(low <= high) {
        while(pivot.ypos >= list[low].ypos && low <= right) {
            low++;
        }
        
        while(pivot.ypos <= list[high].ypos && high >= (left + 1)) {
            high--;
        }
        
        if(low <= high) {
            SwapY(low, high);
        }
    }
    SwapY(left, high);
    return high;
}

void QuickSortX(int left, int right) {
    if(left <= right) {
        int pivot = PartitionX(left, right);
        QuickSortX(left, pivot-1);
        QuickSortX(pivot+1, right);
    }
}

void QuickSortY(int left, int right) {
    if(left <= right) {
        int pivot = PartitionY(left, right);
        QuickSortY(left, pivot-1);
        QuickSortY(pivot+1, right);
    }
}

int main() {
    int x, i;
    int start, end;
    int cnt = 0;
    
    scanf("%d", &x);
    
    for(i=0;i<x;i++) {
        scanf("%d %d", &list[i].xpos, &list[i].ypos);
    }
    
//    // insert sorting // wrong answer
//    for(i=1;i<x;i++) {
//        temp = list[i];
//        j = i-1;
//        while(j>=0 && list[j].xpos >= temp.xpos) {
//            if(list[j].ypos > temp.ypos) {
//                list[j+1] = list[j];
//                j = j-1;
//            }
//            else
//                break;
//        }
//        list[j+1] = temp;
//    }
    
    QuickSortX(0, x-1);
    
    i = 1;
    start = 0;
    end = x-1;
    
    while(i<x) {
        if(list[i].xpos == list[i-1].xpos) {
            cnt = 1;
            start = i-1;
            while(list[i].xpos == list[i-1].xpos) {
                end = i;
                i++;
            }
        }
        
        if(cnt>=1) {
            QuickSortY(start, end);
            start = i;
        }
        cnt = 0;
        i++;
    }
    
    for(i=0;i<x;i++) {
        printf("%d %d\n", list[i].xpos, list[i].ypos);
    }
    
    return 0;
}
