
While learning PYTHON, I wanted to revisit my project of converting Roman numerals to standard numbers,
which I previously implemented in C#. And this time, I approached the topic from a slightly different angle :)



####################################################################  -- C#

using System;
using System.Collections;

public class RomanRakam
{

    public static string toNumber(string roman)
    {
        roman = roman.ToUpper();

        Hashtable liste = new Hashtable();
        liste.Add("I", "1");
        liste.Add("V", "5");
        liste.Add("X", "10");
        liste.Add("L", "50");
        liste.Add("C", "100");
        liste.Add("D", "500");
        liste.Add("M", "1000");

        int total = 0;
        int aratoplam = 0;
        int sayac = 1;

        if (roman.Length == 2)
        {
            sayac = 0;
        }

        for (int i = 0; i < roman.Length; i++)
        {
            if (roman.Length - i >= 2 && sayac == 0)
            {
                string data = roman[i].ToString() + roman[i + 1].ToString();

                if (data != null)
                {
                    int oD = 0;

                    for (int j = 0; j < data.Length; j++)
                    {
                        string nextData = data[j].ToString();
                        int nD = int.Parse(liste[nextData].ToString());

                        if (nextData == data[0].ToString())
                        {
                            aratoplam = int.Parse(liste[nextData].ToString()) + aratoplam;
                            //oldData = nextData;
                            oD = int.Parse(liste[nextData].ToString());
                        }
                        else if (oD > nD)
                        {
                            aratoplam = int.Parse(liste[nextData].ToString()) + aratoplam;
                        }
                        else
                        {
                            aratoplam = int.Parse(liste[nextData].ToString()) - aratoplam;
                        }
                    }

                    i++;
                    total = aratoplam + total;
                    aratoplam = 0;
                }
            }

            else
            {
                total = int.Parse(liste[roman[i].ToString()].ToString()) + total;
                sayac = 0;
            }
        }
        return total.ToString();
    }
    
    public static void Main(string[] args)
    {
        
        Console.WriteLine(toNumber("MCMVII"));
        Console.WriteLine(toNumber("MMXI"));
        Console.WriteLine(toNumber("XC"));
        Console.WriteLine(toNumber("MCMXC"));
        Console.WriteLine(toNumber("MCMX"));
        Console.WriteLine(toNumber("MCmxCII"));
        Console.WriteLine(toNumber("dVl"));

    }
}

####################################################################
