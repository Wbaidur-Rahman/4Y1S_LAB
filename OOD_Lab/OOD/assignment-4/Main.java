public class Main {
    public static void main(String[] args) {
        Building Building =  new Building("Hall");
        Building floor1 =  new Building("Forth floor");
        Building floor2 = new Building("Forth floor");

        Building.addStructures(floor1);
        Building.addStructures(floor2);
        int myfloor = floor1.addStructures(floor2);

        Room r1 = new Room("401");
        Room r2 = new Room("402");
        Room r3 = new Room("403");
        Room r4 = new Room("404");
        Room r5 = new Room("405");

        int myroom = floor1.addStructures(r5);
        int nextroom = floor1.addStructures(r4);
        floor1.addStructures(r3);
        floor1.addStructures(r2);
        floor1.addStructures(r1);

        Building.enter();
        Building currentfloor = (Building) Building.getStructure(myfloor);
        currentfloor.enter();
        Room currentRoom = (Room) currentfloor.getStructure(myroom);
        currentRoom.enter();
        currentRoom.greet();
        currentRoom = (Room) currentfloor.getStructure(nextroom);
        currentRoom.enter();

    }
}
