public class AuthorizedPage extends Decorator{
    
    AuthorizedPage(Page page) {
        super(page);
    } 

    void authorise(){
        System.out.println("Authorising user!!!");
    }

    public void display(){
        super.display();
        this.authorise();
    }
}
