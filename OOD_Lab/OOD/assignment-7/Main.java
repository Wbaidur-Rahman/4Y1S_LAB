public class Main {
    public static void main(String[] args) {
        VendingMachine vendingMachine = new VendingMachine(2);
        vendingMachine.insertDollar();
        vendingMachine.insertDollar();
        vendingMachine.ejectkMoney();
        vendingMachine.insertDollar();
        vendingMachine.dispense();
        vendingMachine.ejectkMoney();
        vendingMachine.insertDollar();
        vendingMachine.dispense();
        vendingMachine.insertDollar();
        vendingMachine.dispense();
        vendingMachine.ejectkMoney();
    }
}
