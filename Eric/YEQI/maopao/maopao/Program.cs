using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace maopao
{
    class Program
    {
        static void Main(string[] args)
        {
            int temp;
            int[] num = {2,3,4,1,1,100,5,8,9};
            for (int i = 0; i < num.Length-1; i++) 
            {

                for (int j = 0; j < num.Length - i-1; j++)
                {
                    if (num[j] > num[j + 1])
                    {
                        temp = num[j];
                        num[j] = num[j + 1];
                        num[j + 1] = temp;
                    }

                }
            
            }
            for (int a = 0; a < num.Length; a++) 
            {

                Console.Write("{0} ", num[a]);


            } Console.ReadKey();
        }
    }
}
