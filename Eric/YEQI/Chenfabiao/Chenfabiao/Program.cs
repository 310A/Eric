using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Chenfabiao
{
    class Program
    {
        static void Main(string[] args)
        {

            /*Console.WriteLine("请输入行数");
            string x = Console.ReadLine();
            int y = Convert.ToInt16(x);
            for (int a = 1; a <= y; a++)
            {
                

                for (int b = 1; b <=y-a;b++) 
                {

                    Console.Write(" ");

                
                }
                for (int c = 1; c <= 2*a-1; c++)
                {

                    Console.Write("*");


                }


                

                Console.WriteLine();
               


            }


            Console.ReadKey();*/


           /* Console.WriteLine("请输入行数");
            string x = Console.ReadLine();
            int y = Convert.ToInt16(x);
            for (int a = 1; a <= y; a++)
            {


                for (int b = 1; b <= y - a; b++)
                {

                    Console.Write(" ");


                }
                for (int c = 1; c <= a; c++)
                {

                    Console.Write("*");


                }




                Console.WriteLine();



            }


            Console.ReadKey();*/

            //Console.WriteLine("请输入行数");
            //string x = Console.ReadLine();
            //int y = Convert.ToInt16(x);
            //for (int a = 1; a <= y; a++)
            //{


            //    for (int b = 1; b <= a-1; b++)
            //    {

            //        Console.Write(" ");


            //    }
            //    for (int c = 1; c <= 2*y+1-2*a; c++)
            //    {

            //        Console.Write("*");


            //    }




            //    Console.WriteLine();



            //}


            //Console.ReadKey();

            Console.WriteLine("请输入行数");
            string x = Console.ReadLine();
            int y = Convert.ToInt16(x);
            for (int a = 1; a <= y; a++)
            {


                for (int b = 1; b <= a - 1; b++)
                {

                    Console.Write(" ");


                }
                for (int c = 1; c <= y-a+1; c++)
                {

                    Console.Write("*");


                }




                Console.WriteLine();



            }


            Console.ReadKey();

        }
    }
}
