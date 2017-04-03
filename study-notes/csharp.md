### C# program components

* Namespace declaration
* A class
* Class methods
* Class attributes
* A Main method
* Statements and Expressions
* Comments

```csharp
using System;
namespace RectangleApplication
{
   class Rectangle 
   {
      // member variables
      double length;
      double width;
      public void Acceptdetails()
      {
         length = 4.5;    
         width = 3.5;
      }
      
      public double GetArea()
      {
         return length * width; 
      }
      
      public void Display()
      {
         Console.WriteLine("Length: {0}", length);
         Console.WriteLine("Width: {0}", width);
         Console.WriteLine("Area: {0}", GetArea());
      }
   }
   
   class ExecuteRectangle 
   {
      static void Main(string[] args) 
      {
         Rectangle r = new Rectangle();
         r.Acceptdetails();
         r.Display();
         Console.ReadLine(); 
      }
   }
}
```

* `using` includes the namespaces, like `includ` in Python
* `namespace` defines a namespace
* `class` declares a class
    * instantiating a class:
    `ClassName instance = new ClassName();`
    
    
## function params passed as value but NOT ref
* function do not change the values at the end
```csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp {
    class PassingParam {

        class classX {

            public int x { get; set; }
            public int y { get; set; }

            public classX() {
                this.x = 1;
                this.y = 10;
            }

        }

        class classY {

            public void foo(int x, int y) {
                int z = 0;

                Console.WriteLine(x);
                Console.WriteLine(y);
                Console.WriteLine(z);

                x += 100;
                y += 100;
                z += -100;

                Console.WriteLine(x);
                Console.WriteLine(y);
                Console.WriteLine(z);
            }

            public static void foo2(int x, int y) {
                int z = 0;
                z = x + y;

                Console.WriteLine(x);
                Console.WriteLine(y);
                Console.WriteLine(z);



                x += 100;
                y += 100;
                z = x + y;

                Console.WriteLine(x);
                Console.WriteLine(y);
                Console.WriteLine(z);
            }

            public classY() {

            }
        }


        public void Main() {

            classX xx = new classX();
            classY yy = new classY();

            yy.foo(xx.x, xx.y);
            classY.foo2(xx.x, xx.y);

            Console.WriteLine(xx.x);
            Console.WriteLine(xx.y);

            Console.ReadLine();
        }
    }
}
```
