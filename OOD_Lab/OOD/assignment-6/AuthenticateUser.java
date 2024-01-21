public class AuthenticateUser extends Decorator {
    AuthenticateUser(Page page){
        super(page);
    }

    public void authenticate(){
        System.out.println("Authenticating User");
    }

    public void display(){
        super.display();
        this.authenticate();
    }
}
