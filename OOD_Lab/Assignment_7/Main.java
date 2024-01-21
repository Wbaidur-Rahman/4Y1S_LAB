public class Main {
    public static void main(String[] args) {
        VendingMachine vendingMachine = new VendingMachine(2);
        vendingMachine.ejectMoney();
        vendingMachine.insertDollar();
        vendingMachine.insertDollar();
        vendingMachine.dispense();
        vendingMachine.ejectMoney();
        vendingMachine.insertDollar();
        vendingMachine.dispense();
        // vendingMachine.insertDollar();
        vendingMachine.dispense();
        System.err.println(vendingMachine.getCount());
    }
}
