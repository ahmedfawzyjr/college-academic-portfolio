import java.util.Scanner;

public class StringCount {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = input.nextLine();
        System.out.print("Enter character to count: ");
        char ch = input.nextLine().charAt(0);

        int count = countChar(str, ch);
        System.out.println("The character '" + ch + "' appears " + count + " time(s) in the string.");
    }

    public static int countChar(String str, char a) {
        int count = 0;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == a) {
                count++;
            }
        }
        return count;
    }
}
