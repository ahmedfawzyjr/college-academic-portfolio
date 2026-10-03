// shared/programming-patterns/SingletonPattern.java
// Thread-safe Singleton Design Pattern in Java

public class SingletonPattern {
    private static volatile SingletonPattern instance;
    private String configuration;

    private SingletonPattern() {
        this.configuration = "Default System Config";
    }

    public static SingletonPattern getInstance() {
        if (instance == null) {
            synchronized (SingletonPattern.class) {
                if (instance == null) {
                    instance = new SingletonPattern();
                }
            }
        }
        return instance;
    }

    public String getConfiguration() {
        return configuration;
    }
}
