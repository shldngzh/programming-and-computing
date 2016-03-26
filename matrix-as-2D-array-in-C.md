# Matrix as 2D array in C

#### Motivating problem
Passing a 2d-array to function in c is... suffering, this because we _**cannot**_ do this:
```c
void func(int M[][], int m, int n) {
...
}
```
because some problem with double pointers (like pointer to the pointer is not blahblahblah I don't really care).  
However, we _**can**_ define a function to process matrix by predefining the column number of the matrix, like:
###### method 1
```c
void func(int M[][4], int m){
...
}
```
or
###### method 2
```c
func(int *M[], int n){
..
}
```

#### From defining matrix by dynamic memory allocation, to passing matrices to functions
###### predefine matrix by dynamic memory allocation
```c
double** predefine_matrix(int m, int n) {
        double **A;
        int i=0, j=0;

        A = (double *)malloc(m *sizeof(double *));
        for(i=0; i<m; i++){
                A[i] = (double *)malloc(n *sizeof(double));
        }

        for(i=0; i<m; i++){
                for(j=0; j<n; j++){
                        A[i][j] = 0;
                }
        }
        return A;
}

/*
int main(int argc, char* argv[]){
        double** C = predefine_matrix(3, 4);
        matrix_print(C, 3, 4); // later defined
        return 0;

}
*/
```
###### passing matrix to functions
```c
void func(doble **A, int m, int n){
...
}
```

###### matrix_print
```c
#include <stdio.h>

void matrix_print(double **M, int m, int n){
        int i, j = 0;
        for(i=0; i<m; i++){
                for(j=0; j<n; j++){

                if (j==0) { printf("\n"); }


        //      if (i == 0 && j == 0) { printf("[["); } // [[
        //      if (i != 0 && i != m-1 && j == 0) { printf("["); } // [

//              printf("%f\t", *(*(M+i)+j));
                printf("%.1f\t", M[i][j]);

        //      if (i != 0 && i != m-1 && j == n-1) { printf("]"); } //]
        //      if (i == m-1 && j == n-1) { printf("]]"); } // ]]
                }
        }
        printf("\n\n");
}
```

Thus my personal experience and feelings are: how important the class or OOP is.


