using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace digui
{
    class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine("shuruyigeshu");
            string num = Console.ReadLine();
            int a = Convert.ToInt16(num);
            Program p = new Program();
            Console.WriteLine(p.recursion(a));
        }
            public  int recursion(int n)
            {
            
            if(n==1) 
                return 1;
            else
                return n*recursion(n-1);
            
            
            }

        }
    }

