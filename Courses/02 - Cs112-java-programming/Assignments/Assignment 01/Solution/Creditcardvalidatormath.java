import java.util.Scanner;

public class CreditCardValidatorMath {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a credit card number as a Long integer: ");
        long number = input.nextLong();

        if (isValid(number)) {
            System.out.println(number + " is valid");
        } else {
            System.out.println(number + " is invalid");
        }
    }

    public static boolean isValid(long number) {
        boolean validPrefix = prefixMatched(number, 4) || prefixMatched(number, 5) ||
                              prefixMatched(number, 37) || prefixMatched(number, 6);
        int totalSum = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number);
        int size = getSize(number);

        return (size >= 13 && size <= 16) && validPrefix && (totalSum % 10 == 0);
    }

    public static int sumOfDoubleEvenPlace(long number) {
        int sum = 0;
        number /= 10;
        while (number > 0) {
            int digit = (int)((number % 10) * 2);
            sum += getDigit(digit);
            number /= 100;
        }
        return sum;
    }

    public static int getDigit(int number) {
        if (number < 10) return number;
        return (number / 10) + (number % 10);
    }

    public static int sumOfOddPlace(long number) {
        int sum = 0;
        while (number > 0) {
            sum += (int)(number % 10);
            number /= 100;
        }
        return sum;
    }

    public static boolean prefixMatched(long number, int d) {
        return getPrefix(number, getSize(d)) == d;
    }

    public static int getSize(long d) {
        int count = 0;
        while (d > 0) {
            count++;
            d /= 10;
        }
        return count;
    }

    public static long getPrefix(long number, int k) {
        int size = getSize(number);
        if (size > k) {
            for (int i = 0; i < size - k; i++) {
                number /= 10;
            }
            return number;
        }
        return number;
    }
}
