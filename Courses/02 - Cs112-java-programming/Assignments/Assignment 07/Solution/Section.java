public class Section {
    private String sectionId;
    private String courseName;
    private int capacity;
    private int enrolledStudents;

    public Section(String sectionId, String courseName, int capacity) {
        this.sectionId = sectionId;
        this.courseName = courseName;
        this.capacity = capacity;
        this.enrolledStudents = 0;
    }

    public boolean enrollStudent() {
        if (enrolledStudents < capacity) {
            enrolledStudents++;
            return true;
        }
        return false;
    }

    public String getSectionId() { return sectionId; }
    public String getCourseName() { return courseName; }
    public int getCapacity() { return capacity; }
    public int getEnrolledStudents() { return enrolledStudents; }

    @Override
    public String toString() {
        return "Section " + sectionId + " (" + courseName + "): " + enrolledStudents + "/" + capacity + " enrolled";
    }

    public static void main(String[] args) {
        Section sec = new Section("SEC-01", "OOP Java", 30);
        sec.enrollStudent();
        sec.enrollStudent();
        System.out.println(sec);
    }
}
