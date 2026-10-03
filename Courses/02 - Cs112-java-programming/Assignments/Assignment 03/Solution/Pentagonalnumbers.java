public class PentagonalNumbers {
    public static void main(String[] args) {
        final int NUMBER_OF_PENTAGONALS = 100;
        final int NUMBER_PER_LINE = 10;

        System.out.println("The first 100 pentagonal numbers are:");
        for (int i = 1; i <= NUMBER_OF_PENTAGONALS; i++) {
            System.out.printf("%7d ", getPentagonalNumber(i));
            if (i % NUMBER_PER_LINE == 0) System.out.println();
        }
    }

    public static int getPentagonalNumber(int n) {
        return n * (3 * n - 1) / 2;
    }
}
