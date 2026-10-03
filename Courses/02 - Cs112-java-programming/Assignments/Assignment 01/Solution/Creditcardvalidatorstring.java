import java.util.Scanner;

public class CreditCardValidatorString {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a credit card number as a String: ");
        String numberStr = input.nextLine().trim();

        if (isValid(numberStr)) {
            System.out.println(numberStr + " is valid");
        } else {
            System.out.println(numberStr + " is invalid");
        }
    }

    public static boolean isValid(String numberStr) {
        int size = numberStr.length();
        if (size < 13 || size > 16) return false;

        boolean validPrefix = numberStr.startsWith("4") || numberStr.startsWith("5") ||
                              numberStr.startsWith("37") || numberStr.startsWith("6");
        if (!validPrefix) return false;

        int totalSum = sumOfDoubleEvenPlace(numberStr) + sumOfOddPlace(numberStr);
        return (totalSum % 10 == 0);
    }

    public static int sumOfDoubleEvenPlace(String numberStr) {
        int sum = 0;
        for (int i = numberStr.length() - 2; i >= 0; i -= 2) {
            int digit = Character.getNumericValue(numberStr.charAt(i)) * 2;
            sum += getDigit(digit);
        }
        return sum;
    }

    public static int getDigit(int number) {
        return (number < 10) ? number : (number / 10 + number % 10);
    }

    public static int sumOfOddPlace(String numberStr) {
        int sum = 0;
        for (int i = numberStr.length() - 1; i >= 0; i -= 2) {
            sum += Character.getNumericValue(numberStr.charAt(i));
        }
        return sum;
    }
}
