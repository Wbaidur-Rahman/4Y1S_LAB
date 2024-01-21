public class InvestmentAccount extends Account{

    InvestmentAccount(String accountNumber, int balance){
        this.setAccountNumber(accountNumber);
        this.setAccountBalance(balance);
    }
    @Override
    public int withdraw(int amount) {
        if(this.getAccountBalance() >= amount){
            System.out.println("Withdraw task completed in investment account");
            this.setAccountBalance(this.getAccountBalance()-amount);
            return 1;
        }
        else{
            System.out.println("Not sufficient balance");
            return 0;
        }
    }

    @Override
    public void transfer(Account toAccount, int amount) {
        System.out.println("In Investment account");
        System.out.println("transfer Request can not be completed as it is an Investment account!");
    } 

    void Interest(){
        System.out.println("Interest is prohibited in Islam");
    }
}
