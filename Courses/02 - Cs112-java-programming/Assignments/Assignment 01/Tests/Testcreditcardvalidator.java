public class TestCreditCardValidator {
    public static void main(String[] args) {
        long validCard = 4388576018410707L;
        boolean result = CreditCardValidatorMath.isValid(validCard);
        if (result) {
            System.out.println("TEST PASSED: " + validCard + " recognized as valid.");
        } else {
            System.err.println("TEST FAILED: " + validCard + " should be valid!");
            System.exit(1);
        }
    }
}
