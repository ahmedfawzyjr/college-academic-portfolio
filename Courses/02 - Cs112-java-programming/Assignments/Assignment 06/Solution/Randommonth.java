public class RandomMonth {
    public static void main(String[] args) {
        int monthNumber = (int)(Math.random() * 12) + 1;
        String[] months = {
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        };
        System.out.println("Generated Month (" + monthNumber + "): " + months[monthNumber - 1]);
    }
}
