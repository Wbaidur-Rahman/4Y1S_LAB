abstract class Pet {
    private String name = "No Name Assigned" ;
    void setName(String name){
        this.name = name;
    }
    String getName(){
        return this.name;
    }

    public abstract void petCare();
}