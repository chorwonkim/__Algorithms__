//
//  codeup_1581.c
//  Baekjoon
//
//  Created by Chorwon Kim on 2018. 4. 19..
//  Copyright © 2018년 Chorwon Kim. All rights reserved.
//

#include <stdio.h>

void myswap(int *a, int *b) {
    {
        int temp = *a;
        *a = *b;
        *b = temp;
    }
}

int main() {
    int num1, num2;
    
    scanf("%d %d", &num1, &num2);
    
    myswap(&num1, &num2);
    
    printf("%d %d\n", num1, num2);
    
    return 0;
}
