# Study Notes for C++ Programming

### 04/28/2016

### data type

#### declariation: typedef 
format:
```c++
typedef type newname;
```
example:
```c++
typedef int feet;
feet distance // same as int distance
```

#### enumerated types
format:
```c++
enum enum-name { list of names } var-list;
```
example:
```c++
enum color { red, green, blue } c; // optional ...{ red=1, green=2, blue=3 }...
c = blue;
```

### Variables

#### var declaration 
__extern__ to declare var, so later you do not mess up with the same name. Cannot initiate the __extern__ declared var in declaration, and must declare later in file.
example:
```c++
...
extern int a, b;

int main(){
...
}
```

#### lvalue & rvalue
* lvalue: expression refering to a memory location, may apper as lhs or rhs of an assignment
* rvalue: a data value that is stored at some address in memory, an expression that cannot have a value assigned to so only appears on rhs
```c++
int g = 20;
```

#### var scope
A var scope is a region of the program where vars can be declared:
* inside a function or a block, __local var__
* in the definition of cuntoin parameters, __formal parameters__
* outside of all functions, __global variables__

#### constants/literals
Cosntants refer to fixed values the program may not alter thus called __literals__

##### define constants
* by __#define__
* by __const__

```c++
#define identifier value
```
example:
```c++
#include <iostream>
...
#define LENGTH 10
#define WIDTH 5
#define NEWLINE '\n'
...
```
```c++
...
int main(){
    const int LENGTH = 10;
    const int WIDTH = 5;
    const char NEWLINE = '\n';
    ...
}
```

#### modifier types
__char, int, double__
* __signed__, int, char, long, short
* __unsigned__, int, char, long, short
* __long__, int, double
* __short__, int

can be used without __int__

### Storage Classes 
A storage class defines the scope (visibility) and life-time of variables and/or functions within a C++ program. 
* auto, only used within functions (local var)
* register, define local var to (may) be stored in a register instead of RAM (no memory location). Used for var requires quick access such as counters.
* static, instucts the compiler to keep a local var in existence during the life-time of the program rather than creating and destroying it each time it comes into and goes out of scope.
```c++
#include <iostream>
 
// Function declaration
void func(void);
 
static int count = 10; /* Global variable */
 
main()
{
    while(count--)
    {
       func();
    }
    return 0;
}
// Function definition
void func( void )
{
    static int i = 5; // local static variable
    i++;
    std::cout << "i is " << i ;
    std::cout << " and count is " << count << std::endl;
}
```
```
i is 6 and count is 9
i is 7 and count is 8
i is 8 and count is 7
i is 9 and count is 6
i is 10 and count is 5
i is 11 and count is 4
i is 12 and count is 3
i is 13 and count is 2
i is 14 and count is 1
i is 15 and count is 0
```
* extern
* mutable

### Operators
* __arithmetic__: +, -, *, /, %, ++, --
* __relational__: ==, !=, >, <, >=, <= 
* __logical__: &&, ||, !
* __bitwise__: &, | ^, ~, <<, >>
* __assignment__: =, +=, -=, *=, /=, %=, <<=, >>=, &=, ^=, !=
* __misc__: sizeof, condition ?, ,, . and ->, Cast, & (pointer, return address of an var), * (pointer to an var, *v will pointer to an var v)
condition:
```c++
if (y < 10) {
    var = 30;
}else{
    var = 40;
    }

x = (y < 10) ? 30 : 40;
```

### Functions
```c++
return_type funtion_name( parameter list ){
    function body
}
```
__function declarations__: tells the compiler a function which can be defined separately.
```c++
int max(int, int)
```
is also valid.

#### function arguments
__call by value__
```c++
void swap(int x, int y){
    ...
    return;
}

...

int main(){
    ...
    swap(a, b);
    ...
    return 0;
}
```
__call by pointer__
```c++
// function definition to swap the values.
void swap(int *x, int *y)
{
   int temp;
   temp = *x; /* save the value at address x */
   *x = *y; /* put y into x */
   *y = temp; /* put x into y */
  
   return;
}
```
```c++
#include <iostream>
using namespace std;

// function declaration
void swap(int *x, int *y);

int main ()
{
   // local variable declaration:
   int a = 100;
   int b = 200;
 
   cout << "Before swap, value of a :" << a << endl;
   cout << "Before swap, value of b :" << b << endl;

   /* calling a function to swap the values.
    * &a indicates pointer to a ie. address of variable a and 
    * &b indicates pointer to b ie. address of variable b.
    */
   swap(&a, &b);

   cout << "After swap, value of a :" << a << endl;
   cout << "After swap, value of b :" << b << endl;
 
   return 0;
}
```
__call by reference__
```c++
// function definition to swap the values.
void swap(int &x, int &y)
{
   int temp;
   temp = x; /* save the value at address x */
   x = y;    /* put y into x */
   y = temp; /* put x into y */
  
   return;
}
```
```c++
#include <iostream>
using namespace std;

// function declaration
void swap(int &x, int &y);

int main ()
{
   // local variable declaration:
   int a = 100;
   int b = 200;
 
   cout << "Before swap, value of a :" << a << endl;
   cout << "Before swap, value of b :" << b << endl;

   /* calling a function to swap the values using variable reference.*/
   swap(a, b);

   cout << "After swap, value of a :" << a << endl;
   cout << "After swap, value of b :" << b << endl;
 
   return 0;
}
```

### Numbers
__<cmath>__: 

cos, sin, tan, log, pow(double, double), hypot(double, double), sqrt, int abs(int), double fabs(double), floor

rand(), srand()

### Arrays
    

