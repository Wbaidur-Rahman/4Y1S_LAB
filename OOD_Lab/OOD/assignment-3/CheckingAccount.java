public class CheckingAccount extends Account {

    CheckingAccount(String accountNumber, int balance){
        this.setAccountNumber(accountNumber);
        this.setAccountBalance(balance);
    }
    @Override
    public int withdraw(int amount) {
        if(this.getAccountBalance() >= amount){
            System.out.println("Withdraw task completed in checking account");
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
        if(this.withdraw(amount) == 1){
            System.out.println("Transfering from checking account");
            toAccount.deposit(amount);
        };    
    }
    
}
