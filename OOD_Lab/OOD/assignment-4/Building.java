import java.util.ArrayList;

public class Building extends Housing{
    ArrayList <Housing> structures;

    Building(String name){
        this.name = name;
        this.structures = new ArrayList<Housing>();
    }

    public int addStructures(Housing structure){
        structures.add(structure);
        return structures.size()-1;
    }

    public Housing getStructure(int id){
        return structures.get(id);
    }

}