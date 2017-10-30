using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Function1
{
    class Program
    {
        static void Main(string[] args)
        {


            string[] str = System.IO.File.ReadAllLines("d:/1.txt", Encoding.Default);


            //string[] str = { "22","55","66"};
            //string s = string.Join("-", str);
            ////Console.WriteLine(s);
            ////Console.ReadKey();
            //string s1 = "a-b,c";
            //string[] nstr = s1.Split('-',',');
            int max = 0;
            string top="";
            for (int i = 0; i < str.Length; i++)
            {
                string[] temp = str[i].Split('|');
                int num = Convert.ToInt32(temp[1]);
                if (max < num) 
                {
                    max = num;
                    top = str[i];
                
                }


            }
            Console.WriteLine(top);
            Console.ReadKey();
        }
        //static string change(string str)
        //{
        //    char[] date = { '零', '一', '二', '三', '四', '五', '六', '七', '八', '九' }; 
        //    char[] ch=str.ToCharArray();
        //    for (int i = 0; i < ch.Length-1; i++) 
        //    {

        //        if (ch[i] >= '0' && ch[i] <='9')
        //        {
        //            int a = ch[i];
        //            ch[i] = date[int.Parse(a)];

        //        }
            
        //   } 
        //    string s = new string(ch);
        //    return s;
        //}
    }
}
