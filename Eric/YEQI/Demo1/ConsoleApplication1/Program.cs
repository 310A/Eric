using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication1
{


  
    
    
    class Program
    {
        
        static void Main(string[] args)
        {
            int[] array=new int[10];
            for(int i=0;i<10;i++)
            {
            array[i]=100+i*2;

            
            }
            for(int j=0;j<10;j++)
            {
            Console.WriteLine("arry[{0}]:{1}",j,array[j]);
            }

            Console.ReadKey();
        }
    }
}
