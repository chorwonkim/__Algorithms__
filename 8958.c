//
//  8958.c
//  Baekjoon
//
//  Created by Chorwon Kim on 2018. 4. 19..
//  Copyright © 2018년 Chorwon Kim. All rights reserved.
//

#define _CRT_SECURE_NO_WARNINGS // scanf 보안 경고로 인한 컴파일 에러 방지
#include <stdio.h>
#include <stdlib.h> // malloc, free 함수가 선언된 헤더 선언
#include <string.h>

int main() {
    
    int x=0, i=0, j=0;
    int count, result;
    char s1[80];
    
    scanf("%d", &x);
    
    for(i=0;i<x;i++) {
        count = 0;
        result = 0;
        scanf("%s", s1);
        for(j=0;j<strlen(s1);j++) {
            if(s1[j] == 'O' || s1[j] == 'o') {
                count++;
                result += count;
            }
            else if(s1[j] == 'X' || s1[j] == 'x') {
                count = 0;
                continue;
            }
        }
        
        printf("%d\n", result);
    }
    
    return 0;
}
