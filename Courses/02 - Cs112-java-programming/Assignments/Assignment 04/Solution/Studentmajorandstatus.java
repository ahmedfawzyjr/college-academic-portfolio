import java.util.Scanner;

public class StudentMajorAndStatus {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter two characters (e.g. M1, C2, I4): ");
        String str = input.nextLine().toUpperCase().trim();

        if (str.length() != 2) {
            System.out.println("Invalid input length");
            return;
        }

        char majorChar = str.charAt(0);
        char statusChar = str.charAt(1);

        String major;
        switch (majorChar) {
            case 'M': major = "Mathematics"; break;
            case 'C': major = "Computer Science"; break;
            case 'I': major = "Information Technology"; break;
            default: System.out.println("Invalid major code"); return;
        }

        String status;
        switch (statusChar) {
            case '1': status = "Freshman"; break;
            case '2': status = "Sophomore"; break;
            case '3': status = "Junior"; break;
            case '4': status = "Senior"; break;
            default: System.out.println("Invalid status code"); return;
        }

        System.out.println(major + " " + status);
    }
}
