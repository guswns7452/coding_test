#include <stdio.h>

int main(){
    int N, K = 0;
    int A[10001] = {};
    scanf("%d", &N);
    scanf("%d", &K);
    for(int i = 0; i < N; i++){
        scanf("%d",&A[i]);
    }

    for(int last = N-1; last > 0; last--){
        for (int i=0;i<last;i++){
            if (A[i] > A[i+1]){
                int temp = 0;
                temp = A[i];
                A[i] = A[i+1];
                A[i+1] = temp; 
                K--;
                if (K == 0){
                    printf("%d %d", A[i], A[i+1]);
                    return 0;
                }
            }
                
        }
    }
    printf("-1");
}