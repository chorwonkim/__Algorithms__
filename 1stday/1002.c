//
//  main.c
//  baekjoon1002
//
//  Created by Chorwon Kim on 2018. 4. 18..
//  Copyright © 2018년 Chorwon Kim. All rights reserved.
//

//#include <stdio.h>
//
//int main(int argc, const char * argv[]) {
//    // insert code here...
//    printf("Hello, World!\n");
//    return 0;
//}

#include <stdio.h>
#include <math.h>

int main() {
    int t, x1, y1, r1, x2, y2, r2;
    
    scanf("%d", &t);
    for(;t>0;t--) {
        scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);
        double i = sqrt(pow(x1-x2, 2.0) + pow(y1-y2, 2.0));
        
        if(x1 == x2 && y1 == y2) {
            if (r1 == r2)
                printf("-1\n");
            else
                printf("0\n");
        }
        else {
            if((r1+r2) > i && abs(r1-r2) < i)
                printf("2\n");
            else if((r1+r2) == i || abs(r1-r2) == i)
                printf("1\n");
            else
                printf("0\n");
        }
    }
    
    return 0;
}
