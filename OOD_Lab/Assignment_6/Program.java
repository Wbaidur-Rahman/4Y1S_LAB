public class Program {
    public static void main(String args[]) {
        Webpage myPage = new BasicWebPage();
        myPage = new AuthenticatedUser(myPage);
        myPage = new AuthorizedWebpage(myPage);
        myPage.display();
    }
}