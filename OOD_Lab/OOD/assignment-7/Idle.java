public class Idle implements State {
    VendingMachine vendingMachine;
    Idle(VendingMachine vendingMachine){
        this.vendingMachine = vendingMachine;
    }
    @Override
    public void insertDollar() {
        System.out.println("Dollar Inseted");
        vendingMachine.setState(vendingMachine.hasOneDollar);
    }
    @Override
    public void ejectkMoney() {
        System.out.println("No Money to eject");
    }
    @Override
    public void dispense() {
        System.out.println("Please insert a dollar");
    }
}
