public class HasOneDollar implements State{
    VendingMachine vendingMachine;
    HasOneDollar(VendingMachine vendingMachine){
        this.vendingMachine = vendingMachine;
    }

    @Override
    public void insertDollar() {
       System.out.println("Already Has A Dollar");
    }

    @Override
    public void ejectkMoney() {
        System.out.println("Money Ejected");
        vendingMachine.setState(vendingMachine.idlestate);
    }
    
    @Override
    public void dispense() {
        if(vendingMachine.count >0 ){
            vendingMachine.count --;
            System.out.println("Relesing Product");
            vendingMachine.setState(vendingMachine.idlestate);
        }
        else{
            vendingMachine.setState(vendingMachine.outOfStock);
        }
    }

    
}