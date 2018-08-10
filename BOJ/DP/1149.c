//
//  1149.c
//  Baekjoon
//
//  Created by Chorwon Kim on 2018. 7. 22..
//  Copyright © 2018년 Chorwon Kim. All rights reserved.
//

//#include <stdio.h>
//
//int main() {
//    int N, i;
//    int r, g, b;
//    int min;
//    int house[1000][3];
//    
//    scanf("%d", &N);
//    scanf("%d %d %d", &house[0][0], &house[0][1], &house[0][2]);
//    
//    for(i=1;i<N;i++) {
//        scanf("%d %d %d", &r, &g, &b);
//        
//        if(r + house[i-1][1] > r + house[i-1][2]) {
//            house[i][0] = r + house[i-1][2];
//        }
//        else {
//            house[i][0] = r + house[i-1][1];
//        }
//        
//        if(g + house[i-1][0] > g + house[i-1][2]) {
//            house[i][1] = g + house[i-1][2];
//        }
//        else {
//            house[i][1] = g + house[i-1][0];
//        }
//        
//        if(b + house[i-1][0] > b + house[i-1][1]) {
//            house[i][2] = b + house[i-1][1];
//        }
//        else {
//            house[i][2] = b + house[i-1][0];
//        }
//    }
//    
//    min = house[N-1][0];
//    
//    for(i=1;i<3;i++) {
//        
//        if(min > house[N-1][i]) {
//            min = house[N-1][i];
//        }
//    }
//    
//    printf("%d\n", min);
//    
//    return 0;
//    
//}
