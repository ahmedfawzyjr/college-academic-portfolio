public class TestAssignment02 {
    public static void main(String[] args) {
        if (PalindromeInteger.isPalindrome(12321) && !PalindromeInteger.isPalindrome(12345)) {
            System.out.println("TEST PASSED: Palindrome integer logic verified.");
        } else {
            System.err.println("TEST FAILED");
            System.exit(1);
        }
    }
}
