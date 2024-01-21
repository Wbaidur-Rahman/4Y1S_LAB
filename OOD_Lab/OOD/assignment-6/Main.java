public class Main {
    public static void main(String[] args) {
        Page page = new WebPage();
        page = new AuthenticateUser(page);
        page = new AuthorizedPage(page);
        page.display();
    }
}
