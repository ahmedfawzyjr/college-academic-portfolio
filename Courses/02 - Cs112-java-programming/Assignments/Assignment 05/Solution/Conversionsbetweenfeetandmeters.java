public class ConversionsBetweenFeetAndMeters {
    public static void main(String[] args) {
        System.out.println("Feet     Meters    |    Meters    Feet");
        System.out.println("-----------------------------------------");
        for (double feet = 1.0, meters = 20.0; feet <= 10.0; feet++, meters += 5.0) {
            System.out.printf("%-8.1f %-9.3f |    %-9.1f %-7.3f%n",
                    feet, footToMeter(feet), meters, meterToFoot(meters));
        }
    }

    public static double footToMeter(double foot) {
        return 0.305 * foot;
    }

    public static double meterToFoot(double meter) {
        return 3.279 * meter;
    }
}
