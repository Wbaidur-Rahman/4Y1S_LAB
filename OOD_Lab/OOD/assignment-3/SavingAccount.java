public class SavingAccount extends Account{

    SavingAccount(String accountNumber, int balance){
        this.setAccountNumber(accountNumber);
        this.setAccountBalance(balance);
    }
    @Override
    public int withdraw(int amount) {
        System.out.println("Request can not be completed as it it a saving account!");
        return 0;
    }

    @Override
    public void transfer(Account toAccount, int amount) {
        System.out.println("Request can not be completed as it it a saving account!");
    } 

    void Interest(){
        System.out.println("Interest is prohibited");
    }
}
