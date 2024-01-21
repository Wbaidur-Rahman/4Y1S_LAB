import java.util.Hashtable;

public class BankService {
    private Hashtable<String, Account> accounts;

    BankService(){
        this.accounts = new Hashtable<String, Account>();
    }

    public String createNewAccount(String type, String accountNumber, int accountBalance){
        // Account newAccount;


        switch (type) {
            case "saving":
                SavingAccount sAccount = new SavingAccount(accountNumber, accountBalance);
                this.accounts.put(sAccount.getAccountNumber(), sAccount);
                return sAccount.getAccountNumber();
            case "checking":
                CheckingAccount cAccount = new CheckingAccount(accountNumber, accountBalance);
                this.accounts.put(cAccount.getAccountNumber(), cAccount);
                return cAccount.getAccountNumber();
            default: 
                InvestmentAccount iAccount = new InvestmentAccount(accountNumber, accountBalance);
                this.accounts.put(iAccount.getAccountNumber(), iAccount);
                return iAccount.getAccountNumber();
        }
        // switch (type) {
        //     case "saving":
        //         newAccount = new SavingAccount(accountNumber, accountBalance);
        //         break;
        //     case "checking":
        //         newAccount = new CheckingAccount(accountNumber, accountBalance);
        //         break;
        //     default: 
        //         newAccount = new InvestmentAccount(accountNumber, accountBalance);
        //         break;
        // }
        // this.accounts.put(newAccount.getAccountNumber(), newAccount);
        // return newAccount.getAccountNumber();
    }

    public void transferMoney(String from, String to, int amount){
        Account fromAccount = accounts.get(from);
        Account toAccount = accounts.get(to);
        fromAccount.transfer(toAccount, amount);
    }

    Account getAccount(String accoutNumber){
        return accounts.get(accoutNumber);
    }
}
