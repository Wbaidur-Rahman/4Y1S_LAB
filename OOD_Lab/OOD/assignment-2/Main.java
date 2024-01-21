import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        PetShop petShop = new PetShop();
        Pet cat;
        Pet dog;
        String[] cats = {"Volvo", "BMW", "Ford", "Mazda"};
        String[] dogs = {"A", "B", "C", "D"};
        for(int i=0;i<4;i++){
            cat = new Cat();
            cat.setName(cats[i]);
            dog = new Dog();
            dog.setName(dogs[i]);
            petShop.add(cat);
            petShop.add(dog);
        }
        try {
            File myFile = new File("input.txt");
            Scanner myReader = new Scanner(myFile);
            while(myReader.hasNextLine()){
                String name = myReader.nextLine();
                petShop.sell(name);
            }
            
        } catch (FileNotFoundException e) {
            System.out.println("Some Error Occured");
            e.printStackTrace();
        }

        while(true){
            String name;
            System.out.println("Enter the pet you want to buy");
            name = scanner.nextLine();
            if(name.equals("")){
                break;
            }
            petShop.sell(name);
        }
    }
}
