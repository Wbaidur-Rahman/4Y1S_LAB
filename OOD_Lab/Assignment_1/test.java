// In Java, multiple inheritance is not supported through class inheritance, 
// where a class can only extend one superclass

// Interface for the first behavior
interface Swimming {
    void swim();
}

// Interface for the second behavior
interface Flying {
    void fly();
}

// Class that implements both Swimming and Flying interfaces
class Bird implements Swimming, Flying {
    @Override
    public void swim() {
        System.out.println("Bird is swimming");
    }

    @Override
    public void fly() {
        System.out.println("Bird is flying");
    }
}

public class test {
    public static void main(String[] args) {
        Bird bird = new Bird();
        bird.swim(); // Calls the swim method from the Swimming interface
        bird.fly();  // Calls the fly method from the Flying interface
    }
}
