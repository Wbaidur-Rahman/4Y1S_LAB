public class User {
    public static void main(String[] args) {
        BankService service = new BankService();
        String savingId = service.createNewAccount("saving", "s1", 10000);
        String checkingId = service.createNewAccount("checking", "c10", 50000);
        String investId = service.createNewAccount("", "i20", 90000);

        SavingAccount mySavingAccount = (SavingAccount)service.getAccount(savingId);
        CheckingAccount myCheckingAccount = (CheckingAccount) service.getAccount(checkingId);
        InvestmentAccount myInvestmentAccount = (InvestmentAccount) service.getAccount(investId);

        myCheckingAccount.deposit(100000);
        myInvestmentAccount.Interest();
        service.transferMoney(checkingId, investId, 70000);

        System.out.println(mySavingAccount.getAccountBalance());
        System.out.println(myCheckingAccount.getAccountBalance());
        System.out.println(myInvestmentAccount.getAccountBalance());
    }
}
