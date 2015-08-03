#include<stdio.h>
#define BITSPERWORD 32
#define SHIFT 5
#define MASK 0x1F
#define N 10000000
int a[1 + N/BITSPERWORD];
 
void set(int i) { 
    printf("\tset > %d, ", a[i>>SHIFT]);  // 0
    a[i>>SHIFT] |= (1<<(i & MASK)); 
    printf("%d\n", a[i>>SHIFT]);  // 32768
}
void clr(int i) { 
    printf("\tclr > %d, ", a[i>>SHIFT]);  // 32768
    a[i>>SHIFT] &= ~(1<<(i & MASK));
    printf("%d\n", a[i>>SHIFT]);  // 0
}
int test(int i) { return a[i>>SHIFT] & (1<<(i & MASK)); }

int main() {
    int arr[10] = {7680933,1915563,2138465,4410815,9895334,
        6319075,3267312,9921634,2944834,7401574};

    for(int i = 0; i < 10; i++) {
        printf("int %d\n", arr[i]);
        set(arr[i]);
        clr(arr[i]);
    }
    
    return 0;
}


// 컴파일 명령
// gcc -o exercise02 exercise02.c