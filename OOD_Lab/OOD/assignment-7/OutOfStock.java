public class OutOfStock implements State{
    VendingMachine vendingMachine;
    OutOfStock(VendingMachine vendingMachine){
        this.vendingMachine = vendingMachine;
    }
    @Override
    public void insertDollar() {
        System.out.println("OutOfStock");
    }
    @Override
    public void ejectkMoney() {
        System.out.println("OutOfStock");
    }
    @Override
    public void dispense() {
        System.out.println("OutOfStock");
    }
}
