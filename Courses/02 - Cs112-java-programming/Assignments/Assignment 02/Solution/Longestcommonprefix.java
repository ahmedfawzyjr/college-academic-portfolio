import java.util.Scanner;

public class LongestCommonPrefix {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the first string: ");
        String s1 = input.nextLine();
        System.out.print("Enter the second string: ");
        String s2 = input.nextLine();

        int minLen = Math.min(s1.length(), s2.length());
        StringBuilder prefix = new StringBuilder();

        for (int i = 0; i < minLen; i++) {
            if (s1.charAt(i) == s2.charAt(i)) {
                prefix.append(s1.charAt(i));
            } else {
                break;
            }
        }

        if (prefix.length() > 0) {
            System.out.println("The common prefix is: " + prefix);
        } else {
            System.out.println(s1 + " and " + s2 + " have no common prefix.");
        }
    }
}
