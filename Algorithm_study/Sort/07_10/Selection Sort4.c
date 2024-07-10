#include <stdio.h>

int main()
{
    int N, K = 0;
    int A[500001] = {};
    scanf("%d", &N);
    scanf("%d", &K);
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &A[i]);
    }

    for (int last = N - 1; last > 0; last--)
    {
        for (int u = 0; u < N; u++){
            printf("%d ", A[u]);
        }
        int max_value, max_index = 0;
        for (int k = 0; k <= last; k++)
        {
            printf("%d", k);
            if (A[k] > max_value)
            {
                max_value = A[k];
                max_index = k;
            }
            if (last != max_index)
            {
                int temp = 0;
                temp = A[last];
                A[last] = A[max_index];
                A[max_index] = temp;
                K--;
                if (K == 0)
                {
                    for (int u = 0; u < N; u++)
                    {
                        printf("%d ", A[u]);
                    }
                    return 0;
                }
            }
        }
        printf("-1");
    }
}