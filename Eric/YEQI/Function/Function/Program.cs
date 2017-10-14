using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Function
{
    class Program
    {    
        static void Main(string[] args)
        {
            string[] num = {"aa","cc","cd"};
            
           Console.WriteLine(sentence(num,"|"));
           Console.ReadKey();
        }

        public static string sentence(string[] str, string tag)
        {
            string temp =str[0] ;
        for(int i=1;i<str.Length-1;i++)
            {
            temp=temp+tag+str[i];
            
            }
        return temp+tag+str[str.Length-1]+tag;
        }
    }
}
