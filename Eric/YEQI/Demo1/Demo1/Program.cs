using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ConsoleApplication1
{



    class rectangle
    {
        int length;
        int width;
        public void initial()
        {
            Console.WriteLine("SHURU CHANG");
            String chang = Console.ReadLine();
            length = Convert.ToInt16(chang);
            Console.WriteLine("shuru kuan");
            String kuan = Console.ReadLine();
            width = Convert.ToInt16(kuan);
        }
        public int getlen() 
        {
            return length;
        }

        public int getwid()
        {
            return width;
        }
        public int area() 
        {
            return length * width;
        }

    }



    class Program
    {
        static void Main(string[] args)
        {
            rectangle rec=new rectangle();
            rec.initial();
            
            Console.WriteLine("mianjiwei:{0}",rec.area());
            Console.ReadKey();
        }
    }

}