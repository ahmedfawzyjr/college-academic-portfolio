// Object-Oriented Programming (Java) - Polymorphism & Inheritance Example

abstract class Shape {
    protected String name;
    public Shape(String name) { this.name = name; }
    public abstract double getArea();
}

class Circle extends Shape {
    private double radius;
    public Circle(double radius) {
        super("Circle");
        this.radius = radius;
    }
    @Override
    public double getArea() { return Math.PI * radius * radius; }
}

public class InheritanceExample {
    public static void main(String[] args) {
        Shape c = new Circle(5.0);
        System.out.println(c.name + " Area: " + c.getArea());
    }
}
