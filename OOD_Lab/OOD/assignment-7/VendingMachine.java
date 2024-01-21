public class VendingMachine implements State{
    Idle idlestate;
    HasOneDollar hasOneDollar; 
    OutOfStock outOfStock;
    State currenState;
    int count ;

    VendingMachine(int count){
        this.idlestate = new Idle(this);
        this.hasOneDollar = new HasOneDollar(this);
        this.outOfStock = new OutOfStock(this);
        this.count = count;
        this.currenState =this.idlestate;
    }

    void setState(State state){
        this.currenState = state;
    }

    @Override
    public void insertDollar() {
        currenState.insertDollar();
    }

    @Override
    public void ejectkMoney() {
        currenState.ejectkMoney();
    }

    @Override
    public void dispense() {
        currenState.dispense();
    }
}
