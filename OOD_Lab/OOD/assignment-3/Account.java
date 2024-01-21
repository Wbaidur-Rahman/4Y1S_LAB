public abstract class Account {
    private int accountBalance;
    private String accountNumber;
    public abstract int withdraw(int amount);
    public abstract void transfer(Account toAccount, int amount);

    public void deposit(int amount){
        this.accountBalance += amount;
    }
    
    public void setAccountNumber(String accountNumber){
        this.accountNumber = accountNumber;
    }
    public String getAccountNumber(){
        return this.accountNumber;
    }
    
    public void setAccountBalance(int accountBalance){
        this.accountBalance = accountBalance;
    }
    public int getAccountBalance(){
        return this.accountBalance;
    }
}
