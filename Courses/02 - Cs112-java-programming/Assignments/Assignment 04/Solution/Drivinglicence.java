import java.util.Scanner;

public class DrivingLicence {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter your age: ");
        int age = input.nextInt();

        if (age >= 18) {
            System.out.println("Eligible for a full driving license.");
        } else if (age >= 16) {
            System.out.println("Eligible for a learner permit only.");
        } else {
            System.out.println("Not eligible for a driving license.");
        }
    }
}
