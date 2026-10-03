// CS214: Visual Programming (C#)
// Visual Programming (C#) Implementation

using System;
using System.Collections.Generic;

namespace CS214App
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("C# Visual Programming Module - CS214: Visual Programming (C#)");
            List<string> modules = new List<string> { "UI Layer", "Logic Layer", "Data Layer" };
            foreach (var m in modules)
            {
                Console.WriteLine($"Initialized Component: {m}");
            }
        }
    }
}
