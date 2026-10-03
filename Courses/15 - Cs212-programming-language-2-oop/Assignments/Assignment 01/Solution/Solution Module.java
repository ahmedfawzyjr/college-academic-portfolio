// CS212: Programming Language II (OOP)
// Practical Java Implementation

public class DemoCS212 {
    public static void main(String[] args) {
        System.out.println("Java execution module for CS212: Programming Language II (OOP)");
        int[] scores = {85, 92, 78, 90, 88};
        int max = scores[0];
        for (int s : scores) {
            if (s > max) max = s;
        }
        System.out.println("Highest score recorded: " + max);
    }
}
