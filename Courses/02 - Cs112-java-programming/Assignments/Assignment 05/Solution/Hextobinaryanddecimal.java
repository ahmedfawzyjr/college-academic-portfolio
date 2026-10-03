import java.util.Scanner;

public class HexToBinaryAndDecimal {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a hex digit: ");
        String hex = input.nextLine().trim();

        if (hex.length() != 1) {
            System.out.println("You must enter exactly one character");
            return;
        }

        char ch = Character.toUpperCase(hex.charAt(0));
        int value;
        if (ch >= '0' && ch <= '9') {
            value = ch - '0';
        } else if (ch >= 'A' && ch <= 'F') {
            value = ch - 'A' + 10;
        } else {
            System.out.println(hex + " is an invalid input");
            return;
        }

        System.out.println("Decimal value: " + value);
        System.out.println("Binary value: " + Integer.toBinaryString(value));
    }
}
