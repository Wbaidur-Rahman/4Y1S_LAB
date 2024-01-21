import java.util.ArrayList;

public class PetShop implements Shop{

    private ArrayList <Pet> petList;
    PetShop(){
        this.petList = new ArrayList<Pet>();
    }

    @Override
    public void add(Pet pet) {
        this.petList.add(pet);
    }
    
    @Override
    public void sell(String petName) {
        boolean ok=false;
        for(Pet pet : this.petList){
            if(petName.equals(pet.getName()))
            {
                System.out.println("Sell the pet "+ petName);
                ok=true;
                break;
            }

        }
        if(!ok) System.out.println("No "+petName);
    }

    @Override
    public void delivery(String address) {
        System.out.println("Delivery the pet at "+ address);
    }

}
