//
//  1004.c
//  Baekjoon
//
//  Created by Chorwon Kim on 2018. 4. 19..
//  Copyright © 2018년 Chorwon Kim. All rights reserved.
//

#include <stdio.h>
#include <math.h>

typedef struct point {
    int xpos;
    int ypos;
} Point;

typedef struct circle {
    int x_value;
    int y_value;
    int radius;
} Circle;

int main() {
    int timer, i;
    int test_timer, j;
    int result;
    double d1, d2;
    Point p[2];
    Circle c[50];
    
    scanf("%d", &timer);
    
    for(i=0;i<timer;i++) {
        result = 0;
        scanf("%d %d %d %d", &p[0].xpos, &p[0].ypos, &p[1].xpos, &p[1].ypos);
        
        scanf("%d", &test_timer);
        
        for(j=0;j<test_timer;j++) {
            scanf("%d %d %d", &c[j].x_value, &c[j].y_value, &c[j].radius);
            
            d1 = sqrt(pow(p[0].xpos - c[j].x_value, 2) + pow(p[0].ypos - c[j].y_value, 2));
            d2 = sqrt(pow(p[1].xpos - c[j].x_value, 2) + pow(p[1].ypos - c[j].y_value, 2));
            
            if(d1 <= c[j].radius && d2 <= c[j].radius) {
                continue;
            }
            else if(d1 <= c[j].radius) {
                result++;
            }
            else if(d2 <= c[j].radius) {
                result++;
            }
        }
        
        printf("%d\n", result);
    }
    
    return 0;
}
